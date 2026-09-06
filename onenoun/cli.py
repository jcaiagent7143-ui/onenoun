"""onenoun — one noun activates a whole method.

    onenoun audit   <skill.md | dir>            classify + report, changes nothing
    onenoun prune   <skill.md | dir> -o out/    write pruned copy, diff, report
    onenoun ablate  <original> <pruned> -k 5    blind pairwise judge, prove it
    onenoun lexicon check                       prove every noun is in the model
    onenoun segment <skill.md>                  show the guards, no model call
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys

from . import __version__, ablate as ab, classify as cl, lexicon as lx, prune as pr
from .drivers import Driver, DriverError, make_driver
from .segment import approx_tokens, segment, summary

SKILL_NAMES = ("SKILL.md", "CLAUDE.md", "AGENTS.md", ".cursorrules")


def find_skills(target: pathlib.Path) -> list[pathlib.Path]:
    if target.is_file():
        return [target]
    found = sorted(p for p in target.rglob("*.md") if p.name in SKILL_NAMES or p.parent.name in ("rules", "commands"))
    if not found:
        found = sorted(target.rglob("*.md"))
    return [p for p in found if ".onenoun" not in p.parts and not p.name.endswith((".pruned.md", ".diff.md", ".report.md"))]


def say(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def cmd_segment(a) -> int:
    md = pathlib.Path(a.path).read_text(encoding="utf-8")
    units = segment(md)
    for i, u in enumerate(units):
        if u.kind == "blank":
            continue
        tag = "TOUCH" if u.touchable else f"keep:{u.guard}"
        print(f"[{i:3d}] L{u.start}-{u.end:<4} {u.kind:<11} {tag:<16} {u.body.splitlines()[0][:80]!r}")
    print(summary(units), file=sys.stderr)
    return 0


def _audit_one(path: pathlib.Path, terms, driver: Driver, out_dir: pathlib.Path | None, write: bool,
               keep_filler: bool = False, reuse: bool = False, no_discover: bool = False,
               local: pathlib.Path = pathlib.Path("onenoun-lexicon.md")) -> dict:
    md = path.read_text(encoding="utf-8")
    units = segment(md)
    name = path.parent.name if path.name == "SKILL.md" else path.stem
    dest = out_dir or (path.parent / ".onenoun")
    dest.mkdir(parents=True, exist_ok=True)
    audit_path = dest / f"{name}.audit.json"
    c0, n0 = Driver.total_cost, Driver.calls
    if reuse and audit_path.exists():
        saved = json.loads(audit_path.read_text(encoding="utf-8"))
        if saved.get("source_sha") != _sha(md):
            say(f"  {audit_path.name} was made from a different version of the file; re-classifying")
            audit = cl.classify(units, terms, driver, md)
        else:
            audit = cl.Audit(verdicts={int(k): cl.Verdict(**v) for k, v in saved["verdicts"].items()},
                             uncertainties=saved.get("uncertainties", []))
            say(f"  verdicts reused from {audit_path.name}")
    else:
        audit = cl.classify(units, terms, driver, md)
    if audit.proposals and not no_discover:
        say(f"  {len(audit.proposals)} new term(s) proposed: " + ", ".join(t.name for t in audit.proposals))
        passed, results = lx.verify(audit.proposals, driver)
        for t, missing, _ in results:
            say(f"    {'verified' if not missing else 'rejected'}  {t.name}" + ("" if not missing else f"  (missing {missing})"))
        for t in passed:
            lx.append(t, local)
        if passed:
            terms = terms + passed
            names = {t.name for t in passed}
            for i, v in audit.verdicts.items():
                if v.label == "CANDIDATE" and set(v.terms) <= names:
                    v.label, v.why = "METHOD", v.why.replace("not yet verified", "verified by activation test")
    audit_path.write_text(json.dumps({"source_sha": _sha(md), "driver": driver.name,
                                      "verdicts": {k: vars(v) for k, v in audit.verdicts.items()},
                                      "uncertainties": audit.uncertainties}, ensure_ascii=False, indent=1), encoding="utf-8")
    pruned, rows = pr.prune(units, audit, terms, keep_filler=keep_filler)
    rep = pr.report(str(path), units, rows, audit, md, pruned, Driver.total_cost - c0, Driver.calls - n0, driver.name)
    (dest / f"{name}.report.md").write_text(rep, encoding="utf-8")
    if write:
        (dest / f"{name}.pruned.md").write_text(pruned, encoding="utf-8")
        (dest / f"{name}.diff.md").write_text(pr.diff(md, pruned, name), encoding="utf-8")
    before, after = approx_tokens(md), approx_tokens(pruned)
    counts = {k: sum(1 for r in rows if r["label"] == k) for k in ("FACT", "METHOD", "FILLER", "UNSURE", "CANDIDATE")}
    return {"path": path, "name": name, "before": before, "after": after, "counts": counts, "dest": dest,
            "uncertainties": len(audit.uncertainties)}


def _sha(text: str) -> str:
    import hashlib
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def cmd_audit(a, write: bool) -> int:
    local = pathlib.Path(a.local_lexicon)
    terms = lx.load(pathlib.Path(a.lexicon) if a.lexicon else None, extra=local)
    driver = make_driver(a.driver, a.model)
    out_dir = pathlib.Path(a.out) if a.out else None
    paths = find_skills(pathlib.Path(a.path))
    if not paths:
        say(f"no skill files under {a.path}")
        return 1
    print(f"{'skill':<34} {'tokens':>14} {'FACT':>5} {'METHOD':>6} {'FILLER':>6} {'UNSURE':>6} {'CAND':>5}")
    for p in paths:
        say(f"· {p}")
        r = _audit_one(p, terms, driver, out_dir, write, keep_filler=a.keep_filler, reuse=a.reuse,
                       no_discover=a.no_discover, local=local)
        pct = 100 * (r["after"] - r["before"]) / r["before"] if r["before"] else 0
        c = r["counts"]
        print(f"{r['name'][:34]:<34} {r['before']:>5} → {r['after']:>5} {pct:+4.0f}% {c['FACT']:>5} {c['METHOD']:>6} {c['FILLER']:>6} {c['UNSURE']:>6} {c['CANDIDATE']:>5}")
        say(f"  report: {r['dest'] / (r['name'] + '.report.md')}" + (f"  pruned: {r['dest'] / (r['name'] + '.pruned.md')}" if write else ""))
    say(f"{Driver.calls} model call(s), ${Driver.total_cost:.3f}")
    if write:
        say("The pruned file is a proposal. Run `onenoun ablate <original> <pruned>` before you adopt it.")
    return 0


def cmd_ablate(a) -> int:
    o, p = pathlib.Path(a.original), pathlib.Path(a.pruned)
    original, pruned = o.read_text(encoding="utf-8"), p.read_text(encoding="utf-8")
    driver = make_driver(a.driver, a.model)
    tasks = [l.strip() for l in pathlib.Path(a.tasks).read_text().splitlines() if l.strip()] if a.tasks else None
    trials = ab.run(original, pruned, a.k, driver, seed=a.seed, tasks=tasks, progress=say)
    rep = ab.report(o.name, trials, approx_tokens(original), approx_tokens(pruned), Driver.total_cost, Driver.calls, driver.name)
    dest = pathlib.Path(a.out) if a.out else p.parent / (p.stem.replace(".pruned", "") + ".ablate.md")
    dest.write_text(rep, encoding="utf-8")
    print(rep.split("\n\n")[1])
    say(f"report: {dest}")
    return 0 if not any(t.winner == "original" for t in trials) else 2


def cmd_lexicon(a) -> int:
    terms = lx.load(pathlib.Path(a.lexicon) if a.lexicon else None, extra=pathlib.Path(a.local_lexicon))
    problems = lx.validate(terms)
    for pb in problems:
        print(f"shape: {pb}")
    if a.sub != "check":
        print(f"{len(terms)} terms, {'shape ok' if not problems else f'{len(problems)} problem(s)'}")
        return 1 if problems else 0
    driver = make_driver(a.driver, a.model)
    if a.only:
        terms = [t for t in terms if t.name in a.only]
    fails = 0
    for t, missing, answer in lx.check(terms, driver):
        ok = not missing
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {t.name:<34} " + ("" if ok else f"missing: {missing}"))
        if not ok and a.verbose:
            print("      " + answer.replace("\n", "\n      ")[:1200])
    say(f"{len(terms) - fails}/{len(terms)} pass · {Driver.calls} call(s), ${Driver.total_cost:.2f}")
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="onenoun", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--version", action="version", version=f"onenoun {__version__}")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--driver", default="claude", help="claude (default) or shell:<command with {prompt}>")
    common.add_argument("--model", default="sonnet", help="model name passed to the claude driver (default: sonnet)")
    common.add_argument("--lexicon", help="path to a lexicon.md (default: the bundled one)")
    common.add_argument("--local-lexicon", default="onenoun-lexicon.md",
                        help="file where verified new terms are stored and reloaded (default: ./onenoun-lexicon.md)")
    common.add_argument("--no-discover", action="store_true",
                        help="use only the terms already in the lexicon; do not propose or verify new ones")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("segment", help="show units and guards; no model call")
    s.add_argument("path")
    for name, help_ in (("audit", "classify and report; changes nothing"), ("prune", "write pruned copy + diff + report")):
        s = sub.add_parser(name, parents=[common], help=help_)
        s.add_argument("path")
        s.add_argument("-o", "--out", help="output directory (default: .onenoun/ next to each file)")
        s.add_argument("--keep-filler", action="store_true",
                       help="replace METHOD units but keep FILLER units (report them only); the safer mode")
        s.add_argument("--reuse", action="store_true",
                       help="reuse <name>.audit.json from a previous run instead of calling the model again")
    s = sub.add_parser("ablate", parents=[common], help="blind pairwise judge: original vs pruned")
    s.add_argument("original")
    s.add_argument("pruned")
    s.add_argument("-k", type=int, default=5, help="number of tasks (default 5)")
    s.add_argument("--tasks", help="file with one task per line instead of generated tasks")
    s.add_argument("--seed", type=int, default=0)
    s.add_argument("-o", "--out", help="report path (default: <name>.ablate.md next to the pruned file)")
    s = sub.add_parser("lexicon", parents=[common], help="validate the lexicon; `check` runs activation tests")
    s.add_argument("sub", nargs="?", default="validate", choices=["validate", "check"])
    s.add_argument("--only", nargs="*", help="check only these terms")
    s.add_argument("-v", "--verbose", action="store_true")

    a = ap.parse_args(argv)
    try:
        if a.cmd == "segment":
            return cmd_segment(a)
        if a.cmd == "audit":
            return cmd_audit(a, write=False)
        if a.cmd == "prune":
            return cmd_audit(a, write=True)
        if a.cmd == "ablate":
            return cmd_ablate(a)
        if a.cmd == "lexicon":
            return cmd_lexicon(a)
    except DriverError as e:
        say(f"error: {e}")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
