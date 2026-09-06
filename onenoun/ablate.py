"""Prove it. Generate tasks from the skill's own description, answer each with
the original and the pruned skill loaded, and let a blind judge compare."""

from __future__ import annotations

import random
import re
from dataclasses import dataclass, field

from .classify import prompt_text
from .drivers import Driver

TASKS_SCHEMA = {"type": "object", "properties": {"tasks": {"type": "array", "items": {"type": "string"}}}, "required": ["tasks"]}
JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "winner": {"type": "string", "enum": ["A", "B", "tie"]},
        "reason": {"type": "string", "minLength": 120},
        "uncertainties": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 40}},
    },
    "required": ["winner", "reason", "uncertainties"],
}
# Models sometimes fill a schema with placeholder values ("test", "a", "b").
# A judgement like that is noise wearing the shape of a result, so it is
# rejected and the call retried rather than counted.
PLACEHOLDER = re.compile(r"^(test\d*|foo|bar|baz|placeholder|n/?a|none|[a-z]|\.+)$", re.I)


def _degenerate(j: dict) -> str:
    reason = (j.get("reason") or "").strip()
    if PLACEHOLDER.match(reason) or len(reason) < 60:
        return f"reason too short or placeholder: {reason!r}"
    unc = [u.strip() for u in j.get("uncertainties") or []]
    if not unc:
        return "no uncertainties listed"
    if any(PLACEHOLDER.match(u) or len(u) < 25 for u in unc):
        return f"placeholder uncertainty: {unc!r}"
    return ""


@dataclass
class Trial:
    task: str
    original: str
    pruned: str
    pruned_was: str  # "A" or "B"
    winner: str  # "original" | "pruned" | "tie"
    reason: str
    uncertainties: list[str] = field(default_factory=list)


def description_and_headings(md: str) -> tuple[str, str]:
    desc = ""
    m = re.match(r"---\n(.*?)\n---", md, re.S)
    if m:
        d = re.search(r"^description:\s*(.*)$", m.group(1), re.M)
        if d:
            desc = d.group(1).strip().strip("\"'")
    heads = [l.strip("# ").strip() for l in md.splitlines() if re.match(r"^\s{0,3}#{1,6}\s", l)]
    return desc or md[:400], "\n".join(f"- {h}" for h in heads[:25])


def make_tasks(md: str, k: int, driver: Driver) -> list[str]:
    desc, heads = description_and_headings(md)
    p = prompt_text("tasks.md").replace("{k}", str(k)).replace("{description}", desc).replace("{headings}", heads)
    return [t for t in driver.json(p, TASKS_SCHEMA).get("tasks", []) if t.strip()][:k]


# The skill under test may tell the model to run things. It has no tools in
# this session, and the CLI errors out if it keeps trying; say so up front.
NO_TOOLS = "\n\n(You have no tools in this session. Answer entirely in text; if the task would need a tool, say what you would do.)"


def run(original: str, pruned: str, k: int, driver: Driver, seed: int = 0, tasks: list[str] | None = None,
        progress=lambda s: None) -> list[Trial]:
    rng = random.Random(seed)
    tasks = tasks or make_tasks(original, k, driver)
    trials = []
    for n, task in enumerate(tasks, 1):
        q = task + NO_TOOLS
        progress(f"task {n}/{len(tasks)}: original")
        ans_o = driver.text(q, system=original)
        progress(f"task {n}/{len(tasks)}: pruned")
        ans_p = driver.text(q, system=pruned)
        pruned_is_a = rng.random() < 0.5
        a, b = (ans_p, ans_o) if pruned_is_a else (ans_o, ans_p)
        progress(f"task {n}/{len(tasks)}: judge")
        jp = prompt_text("judge.md").replace("{task}", task).replace("{a}", a).replace("{b}", b)
        for attempt in range(3):
            j = driver.json(jp, JUDGE_SCHEMA)
            bad = _degenerate(j)
            if not bad:
                break
            progress(f"task {n}/{len(tasks)}: judge returned {bad}; retrying")
        else:
            raise RuntimeError(f"judge kept returning placeholder output for task {n}: {bad}")
        w = j.get("winner", "tie")
        winner = "tie" if w == "tie" else ("pruned" if (w == "A") == pruned_is_a else "original")
        trials.append(Trial(task, ans_o, ans_p, "A" if pruned_is_a else "B", winner, j.get("reason", ""), j.get("uncertainties", [])))
    return trials


def report(name: str, trials: list[Trial], before: int, after: int, cost: float, calls: int, driver: str) -> str:
    wins = sum(t.winner == "pruned" for t in trials)
    ties = sum(t.winner == "tie" for t in trials)
    losses = sum(t.winner == "original" for t in trials)
    verdict = "pruned is not worse" if losses == 0 else ("mixed" if wins >= losses else "pruned is worse — do not ship")
    lines = [
        f"# onenoun ablation — {name}",
        "",
        f"**pruned ≥ original in {wins + ties}/{len(trials)}** (won {wins}, tied {ties}, lost {losses}) · "
        f"tokens {before} → {after} ({100 * (after - before) / before:+.0f}%) · **{verdict}**",
        f"driver: {driver}, {calls} call(s), ${cost:.2f}. Blind pairwise judge; A/B order randomised per task.",
        "",
        "| # | task | winner | judge's reason |",
        "|---|---|---|---|",
    ]
    for n, t in enumerate(trials, 1):
        lines.append(f"| {n} | {t.task.replace('|', '/')[:110]} | {t.winner} | {t.reason.replace('|', '/').replace(chr(10), ' ')[:200]} |")
    lines += ["", "## Judge's uncertainties (列出所有不自信的点)", ""]
    for n, t in enumerate(trials, 1):
        for u in t.uncertainties:
            lines.append(f"- task {n}: {u}")
    lines += ["", "## Transcripts", ""]
    for n, t in enumerate(trials, 1):
        lines += [f"### Task {n}", "", t.task, "", "**With original skill**", "", t.original.strip(), "",
                  "**With pruned skill**", "", t.pruned.strip(), ""]
    return "\n".join(lines) + "\n"
