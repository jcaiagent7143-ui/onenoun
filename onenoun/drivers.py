"""Model drivers. The model work is done by an agent CLI the user already has,
called as a subprocess. No SDK, no API key handling, nothing stored.

    claude          claude -p, structured output via --json-schema (tested)
    shell:<tmpl>    any command; {prompt} is substituted, stdout is the answer,
                    the first JSON object in stdout is the structured answer.
                    e.g.  --driver "shell:codex exec -q {prompt}"
"""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import tempfile
from dataclasses import dataclass, field


class DriverError(RuntimeError):
    pass


@dataclass
class Reply:
    text: str
    data: dict | None = None
    cost_usd: float = 0.0
    seconds: float = 0.0
    raw: dict = field(default_factory=dict)


class Driver:
    name = "base"
    total_cost = 0.0
    calls = 0

    def json(self, prompt: str, schema: dict, system: str | None = None) -> dict:
        raise NotImplementedError

    def text(self, prompt: str, system: str | None = None) -> str:
        raise NotImplementedError


class ClaudeDriver(Driver):
    """`claude -p` with tools off, no session persistence, no skills."""

    name = "claude"

    def __init__(self, model: str = "sonnet", timeout: int = 300, retries: int = 3):
        self.model, self.timeout, self.retries = model, timeout, retries
        # Run from an empty directory so no CLAUDE.md, memory, or project
        # settings leak into the answers. Both arms of an ablation must see
        # only the skill under test.
        self.cwd = tempfile.mkdtemp(prefix="onenoun-")

    def _run(self, prompt: str, system: str | None, schema: dict | None, single_turn: bool = False) -> Reply:
        # The CLI dies on transients often enough to matter over a 16-call
        # ablation: a hallucinated tool call it has no tools for, a stdin
        # hiccup, an empty stop_sequence turn. Retry with backoff; three
        # failures in a row is a real error.
        import time as _t

        last = None
        for attempt in range(self.retries):
            try:
                return self._run_once(prompt, system, schema, single_turn)
            except DriverError as e:
                last = e
                if attempt + 1 < self.retries:
                    _t.sleep(2 * (attempt + 1))
        raise last

    def _run_once(self, prompt: str, system: str | None, schema: dict | None, single_turn: bool = False) -> Reply:
        import time

        cmd = ["claude", "-p", "--model", self.model, "--tools", "", "--no-session-persistence",
               "--disable-slash-commands", "--setting-sources", "", "--strict-mcp-config",
               "--settings", '{"autoMemoryEnabled": false}', "--output-format", "json"]
        if single_turn:
            # The skill under test often tells the model to read or write
            # files. With no tools a multi-turn run dies on the attempt, so
            # plain-text calls get one turn and answer in prose instead.
            # Structured-output calls must NOT be capped: the schema is
            # delivered as a tool call and needs the turn after it.
            cmd += ["--max-turns", "1"]
        if system:
            cmd += ["--append-system-prompt", system]
        if schema:
            cmd += ["--json-schema", json.dumps(schema)]
        t = time.time()
        try:
            out = subprocess.run(cmd + [prompt], capture_output=True, text=True, timeout=self.timeout, cwd=self.cwd,
                                 stdin=subprocess.DEVNULL)
        except FileNotFoundError:
            raise DriverError("`claude` is not on PATH. Install Claude Code or pass --driver \"shell:...\".")
        except subprocess.TimeoutExpired:
            raise DriverError(f"claude timed out after {self.timeout}s")
        try:
            d = json.loads(out.stdout)
        except json.JSONDecodeError:
            raise DriverError(f"claude exited {out.returncode}: {(out.stderr or out.stdout).strip()[:400]}")
        if d.get("is_error") or out.returncode != 0:
            # stop_reason "tool_use" means the skill under test told the model
            # to call a tool it has no access to here. The turns before that
            # are still a real answer, so use them rather than discarding the
            # task; only a genuinely empty result is an error.
            text = d.get("result") or _text_from_turns(d)
            if d.get("stop_reason") == "tool_use" and text:
                return Reply(text=text, data=None, cost_usd=float(d.get("total_cost_usd") or 0),
                             seconds=time.time() - t, raw=d)
            raise DriverError(f"claude: {d.get('result') or d.get('stop_reason') or out.returncode}")
        r = Reply(text=d.get("result") or "", data=d.get("structured_output"), cost_usd=float(d.get("total_cost_usd") or 0),
                  seconds=time.time() - t, raw=d)
        Driver.total_cost += r.cost_usd
        Driver.calls += 1
        return r

    def json(self, prompt, schema, system=None):
        r = self._run(prompt, system, schema)
        if r.data is None:
            r.data = extract_json(r.text)
        if r.data is None:
            raise DriverError("model returned no JSON object")
        return r.data

    def text(self, prompt, system=None):
        return self._run(prompt, system, None, single_turn=True).text


class ShellDriver(Driver):
    """Any command line. `{prompt}` is replaced (shell-quoted) by the prompt;
    if a system prompt is given it is prepended to the prompt as a block."""

    name = "shell"

    def __init__(self, template: str, timeout: int = 300):
        self.template, self.timeout = template, timeout

    def _run(self, prompt: str, system: str | None) -> str:
        full = f"<system>\n{system}\n</system>\n\n{prompt}" if system else prompt
        cmd = self.template.replace("{prompt}", shlex.quote(full))
        try:
            out = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=self.timeout, stdin=subprocess.DEVNULL)
        except subprocess.TimeoutExpired:
            raise DriverError(f"driver timed out after {self.timeout}s: {self.template}")
        if out.returncode != 0:
            raise DriverError(f"driver exited {out.returncode}: {(out.stderr or out.stdout).strip()[:500]}")
        Driver.calls += 1
        return out.stdout

    def json(self, prompt, schema, system=None):
        prompt = f"{prompt}\n\nAnswer with a single JSON object matching this schema, nothing else:\n{json.dumps(schema)}"
        d = extract_json(self._run(prompt, system))
        if d is None:
            raise DriverError("driver returned no JSON object")
        return d

    def text(self, prompt, system=None):
        return self._run(prompt, system)


def _text_from_turns(d: dict) -> str:
    """Best-effort text from a run that ended mid-tool-call."""
    parts = []
    for msg in d.get("messages") or []:
        for block in (msg.get("content") if isinstance(msg.get("content"), list) else []) or []:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block["text"])
    return "\n".join(parts).strip()


def extract_json(text: str) -> dict | None:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def make_driver(spec: str, model: str) -> Driver:
    if spec == "claude":
        return ClaudeDriver(model=model)
    if spec.startswith("shell:"):
        return ShellDriver(spec[len("shell:"):])
    raise DriverError(f"unknown driver {spec!r}; use 'claude' or 'shell:<command with {{prompt}}>'")
