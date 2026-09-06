"""Split a markdown skill into units and decide, without any model, which units
may be touched at all.

The guard list is the product. A model can misjudge a paragraph; it cannot
misjudge a unit it never sees. Anything carrying a fact the model could not
know on its own — a path, a URL, an env var, a flag, a number with a unit, a
backtick span, a code fence, a table, the frontmatter — is untouchable here and
copied verbatim by the pruner regardless of what the classifier says.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

# Anything matching one of these carries a fact. Keep verbatim.
GUARDS: list[tuple[str, re.Pattern[str]]] = [
    ("backtick", re.compile(r"`[^`]+`")),
    ("url", re.compile(r"https?://|www\.|\b[\w-]+\.(com|dev|ai|io|org|net|cn)\b")),
    ("path", re.compile(r"(^|[\s(\"'])(~|\.{1,2})?/[\w.@-]+(/[\w.@-]+)*|(^|\s)\.?[\w-]*\.(py|sh|ts|tsx|js|jsx|md|json|jsonl|ya?ml|toml|txt|csv|tsv|html?|xlsx?|docx?|pptx?|pdf|png|jpe?g|gif|svg|mp4|mov|zip|env|ipynb|sql|ini|cfg|lock)\b")),
    ("env_var", re.compile(r"\b[A-Z][A-Z0-9]*_[A-Z0-9_]+\b")),
    ("cli_flag", re.compile(r"(^|\s)--?[a-zA-Z][\w-]*")),
    ("number_unit", re.compile(r"\b\d+(\.\d+)?\s?(s|ms|sec|min|h|hr|%|px|[kmgt]b|x|×|k|m|token|char|line|word|day|week|month|year|row|column|page|slide|bp|bps)s?\b", re.I)),
    ("currency", re.compile(r"[$€£¥]\s?\d|\b\d+(\.\d+)?\s?(bn|bps|usd|eur|rmb|cny|billion|million|trillion)\b", re.I)),
    ("formula", re.compile(r"[A-Za-z%)\]]\s?[=×÷]\s?[\w($(\[]|\w+\s*/\s*\w+\s*[=×]|→")),
    ("range", re.compile(r"\b\d+\s?[-–]\s?\d+\b")),
    ("big_number", re.compile(r"\b\d{3,}\b")),
    ("version", re.compile(r"\bv?\d+\.\d+(\.\d+)?\b")),
    ("mention", re.compile(r"(^|\s)@[\w-]+")),
    ("code_word", re.compile(r"\b\w+\(\)|\b\w+\.\w+\(|\{\{|\}\}|\$\{")),
]
MIN_WORDS = 8  # shorter than this is a label, not prose worth pruning


@dataclass
class Unit:
    kind: str  # frontmatter | heading | code | table | list | paragraph | html | blank
    text: str
    start: int  # 1-based line numbers, inclusive
    end: int
    touchable: bool = False
    guard: str = ""  # why it is untouchable, "" if touchable
    prefix: str = ""  # list bullet / indentation to preserve on replacement
    labels: list[str] = field(default_factory=list)

    @property
    def words(self) -> int:
        return word_count(self.text)

    @property
    def body(self) -> str:
        return self.text[len(self.prefix):] if self.prefix else self.text


_FENCE = re.compile(r"^\s*(```|~~~)")
_HEADING = re.compile(r"^\s{0,3}#{1,6}\s")
_LIST = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")
_TABLE = re.compile(r"^\s*\|")
_HTML = re.compile(r"^\s*<")


def word_count(text: str) -> int:
    """Words for English, characters/2 for CJK, so a Chinese paragraph is not
    mistaken for a three-word label."""
    cjk = sum(1 for c in text if "\u4e00" <= c <= "\u9fff")
    return len(re.sub(r"[\u4e00-\u9fff]", " ", text).split()) + cjk // 2


def guard_reason(text: str) -> str:
    """Return the name of the first guard that fires, or "" if none."""
    for name, rx in GUARDS:
        if rx.search(text):
            return name
    return ""


def segment(md: str) -> list[Unit]:
    lines = md.splitlines()
    units: list[Unit] = []
    i, n = 0, len(lines)

    def push(kind: str, start: int, end: int, prefix: str = "") -> None:
        text = "\n".join(lines[start:end])
        u = Unit(kind=kind, text=text, start=start + 1, end=end, prefix=prefix)
        if kind in ("paragraph", "list"):
            reason = guard_reason(u.body)
            if reason:
                u.guard = reason
            elif word_count(u.body) < MIN_WORDS:
                u.guard = "short"
            elif u.body.rstrip().endswith(":"):
                u.guard = "lead_in"  # introduces a code block or list of facts
            else:
                u.touchable = True
        else:
            u.guard = kind
        units.append(u)

    # frontmatter
    if n and lines[0].strip() == "---":
        j = 1
        while j < n and lines[j].strip() != "---":
            j += 1
        if j < n:
            push("frontmatter", 0, j + 1)
            i = j + 1

    while i < n:
        line = lines[i]
        if not line.strip():
            push("blank", i, i + 1)
            i += 1
        elif _FENCE.match(line):
            fence = _FENCE.match(line).group(1)
            j = i + 1
            while j < n and not lines[j].strip().startswith(fence):
                j += 1
            push("code", i, min(j + 1, n))
            i = j + 1
        elif _HEADING.match(line):
            push("heading", i, i + 1)
            i += 1
        elif _TABLE.match(line):
            j = i
            while j < n and _TABLE.match(lines[j]):
                j += 1
            push("table", i, j)
            i = j
        elif _HTML.match(line):
            j = i
            while j < n and lines[j].strip():
                j += 1
            push("html", i, j)
            i = j
        elif _LIST.match(line):
            m = _LIST.match(line)
            indent = len(m.group(1))
            j = i + 1
            # continuation lines: indented deeper than the bullet, not a new bullet
            while j < n and lines[j].strip() and not _LIST.match(lines[j]) and not _HEADING.match(lines[j]) \
                    and not _FENCE.match(lines[j]) and (len(lines[j]) - len(lines[j].lstrip())) > indent:
                j += 1
            push("list", i, j, prefix=m.group(0))
            i = j
        else:
            j = i + 1
            while j < n and lines[j].strip() and not _LIST.match(lines[j]) and not _HEADING.match(lines[j]) \
                    and not _FENCE.match(lines[j]) and not _TABLE.match(lines[j]):
                j += 1
            push("paragraph", i, j)
            i = j
    return units


def join(units: list[Unit]) -> str:
    return "\n".join(u.text for u in units) + ("\n" if units else "")


def approx_tokens(text: str) -> int:
    """Rough token count without a tokenizer dependency: ~4 chars per token for
    English, ~1.5 chars per token for CJK. Good enough for a percentage."""
    cjk = sum(1 for c in text if "一" <= c <= "鿿")
    other = len(text) - cjk
    return int(other / 4 + cjk / 1.5)


def summary(units: list[Unit]) -> dict:
    touch = [u for u in units if u.touchable]
    total = approx_tokens(join(units))
    return {
        "units": len(units),
        "touchable": len(touch),
        "touchable_tokens": sum(approx_tokens(u.body) for u in touch),
        "total_tokens": total,
        "guards": {g: sum(1 for u in units if u.guard == g) for g in sorted({u.guard for u in units if u.guard and u.kind in ("paragraph", "list")})},
    }
