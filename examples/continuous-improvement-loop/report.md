# onenoun audit — ~/.claude/skills/continuous-improvement-loop/SKILL.md

approx tokens: **1503 → 1371** (+9%)  ·  units: 63 total, 33 touchable, 2 guarded  ·  labels: FACT 26, METHOD 5, FILLER 2, UNSURE 0
driver: claude, 1 call(s), $0.493

| # | lines | label | term | tokens | saved | why |
|---|---|---|---|---|---|---|
| 4 | 18-18 | FILLER |  | 20 | 20 | Restates the tagline already given in the YAML description ('evolving any system after it ships... evaluate against REAL execution'); adds no new instruction. |
| 8 | 22-26 | FACT |  | 100 |  | Defines the skill's own core concept ('the eval gate') and the specific list of real-world failure modes mocks miss (rate/connection limits, auth, quotas, latency, schema drift, costs) — not a lexicon term itself, it's the file's central thesis. |
| 12 | 30-32 | FACT |  | 66 |  | Concrete war story with specific technical details (mock-socket test, reconnect storm, 1-connection limit, socket leak) — must stay verbatim. |
| 13 | 33-35 | FACT |  | 48 |  | Concrete war story with specific numbers (t≈5 in-sample, negative median, sub-50% win rate) — must stay verbatim. |
| 17 | 39-39 | FACT |  | 17 |  | Specific workflow step of this skill's loop; ties to the project-specific 'real target' emphasis and cross-references Safety section, not a pure lexicon restatement. |
| 18 | 40-41 | FACT |  | 40 |  | Specific instruction naming concrete observability signals and the 'steady state vs clean startup' distinction — not a lexicon term. |
| 19 | 42-43 | FACT |  | 42 |  | Mixes pre-registration and out-of-sample-validation language with the skill's own 'real signal' emphasis and the added nuance that null/negative results are valid — the 'real' framing is project-specific per the mixing rule. |
| 20 | 44-44 | METHOD | root cause | 23 | 14 | Entire content is a plain restatement of root-cause analysis (find the mechanism, don't patch the symptom) with no project-specific detail. |
| 21 | 45-46 | FACT |  | 28 |  | Specific instruction to add a regression test AND re-run the exact real eval that exposed the issue — a concrete workflow rule beyond any single lexicon term. |
| 22 | 47-48 | FACT |  | 26 |  | Specific verification step ('anomaly gone in real behavior, not just in tests') tied to the skill's real-vs-mock thesis. |
| 23 | 49-50 | FACT |  | 34 |  | Defines a specific note template/naming convention (symptom → root cause → fix → guard added) — a concrete structural decision, not just the generic postmortem idea. |
| 27 | 54-56 | FACT |  | 54 |  | Concrete, specific instruction (reuse real components, swap only the side-effect at the edge, keep ingest→parse→decide→gates real) with named examples like paper/dry-run executor. |
| 28 | 57-57 | FACT |  | 21 |  | Specific empirical claim ('synthetic data hides distribution problems') and instruction to match real scale/shape. |
| 29 | 58-60 | METHOD | out-of-sample validation | 49 | 44 | Entire content is a textbook explanation of out-of-sample validation (train/test split, judge once, in-sample number isn't evidence) with no project-specific detail. |
| 30 | 61-62 | FACT |  | 28 |  | Domain-specific trading terminology (fees, slippage, thin edge) — concrete and specific to a financial/trading domain. |
| 31 | 63-64 | METHOD | pre-registration | 33 | 18 | Entire content is a restatement of pre-registration (decide bar/sample size/metric before seeing results, prevents goalpost-moving). |
| 35 | 68-68 | FILLER |  | 16 | 16 | Restates the mock-vs-real point already made in unit 8, just relabeled as an anti-pattern; 'fake-eval-only' isn't a lexicon term so can't be METHOD. |
| 36 | 69-69 | METHOD | out-of-sample validation | 16 | 11 | Pure restatement of out-of-sample validation as its negation (judging on data you tuned on), duplicative of unit 29 but still a clean method re-explanation. |
| 37 | 70-70 | METHOD | root cause | 15 | 6 | Pure restatement of root-cause analysis as its negation (fixing the log line, not the mechanism), duplicative of unit 20 but still a clean method re-explanation. |
| 38 | 71-73 | FACT |  | 58 |  | Contains a specific prescribed phrase/policy ('not validated — stop,' say so plainly) beyond generic pre-registration/goalpost-moving concepts. |
| 39 | 74-75 | FACT |  | 39 |  | Specific, concrete rule ('log what was dropped') with no matching lexicon term. |
| 40 | 76-77 | FACT |  | 25 |  | Specific safety anti-pattern naming irreversible/real-money/destructive actions — concrete constraint, not a lexicon term. |
| 44 | 81-82 | FACT |  | 30 |  | Concrete, specific safety procedure (separate state/dirs, sandbox/paper mode, no irreversible writes) — not a lexicon term. |
| 45 | 83-84 | FACT |  | 32 |  | Concrete, specific safety procedure (verify primary system idle before/after) — not a lexicon term. |
| 46 | 85-86 | FACT |  | 39 |  | Specific gating policy naming real money/prod cutover/mass action and requiring 'explicit owner approval' — a concrete decision beyond generic method terms. |
| 50 | 90-92 | FACT |  | 54 |  | Defines a specific note template (observed, root cause, fix, guard added, honest verdict + limitations) and names the mechanism ('project's persistent memory/learnings store') — a concrete structural decision, not just generic postmortem. |
| 51 | 93-94 | FACT |  | 40 |  | Second sentence ('verify any file/flag/symbol a past note cites still exists') is a specific, non-generic instruction; per the mixing rule this makes the whole unit FACT even though the first sentence echoes postmortem's 're-read before next cycle'. |
| 57 | 100-100 | FACT |  | 14 |  | Defines a specific role in this skill's own portability framework with concrete examples (server/container/staging/sandbox) — a naming convention the author created. |
| 58 | 101-101 | FACT |  | 17 |  | Defines a specific role with concrete examples (production feed, historical dataset, live API) in the skill's portability framework. |
| 59 | 102-102 | FACT |  | 18 |  | Defines a specific role with concrete examples (logs, metrics, dashboards, health endpoints) in the skill's portability framework. |
| 60 | 103-104 | FACT |  | 36 |  | Defines a specific role with concrete examples (broker, mailer, writer, deployer) in the skill's portability framework. |
| 61 | 105-105 | FACT |  | 20 |  | Names a specific role ('Validation gate') in the skill's own framework, even though its content leans on pre-registration/out-of-sample concepts. |
| 62 | 106-106 | FACT |  | 16 |  | Defines a specific role ('Learnings store') in the skill's portability framework. |

## Guarded (never sent to the model)

- lines 28-28 · lead_in · Two failure classes this catches that mocks never will (real cases — keep them in mind):
- lines 98-98 · lead_in · This loop is project-agnostic. Before starting, identify the project's instances of these 

## The model's own uncertainties (列出所有不自信的点)

- Units 17, 18, 19, 21, 22: I classified these as FACT mainly because they repeatedly emphasize 'real' (the file's core thesis, not itself a lexicon term). One could argue some of these are still substantially just pre-registration/out-of-sample restatements with 'real' as flavor text, which would push them toward METHOD instead.
- Units 38 and 46: I called these FACT for a single specific phrase each ('not validated — stop, say so plainly'; 'explicit owner approval'), but the bulk of their content is pre-registration/out-of-sample language — a stricter reading could call these METHOD.
- Unit 61 ('Validation gate — the pre-committed pass/fail metric (+ out-of-sample split)') is borderline: it's almost pure pre-registration + out-of-sample-validation restatement, and only the role label 'Validation gate' is skill-specific, so METHOD is a plausible alternative.
- Units 23 and 50: I judged their specific field templates (symptom→root cause→fix→guard added; observed/root cause/fix/guard/verdict+limitations) as project-specific decisions rather than generic postmortem, but a stricter reader might see these as natural instantiations of the postmortem method and label them METHOD instead.
- Units 36 and 37 are near-verbatim duplicates of units 29/20 respectively (just phrased as anti-patterns) — I labeled them METHOD rather than FILLER since they map cleanly to lexicon terms, but they could equally be argued as FILLER for repeating content already stated earlier in the file.
