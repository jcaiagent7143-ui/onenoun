from onenoun.lexicon import Term, load, validate


def test_bundled_lexicon_is_well_formed():
    terms = load()
    assert len(terms) >= 25
    assert validate(terms) == []


def test_replace_lines_are_one_line_and_short():
    for t in load():
        assert "\n" not in t.replace and len(t.replace.split()) <= 10, t.name


def test_check_answer_requires_every_group():
    t = Term("x", expect=[["remove", "disable"], ["baseline"], ["one at a time", "individually"]])
    assert t.check_answer("Remove each part individually and compare to the baseline.") == []
    assert t.check_answer("Remove each part and compare.") == ["baseline", "one at a time|individually"]


def test_degenerate_judgements_are_rejected():
    from onenoun.ablate import _degenerate

    good = {"reason": "Answer B names the held-out split and the pre-committed bar, which A omits entirely here.",
            "uncertainties": ["I cannot tell which instruction file produced which answer from the text alone."]}
    assert _degenerate(good) == ""
    assert _degenerate({"reason": "test", "uncertainties": ["a"]})
    assert _degenerate({"reason": good["reason"], "uncertainties": []})
    assert _degenerate({"reason": good["reason"], "uncertainties": ["a", "b"]})
