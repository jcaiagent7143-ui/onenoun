"""Pruning is deterministic given the verdicts, never touches guarded units,
and pruning a pruned file with the same verdict rule changes nothing."""

from onenoun.classify import Audit, Verdict
from onenoun.lexicon import load
from onenoun.prune import prune
from onenoun.segment import segment

TERMS = load()
BY = {t.name: t for t in TERMS}

MD = """---
name: demo
description: demo skill
---

# Demo

Run `make test` before every commit and never skip it, even for docs-only changes.

Before accepting any conclusion, take the opposing side and try as hard as you can to break it; look for the strongest objection.

- Remove one component at a time and observe what changes while keeping everything else fixed.
- Keep everything else fixed and compare each variant against the baseline to see what contributes.

This is really important, so please be careful and thoughtful throughout the whole process.

Set API_TOKEN before running anything at all in this repository.
"""


def verdicts_for(units):
    v = {}
    for i, u in enumerate(units):
        if not u.touchable:
            continue
        b = u.body.lower()
        if "opposing side" in b:
            v[i] = Verdict("METHOD", "adversarial review", "")
        elif "one component" in b or "baseline" in b:
            v[i] = Verdict("METHOD", "ablation", "")
        elif "really important" in b:
            v[i] = Verdict("FILLER", "", "")
        else:
            v[i] = Verdict("FACT", "", "")
    return Audit(verdicts=v)


def test_prune_replaces_and_keeps_facts():
    units = segment(MD)
    out, rows = prune(units, verdicts_for(units), TERMS)
    assert "`make test`" in out and "API_TOKEN" in out
    assert BY["adversarial review"].replace in out
    assert out.count(BY["ablation"].replace) == 1, "consecutive same-term units collapse to one line"
    assert "- " + BY["ablation"].replace in out, "list prefix preserved"
    assert "really important" not in out
    assert "opposing side" not in out
    assert "name: demo" in out


def test_prune_is_idempotent():
    units = segment(MD)
    once, _ = prune(units, verdicts_for(units), TERMS)
    units2 = segment(once)
    twice, _ = prune(units2, verdicts_for(units2), TERMS)
    assert once == twice


def test_guarded_units_survive_any_verdict():
    units = segment(MD)
    bad = Audit(verdicts={i: Verdict("FILLER", "", "") for i in range(len(units))})
    out, _ = prune(units, bad, TERMS)
    assert "`make test`" in out and "API_TOKEN" in out and "name: demo" in out and "# Demo" in out


def test_keep_filler_keeps_text_but_reports_it():
    units = segment(MD)
    out, rows = prune(units, verdicts_for(units), TERMS, keep_filler=True)
    assert "really important" in out
    assert any(r["label"] == "FILLER" and r["saved"] == 0 for r in rows)
    assert BY["adversarial review"].replace in out
