"""Label touchable units with the model: FACT / METHOD:<term> / FILLER / UNSURE."""

from __future__ import annotations

import importlib.resources
from dataclasses import dataclass, field

from .drivers import Driver
from .lexicon import Term, parse_expect
from .segment import Unit

LABELS = ("FACT", "METHOD", "FILLER", "UNSURE")
# CANDIDATE is assigned by this module, never by the model: a METHOD verdict
# naming a term the lexicon does not have yet.
SCHEMA = {
    "type": "object",
    "properties": {
        "units": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "label": {"type": "string", "enum": list(LABELS)},
                    "terms": {"type": "array", "items": {"type": "string"}},
                    "why": {"type": "string"},
                },
                "required": ["id", "label", "why"],
            },
        },
        "proposals": {
            "type": "array",
            "description": "methodology terms this file re-explains that are NOT already in the lexicon",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "zh": {"type": "string"},
                    "replace": {"type": "string"},
                    "subsumes": {"type": "string"},
                    "test": {"type": "string"},
                    "expect": {"type": "array", "items": {"type": "string"}},
                    "unit_ids": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["name", "replace", "subsumes", "test", "expect", "unit_ids"],
            },
        },
        "uncertainties": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["units", "proposals", "uncertainties"],
}


@dataclass
class Verdict:
    label: str
    term: str = ""  # "; "-joined lexicon term names for METHOD
    why: str = ""

    @property
    def terms(self) -> list[str]:
        return [t for t in self.term.split("; ") if t]


@dataclass
class Audit:
    verdicts: dict[int, Verdict]  # unit index -> verdict
    uncertainties: list[str] = field(default_factory=list)
    proposals: list[Term] = field(default_factory=list)  # candidate terms, unverified
    proposed_for: dict[int, str] = field(default_factory=dict)  # unit index -> proposed term


def prompt_text(name: str) -> str:
    return (importlib.resources.files("onenoun") / "prompts" / name).read_text(encoding="utf-8")


def classify(units: list[Unit], terms: list[Term], driver: Driver, file_text: str) -> Audit:
    touch = [(i, u) for i, u in enumerate(units) if u.touchable]
    if not touch:
        return Audit(verdicts={})
    lex = "\n".join(f"- {t.name} ({t.zh}): {t.subsumes}" for t in terms)
    listing = "\n\n".join(f"[{i}] (lines {u.start}-{u.end})\n{u.body}" for i, u in touch)
    prompt = prompt_text("classify.md").replace("{lexicon}", lex).replace("{file}", file_text).replace("{units}", listing)
    data = driver.json(prompt, SCHEMA)
    names = {t.name.lower(): t.name for t in terms}
    proposals: list[Term] = []
    proposed_for: dict[int, str] = {}
    for row in data.get("proposals", []):
        name = (row.get("name") or "").strip()
        if not name or name.lower() in names:
            continue
        t = Term(name=name, zh=(row.get("zh") or "").strip(), replace=(row.get("replace") or "").strip(),
                 subsumes=(row.get("subsumes") or "").strip(), test=(row.get("test") or "").strip(),
                 expect=parse_expect(row.get("expect") or []))
        if not (t.replace and t.test and t.expect):
            continue
        proposals.append(t)
        for i in row.get("unit_ids") or []:
            proposed_for[int(i)] = name
    verdicts: dict[int, Verdict] = {}
    for row in data.get("units", []):
        i = row.get("id")
        if i not in dict(touch):
            continue
        label = row.get("label", "UNSURE")
        raw = row.get("terms") or ([row["term"]] if row.get("term") else [])
        known = [names[t.strip().lower()] for t in raw if t.strip().lower() in names]
        why = row.get("why", "")
        if label == "METHOD" and (not known or len(known) != len(raw)):
            proposed = [t for t in raw if any(t.strip().lower() == p.name.lower() for p in proposals)]
            if proposed and len(proposed) == len(raw):
                # A candidate term, not yet proven to be in the model. It stays
                # unreplaced until `onenoun lexicon verify` puts it through the
                # activation test.
                label = "CANDIDATE"
                why = f"proposed term {proposed!r} not yet verified. {why}"
                verdicts[i] = Verdict(label=label, term="; ".join(proposed), why=why)
                continue
            label, why = "UNSURE", f"model named a term not in the lexicon: {raw!r}. {why}"
        verdicts[i] = Verdict(label=label, term="; ".join(dict.fromkeys(known)), why=why)
    for i, _ in touch:
        verdicts.setdefault(i, Verdict("UNSURE", why="model returned no label for this unit"))
    return Audit(verdicts=verdicts, uncertainties=list(data.get("uncertainties", [])),
                 proposals=proposals, proposed_for=proposed_for)
