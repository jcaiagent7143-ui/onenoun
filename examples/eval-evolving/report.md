# onenoun audit — ~/.claude/skills/eval-evolving/SKILL.md

approx tokens: **1137 → 931** (+18%)  ·  units: 65 total, 21 touchable, 16 guarded  ·  labels: FACT 9, METHOD 2, FILLER 10, UNSURE 0
driver: claude, 1 call(s), $0.219

| # | lines | label | term | tokens | saved | why |
|---|---|---|---|---|---|---|
| 11 | 23-23 | FILLER |  | 33 | 33 | Restates the inner-loop/outer-loop description already given in the bullet points immediately above it, just as an arrow-flow diagram; no new project-specific content. |
| 15 | 27-27 | FILLER |  | 25 | 25 | Restates the top-of-file iron rule 'eval 必须基于真实运行(不是 mock/假测试)' almost verbatim as step 1 of the inner loop. |
| 18 | 30-30 | FACT |  | 7 |  | Specifies a concrete field name in this project's log.md template — a naming convention not derivable from general knowledge. |
| 20 | 32-32 | FACT |  | 11 |  | Specifies a concrete field name/content in the log.md template, first appearance of this structure. |
| 21 | 33-33 | FACT |  | 21 |  | Enumerates specific categories (errors, cost, rate limits, bottlenecks) that must go in this field — project-specific template detail. |
| 22 | 34-34 | FACT |  | 10 |  | Specifies a concrete log field format (success/partial/failure + one-line root cause); the field structure itself is project-specific even though 'root cause' is a lexicon term. |
| 23 | 35-35 | FACT |  | 19 |  | States a specific rule of this framework (log failures/negatives too, or it's self-deception) not previously stated and not a lexicon term re-explanation. |
| 31 | 50-50 | FACT |  | 23 |  | Describes a specific procedure (cluster feedback, rank by frequency × impact) combining clustering with prioritization; not a clean single-term lexicon re-explanation. |
| 32 | 51-51 | FACT |  | 26 |  | Lists specific selection criteria (root cause clear, change feasible, benefit clear) unique to this framework's decision process. |
| 33 | 52-52 | FACT |  | 23 |  | Enumerates the specific categories of change this framework allows (code/params/prompt/guardrails) — project-specific scope definition. |
| 35 | 55-55 | FACT |  | 29 |  | Gives the first detailed operational description of the verification step (check subsequent log records, keep/rollback/iterate) — more specific than the later restated iron law. |
| 44 | 70-70 | FILLER |  | 27 | 27 | Restates the top-of-file iron rule about verification, already covered in more detail by unit 35 and the initial 铁律 statement. |
| 48 | 74-74 | FILLER |  | 12 | 12 | Restates unit 23's rule (log failures/empty results too) as its negation in the anti-pattern list. |
| 49 | 75-75 | FILLER |  | 12 | 12 | Restates the top iron rule and unit 15 about not using mock/fake tests as eval. |
| 51 | 77-77 | FILLER |  | 9 | 9 | Restates the requirement (already stated as iron rule and outer-loop steps 5-6) that changes must be fed back and verified. |
| 52 | 78-78 | METHOD | pre-registration; root cause | 21 |  | Warns against repeatedly trying changes until one looks good or moving the judgment criteria after seeing results (violates pre-registration), and prescribes clarifying root cause before changing; no project-specific detail remains beyond these two concepts. |
| 54 | 80-80 | METHOD | single-variable change | 18 | 11 | States exactly the single-variable-change principle: don't change all feedback at once, change one verifiable thing at a time, for attribution. |
| 60 | 86-86 | FILLER |  | 12 | 12 | Restates the already-described concept of a trigger entry point that does the real work, just under a new abstract role label. |
| 61 | 87-87 | FILLER |  | 23 | 23 | Restates the already-stated 'real system/real data' requirement from the top iron rule and inner-loop step 1, relabeled as a portability role. |
| 63 | 89-89 | FILLER |  | 16 | 16 | Restates the outer-loop trigger condition already given in that section's heading ('攒够 N 条 / 定期触发'). |
| 64 | 90-90 | FILLER |  | 17 | 17 | Restates the change-injection categories already listed in unit 33 (code/params/prompt/guardrails), relabeled as a portability role. |

## Guarded (never sent to the model)

- lines 13-14 · backtick · 把"持续改进"做成一个**闭环**:内循环边干边评估、按时间记账;外循环读账、找改进、回流。
- lines 18-19 · backtick · **内循环 = 干活即评估(eval)**:每次被触发就**真实地**跑一遍任务(真实系统、真实数据、真实输出),
- lines 20-21 · backtick · **外循环 = 自我进化(self-evolving)**:定期(或攒够 N 条)**扫描 `log.md`** 的全部记录与反馈,
- lines 28-28 · backtick · **立刻**把这次运行追加进 `log.md`,一条记录至少含:
- lines 29-29 · backtick · 时间戳(ISO,如 `2026-06-21T14:30:00Z`)
- lines 31-31 · short · 动作(实际做了什么)
- lines 37-37 · backtick · `log.md` 记录模板:
- lines 49-49 · backtick · **扫描** `log.md` 的历史记录(按时间)。
- lines 53-54 · backtick · **回流(闭环)**:应用改动,并在 `log.md` 写一条「进化记录」(改了什么、为什么、预期效果、时间戳),
- lines 57-57 · short · 「进化记录」模板:
- lines 68-68 · backtick · **eval 基于真实**:评估来自真实运行的 `log.md`,不是 mock、不是凭感觉。
- lines 69-69 · backtick · **进化要有证据**:每条改进都能在 `log.md` 里指到具体反馈,不是拍脑袋。
- lines 76-76 · backtick · 外循环不看 `log.md`、凭感觉乱改 → 不是数据驱动。
- lines 79-79 · backtick · `log.md` 不带时间戳 / 不可追溯 → 外循环没法按时间分析。
- lines 84-84 · lead_in · 开工前先把抽象角色映射到你的项目:
- lines 88-88 · backtick · **`log.md`(进化日志)** — 每次运行 + 每条进化的时间戳账本,内外循环都读它。

## The model's own uncertainties (列出所有不自信的点)

- Units 11 and 15 are duplicate in content but also function as enumerated steps in the actual procedure (inner-loop step 1, and the closed-loop summary); whether removing them breaks the step-by-step readability versus being pure token waste is a judgment call.
- Unit 52's mapping to 'pre-registration' is analogical rather than exact — pre-registration is about fixing criteria before seeing results, while this unit describes retrying/moving goalposts after seeing results; I judged the anti-pattern warning as fully captured by that term plus 'root cause', but this is an interpretive stretch.
- Units 60/61/63/64 (the '通用化映射' role-mapping section) restate earlier content under new abstract labels for portability purposes; I labeled them FILLER since no new information is conveyed, but one could argue the act of naming reusable roles has independent value for a portable skill file, which would push them toward FACT instead.
- For unit 35 vs unit 44, I treated 35 as the original (more detailed) statement and 44 as the redundant restatement based on document order, but since 44 sits in a 'iron laws' section that could be read as the canonical/summary statement, the FACT/FILLER assignment between these two is somewhat arbitrary.
