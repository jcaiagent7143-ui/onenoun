"""The guards are the product: a unit carrying a fact must never be touchable."""

from onenoun.segment import join, segment

FACTS = [
    "Run `python3 scripts/validate.py` before shipping.",
    "The base URL is https://api-sg.example.com/ for Singapore accounts.",
    "Set BYTEPLUS_ARK_API_KEY in your shell before running anything at all.",
    "Pass --format json to get the structured output instead of the markdown one.",
    "A 17-image note takes about 119 s end to end on the hosted service.",
    "Write the result to ~/Desktop/out.mp4 and then open it in the player.",
    "Use model video-gen-2-0-260128 unless the user asks for another one.",
    "Mention @jakevin7 in the credit line of every post that quotes the slide.",
    "Call fetch_page() first and then parse the response with parse_html().",
    "The endpoint returns HTTP 412 for every Bilibili URL we have tried so far.",
    "Insert the Task 4 chart.png files throughout the deck using the DOCX skill.",
    "Revenue growth = (this quarter revenue minus the year-ago quarter) over the year-ago quarter",
    "Always include the number in the summary, so write $50B revenue and never large revenue.",
    "Name length must be 3-50 characters and start and end with an alphanumeric character.",
    "Distill each learning into the store as symptom → root cause → fix → guard added, one line.",
    "Exit multiple minus entry multiple × entry EBITDA over equity gives the multiple of money.",
]

GENERIC = [
    "Before accepting a conclusion, look for the strongest objection and try to break it yourself.",
    "Remove one component at a time and observe what changes, keeping everything else fixed.",
    "Prefer the simplest explanation that fits the evidence and do not add parts without necessity.",
]


def test_facts_are_guarded():
    for line in FACTS:
        (u,) = [x for x in segment(line + "\n") if x.kind == "paragraph"]
        assert not u.touchable, f"should be guarded: {line!r}"
        assert u.guard, line


def test_generic_prose_is_touchable():
    for line in GENERIC:
        (u,) = [x for x in segment(line + "\n") if x.kind == "paragraph"]
        assert u.touchable, line


def test_structure_is_never_touchable():
    md = "---\nname: x\ndescription: y\n---\n\n# Title\n\n```sh\necho hi\n```\n\n| a | b |\n|---|---|\n| 1 | 2 |\n\n<div>html</div>\n"
    for u in segment(md):
        assert not u.touchable, u


def test_short_and_lead_in_are_guarded():
    md = "Be careful.\n\nDo the following three things in order, exactly as written below:\n"
    kinds = {u.body: u.guard for u in segment(md) if u.kind == "paragraph"}
    assert kinds["Be careful."] == "short"
    assert kinds["Do the following three things in order, exactly as written below:"] == "lead_in"


def test_chinese_paragraph_counts_as_prose():
    md = "只记成功、不记失败或空结果，进化就没有燃料；每次运行都要把结果记下来。\n"
    (u,) = [x for x in segment(md) if x.kind == "paragraph"]
    assert u.touchable


def test_list_items_keep_prefix():
    md = "- **Ship** to a real target safely, and observe the real behaviour afterwards in the logs.\n  continuation line here\n- second item that is also long enough to be prose for the test\n"
    items = [u for u in segment(md) if u.kind == "list"]
    assert len(items) == 2
    assert items[0].prefix == "- "
    assert items[0].text.startswith("- **Ship**") and "continuation" in items[0].text


def test_round_trip_is_exact():
    md = "---\nname: a\n---\n\n# H\n\nPara one is long enough to be a paragraph for the segmenter here.\n\n- item one long enough to be a real list item for the test\n\n```\ncode\n```\n"
    assert join(segment(md)) == md
