"""Parse lexicon.md and run activation tests."""

from __future__ import annotations

import importlib.resources
import pathlib
import re
from dataclasses import dataclass, field

from .drivers import Driver

FIELDS = ("zh", "replace", "subsumes", "test", "expect")


@dataclass
class Term:
    name: str
    zh: str = ""
    replace: str = ""
    subsumes: str = ""
    test: str = ""
    expect: list[list[str]] = field(default_factory=list)

    def check_answer(self, answer: str) -> list[str]:
        """Return the expect-groups that did not match. Empty list = pass."""
        a = answer.lower()
        return ["|".join(g) for g in self.expect if not any(alt.lower() in a for alt in g)]


def parse_expect(raw) -> list[list[str]]:
    """Accept either the file's "a|b, c" string or a JSON list of such groups."""
    groups = raw.split(",") if isinstance(raw, str) else list(raw)
    return [[alt.strip() for alt in str(g).split("|") if alt.strip()] for g in groups if str(g).strip()]


def format_expect(expect: list[list[str]]) -> str:
    return ", ".join("|".join(g) for g in expect)


def append(term: Term, path: pathlib.Path) -> None:
    """Append a verified term to a lexicon file, creating it if needed."""
    block = (f"\n## {term.name}\n- zh: {term.zh}\n- replace: {term.replace}\n"
             f"- subsumes: {term.subsumes}\n- test: {term.test}\n- expect: {format_expect(term.expect)}\n")
    if not path.exists():
        path.write_text("# Lexicon — verified terms\n\nAdded by `onenoun lexicon verify`. "
                        "Every term here passed its own activation test.\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as f:
        f.write(block)


def default_path() -> pathlib.Path:
    return pathlib.Path(str(importlib.resources.files("onenoun") / "lexicon.md"))


def load(path: pathlib.Path | None = None, extra: pathlib.Path | None = None) -> list[Term]:
    """Load the bundled lexicon, plus a local one if it exists. A local term
    with the same name wins, so a project can override a replacement line."""
    text = (path or default_path()).read_text(encoding="utf-8")
    if extra and extra.exists():
        text += "\n" + extra.read_text(encoding="utf-8")
    terms: list[Term] = []
    cur: Term | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            cur = Term(name=line[3:].strip())
            terms.append(cur)
        elif cur and line.startswith("- "):
            m = re.match(r"- (\w+):\s*(.*)", line)
            if not m or m.group(1) not in FIELDS:
                continue
            k, v = m.group(1), m.group(2).strip()
            if k == "expect":
                cur.expect = parse_expect(v)
            else:
                setattr(cur, k, v)
    by_name: dict[str, Term] = {}
    for t in terms:
        by_name[t.name.lower()] = t
    return list(by_name.values())


def validate(terms: list[Term]) -> list[str]:
    """Shape problems, for tests and for PR review."""
    problems = []
    names = [t.name for t in terms]
    for n in names:
        if names.count(n) > 1:
            problems.append(f"duplicate term {n!r}")
    for t in terms:
        for f in ("zh", "replace", "subsumes", "test"):
            if not getattr(t, f):
                problems.append(f"{t.name}: missing {f}")
        if len(t.expect) < 3:
            problems.append(f"{t.name}: expect needs at least 3 groups")
        if len(t.replace.split()) > 10:
            problems.append(f"{t.name}: replace is longer than 10 words; the point is one line")
    return problems


def verify(candidates: list[Term], driver: Driver) -> tuple[list[Term], list[tuple[Term, list[str], str]]]:
    """Put candidate terms through their own activation test.

    This is what makes the vocabulary open instead of a fixed list of thirty:
    the classifier may name any established method it finds in the customer's
    own skills, and the test decides whether the model really knows it. A term
    the model cannot expand from its name alone is not a term, whatever it is
    called."""
    results = check(candidates, driver)
    passed = [t for t, missing, _ in results if not missing]
    return passed, results


def check(terms: list[Term], driver: Driver) -> list[tuple[Term, list[str], str]]:
    """Ask the model each test question with nothing else. Returns
    (term, missing_groups, answer) per term; missing == [] is a pass."""
    results = []
    for t in terms:
        answer = driver.text(t.test)
        results.append((t, t.check_answer(answer), answer))
    return results
