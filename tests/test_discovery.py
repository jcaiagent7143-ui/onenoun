"""The vocabulary is open: the classifier may name any established method it
finds in the customer's own text, and the activation test decides whether the
model actually knows it. These tests cover that path without a model call."""

import pathlib

from onenoun.lexicon import Term, append, format_expect, load, parse_expect, validate


def test_parse_and_format_expect_round_trip():
    groups = parse_expect("remove|disable, baseline, one at a time")
    assert groups == [["remove", "disable"], ["baseline"], ["one at a time"]]
    assert parse_expect(["remove|disable", "baseline"]) == [["remove", "disable"], ["baseline"]]
    assert format_expect(groups) == "remove|disable, baseline, one at a time"


def test_a_verified_term_is_appended_and_reloads(tmp_path: pathlib.Path):
    local = tmp_path / "onenoun-lexicon.md"
    t = Term(name="Conway's Law", zh="康威定律", replace="Remember Conway's Law here.",
             subsumes="a system mirrors the communication structure of the team that built it",
             test="What is Conway's Law and how does it apply when reviewing an architecture?",
             expect=parse_expect("communication|organi, structure|architecture|design, team|group|org"))
    append(t, local)
    merged = load(extra=local)
    names = [x.name for x in merged]
    assert "Conway's Law" in names
    assert len(names) == len(set(names)), "no duplicates after merge"
    assert validate(merged) == []


def test_local_term_overrides_a_bundled_one(tmp_path: pathlib.Path):
    local = tmp_path / "onenoun-lexicon.md"
    append(Term(name="ablation", zh="消融实验", replace="Ablate it.", subsumes="x",
                test="What is ablation?", expect=parse_expect("a, b, c")), local)
    by = {t.name: t for t in load(extra=local)}
    assert by["ablation"].replace == "Ablate it."


def test_activation_test_rejects_a_term_the_model_cannot_expand():
    t = Term(name="made-up method", expect=parse_expect("remove, baseline, one at a time"))
    assert t.check_answer("I am not familiar with that term.") == ["remove", "baseline", "one at a time"]
