"""Build the pruned file and the reports. Nothing here calls a model."""

from __future__ import annotations

import difflib

from .classify import Audit
from .lexicon import Term
from .segment import Unit, approx_tokens, join


def prune(units: list[Unit], audit: Audit, terms: list[Term], keep_filler: bool = False) -> tuple[str, list[dict]]:
    """Return (pruned_markdown, rows). Rows describe every touchable unit.

    keep_filler: report FILLER verdicts but keep the text. Measured on a
    Chinese methodology skill, FILLER deletions removed the rule list users
    ask about by name and the pruned skill lost 4 of 5 ablation tasks; the
    METHOD replacements alone held. Deleting is the risky half."""
    by_name = {t.name: t for t in terms}
    out: list[str] = []
    rows: list[dict] = []
    last_replacement = None
    for i, u in enumerate(units):
        v = audit.verdicts.get(i)
        if not u.touchable or v is None or v.label in ("FACT", "UNSURE", "CANDIDATE"):
            out.append(u.text)
            if u.touchable:
                rows.append(_row(i, u, v.label if v else "FACT", "", v.why if v else "", 0))
            if u.kind not in ("blank",):
                last_replacement = None
            continue
        if v.label == "FILLER":
            if keep_filler:
                out.append(u.text)
                rows.append(_row(i, u, "FILLER", "", v.why + " (kept: --keep-filler)", 0))
                last_replacement = None
            else:
                rows.append(_row(i, u, "FILLER", "", v.why, approx_tokens(u.body)))
            continue
        # METHOD
        line = " ".join(by_name[t].replace for t in v.terms)
        saved = approx_tokens(u.body) - approx_tokens(line)
        if last_replacement == line:
            # consecutive units re-explaining the same term collapse into one line
            rows.append(_row(i, u, "METHOD", v.term, v.why + " (merged with previous)", approx_tokens(u.body)))
            continue
        out.append(u.prefix + line)
        last_replacement = line
        rows.append(_row(i, u, "METHOD", v.term, v.why, saved))
    text = "\n".join(out)
    # collapse runs of blank lines left behind by deletions
    while "\n\n\n" in text:
        text = text.replace("\n\n\n", "\n\n")
    return text.rstrip("\n") + "\n", rows


def _row(i: int, u: Unit, label: str, term: str, why: str, saved: int) -> dict:
    return {"id": i, "lines": f"{u.start}-{u.end}", "kind": u.kind, "label": label, "term": term,
            "tokens": approx_tokens(u.body), "saved": max(saved, 0), "why": why, "text": u.body}


def diff(original: str, pruned: str, name: str) -> str:
    return "".join(difflib.unified_diff(original.splitlines(True), pruned.splitlines(True),
                                        fromfile=f"{name} (original)", tofile=f"{name} (pruned)"))


def report(name: str, units: list[Unit], rows: list[dict], audit: Audit, original: str, pruned: str,
           cost: float, calls: int, driver: str) -> str:
    before, after = approx_tokens(original), approx_tokens(pruned)
    touch = [u for u in units if u.touchable]
    guarded = [u for u in units if u.kind in ("paragraph", "list") and not u.touchable]
    counts = {k: sum(1 for r in rows if r["label"] == k) for k in ("FACT", "METHOD", "FILLER", "UNSURE", "CANDIDATE")}
    pct = (100 * (before - after) / before) if before else 0
    lines = [
        f"# onenoun audit — {name}",
        "",
        f"approx tokens: **{before} → {after}** ({pct:+.0f}%)  ·  units: {len(units)} total, {len(touch)} touchable, "
        f"{len(guarded)} guarded  ·  labels: " + ", ".join(f"{k} {v}" for k, v in counts.items()),
        f"driver: {driver}, {calls} call(s), ${cost:.3f}",
        "",
        "| # | lines | label | term | tokens | saved | why |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        why = r["why"].replace("|", "\\|").replace("\n", " ")
        lines.append(f"| {r['id']} | {r['lines']} | {r['label']} | {r['term']} | {r['tokens']} | {r['saved'] or ''} | {why} |")
    if guarded:
        lines += ["", "## Guarded (never sent to the model)", ""]
        for u in guarded:
            lines.append(f"- lines {u.start}-{u.end} · {u.guard} · {u.body.splitlines()[0][:90]}")
    lines += ["", "## The model's own uncertainties (列出所有不自信的点)", ""]
    lines += [f"- {x}" for x in audit.uncertainties] or ["- (none reported)"]
    return "\n".join(lines) + "\n"
