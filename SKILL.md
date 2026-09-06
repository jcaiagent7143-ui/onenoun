---
name: onenoun
description: Audit or prune an agent skill file (SKILL.md, CLAUDE.md, AGENTS.md, rules) by replacing prose that re-explains a methodology the model already knows with the one term that activates it, then prove by ablation that the skill did not get worse. Use when the user asks to shorten, prune, distill, audit, or "onenoun" a skill, or says a skill is too long.
---

# onenoun — 一个名词，激活一整套原理

The model was trained on "first principles", "ablation", "Occam's razor",
"adversarial review" and a few dozen more. A skill that re-explains one of them
in three paragraphs is paying tokens for nothing. The noun alone activates the
method. But a paragraph that carries a fact the model could not know (a path, a
command, a measured number, a decision the author made) must stay verbatim.

## When the CLI is available

Run it. It uses `claude -p` as the model, so it works wherever this session
works, and it never overwrites the input.

```sh
uvx onenoun audit  <path-to-skill-or-dir>          # report only
uvx onenoun prune  <path-to-skill-or-dir> -o out/  # writes out/<name>.pruned.md, .diff.md, .report.md
uvx onenoun ablate <original> out/<name>.pruned.md -k 5   # blind A/B judge; exit 2 if pruned lost any task
```

Show the user the report table and the diff. Do not replace the original
unless they ask, and not before `ablate` reports that pruned lost 0 tasks.

## When the CLI is not available

Do the same three passes by hand, in this order, and say which pass you are in.

1. **Segment.** Mark every unit that may not be touched: frontmatter, code
   fences, tables, headings, and any line containing a backtick span, a path,
   a URL, an env var, a CLI flag, a number with a unit, a version, or an
   @mention. Those are copied verbatim, whatever you think of them.
2. **Classify** each remaining paragraph or list item as one of
   FACT (project-specific, keep), METHOD (its entire content re-explains a
   named method; replace with the name), FILLER (restated elsewhere in the
   file, or changes no behaviour; delete), UNSURE (keep, and say why). When in
   doubt, FACT. Then list every point you are not confident about.

   The list below is a starting set, not a limit. Name any established method
   the file re-explains, from any field — if the file is about market entry,
   that may be Porter's five forces or RICE scoring. For a term that is not on
   the list, first write a question that names only that term, answer it in a
   separate step without looking at the file, and check that the answer really
   contains the method. If it does not, leave the prose alone.
3. **Ablate.** Write three realistic tasks from the skill's description.
   Answer each with the original and with the pruned version. Judge blind.
   If the pruned version loses any, say so and do not recommend it.

Replacement lines, one per term (the full lexicon with Chinese names and
activation tests is in `onenoun/lexicon.md`):

first principles → "Reason from first principles." · adversarial review → "Run an adversarial review of the result." · ablation → "Ablate: remove one component at a time and measure." · Occam's razor → "Apply Occam's razor." · list every uncertainty → "List every uncertainty before concluding." · independent thinking → "Think independently; do not defer to the premise." · critical thinking → "Apply critical thinking." · high cohesion, low coupling → "Design for high cohesion, low coupling." · steelman → "Steelman the opposing view first." · pre-registration → "Pre-register the success criteria before looking at results." · root cause → "Fix the root cause, not the symptom." · single-variable change → "Change one variable at a time." · out-of-sample validation → "Validate out of sample." · five whys → "Ask the five whys." · inversion → "Invert: ask what would guarantee failure." · red team → "Red-team it." · postmortem → "Write a blameless postmortem." · principle of least astonishment → "Follow the principle of least astonishment." · separation of concerns → "Keep separation of concerns." · idempotence → "Make it idempotent." · fail fast → "Fail fast with a clear message." · defense in depth → "Apply defense in depth." · YAGNI → "YAGNI." · DRY → "DRY." · rubber duck debugging → "Rubber-duck it." · Chesterton's fence → "Check Chesterton's fence before removing." · base rates → "Start from the base rate." · falsifiability → "State what would falsify the claim." · MECE → "Make the breakdown MECE." · Pareto → "Pareto: find the 20% that gives 80%."

Do not invent a term that is not on this list. If the prose does not map to
one of these, it is FACT or UNSURE.
