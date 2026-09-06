# onenoun

**一个名词，激活一整套原理 — one noun activates a whole method.**

Your agent skills re-explain things the model already knows. `onenoun` reads
your own skills, works out which named method each of those paragraphs is
re-explaining, checks that the model really knows that name, replaces the
paragraph with it, and then proves by blind ablation that the skill did not
get worse. It never touches a fact.

The vocabulary is not a fixed list. It starts from thirty terms and grows out
of whatever your files turn out to be re-explaining, in whatever field they
belong to.

[中文说明](README.zh-CN.md)

```sh
uvx onenoun audit  ~/.claude/skills          # report only, changes nothing
uvx onenoun prune  path/to/SKILL.md -o out/  # pruned copy + diff + report
uvx onenoun prune  path/to/SKILL.md -o out/ --keep-filler   # replace only, delete nothing
uvx onenoun ablate path/to/SKILL.md out/SKILL.pruned.md -k 5   # prove it
```

Needs [uv](https://docs.astral.sh/uv/) and the [Claude Code](https://claude.com/claude-code)
CLI signed in. The model work is done by `claude -p`, so there is no API key
to configure and nothing leaves your machine that does not already. About
$0.20 to audit a skill on Sonnet, about $2 to ablate one.

## Where the idea comes from

At Bilibili's *Build in Public*, Jakevin ([@jakevin7](https://x.com/jakevin7))
showed a *Builder Club* slide:

> **Skill 将死，方法论永生。** 一个名词，激活一整套原理：
> 第一性原理 · 对抗式审查 · 消融实验 · 奥卡姆剃刀 · 列出所有不自信的点 ·
> 保持独立思考 · 批判性思维 · 高内聚，低耦合

*Skills will die, methodology lives forever. One noun activates a whole set of
principles.* The model was trained on the entire literature of "first
principles" and "ablation". Say the word and it runs the procedure; the three
paragraphs you wrote explaining it cost tokens and add nothing. Simon (Simon聊AI落地)
[posted it on Douyin](https://www.douyin.com/note/7682301950289310693); that
post is where I saw it. Their idea, this tool.

The slide makes a claim that can be measured. So this repo measures it.

## What it measured

Three real skill files, first run, Sonnet, `onenoun prune`:

| skill | what it is | approx tokens | units replaced / deleted | pruned |
|---|---|---|---|---|
| [continuous-improvement-loop](examples/continuous-improvement-loop) | a pure methodology skill, no paths or commands at all | 1503 → 1371 | 5 METHOD, 2 FILLER | **−9%** |
| [eval-evolving](examples/eval-evolving) | the same skill written in Chinese | 1137 → 931 | 2 METHOD, 10 FILLER | **−18%** |
| [dcf-model](examples/dcf-model) (financial-analysis plugin) | 7,000-word modelling spec | 12377 → 10304 | 0 METHOD, 92 FILLER | **−17%** |

The slide is right about the words and wrong about the proportion. On the most
methodology-heavy skill on this machine, the one an inventory had guessed was
"about 95% generic", the model reclaimed 9–12% (two runs; the classifier is not
deterministic). What died was re-explanation: *"split by time or holdout, pick
parameters on the train split, judge once on the test split"* became
**"Validate out of sample."** What survived, correctly, was the author's own
decisions: the war stories with numbers, the seven-step loop, the rule that
says *"not validated — stop"*. Those are not in the model. They are the skill.

Run against wrapper skills that are nothing but endpoints, model ids and file
paths, the same command changes about one percent. That is the result to want:
the guards and the classifier together leave a file alone when there is
nothing in it the model already knows. The tool's value is telling the
difference per paragraph, not cutting every file it is pointed at.

**Did the pruned skill get worse?** `onenoun ablate` writes five tasks from
the skill's own description, answers each with the original and with the
pruned version loaded, and has a blind judge pick (A/B order randomised).

On the English methodology skill, five generated tasks, blind judge:

| skill | tokens | pruned won | tied | lost | verdict |
|---|---|---|---|---|---|
| [continuous-improvement-loop](examples/continuous-improvement-loop/ablate.md) | −9% | 3 | 0 | 2 | mixed |
| [eval-evolving](examples/eval-evolving/ablate.md) (Chinese, −18%) | −18% | 1 | 0 | 4 | **pruned is worse** |

Read the second row before you use this tool. On the Chinese skill the pruned
version lost four of five. The judge said why: the deletions took out the
anti-pattern list that users ask about by name, and the role-mapping list the
last task needed. The replacements were not the problem; the deletions were.

That is why deleting and replacing are separate switches. `--keep-filler`
replaces the methods and keeps every paragraph the classifier called a
duplicate, which is the half that carries the risk. On the English skill it
took the change from −9% to a smaller one, and on the Chinese skill from −18%
to −2%. Run `ablate` on your own file and believe that, not this table.

A side effect worth the price of the run: the classifier is told to list every
point it is not confident about (列出所有不自信的点). On the 7,000-word DCF
skill that list contained three internal contradictions the skill has shipped
with: a terminal-value threshold stated as 75% in one place and 80% in
another, a "blues and greys only" colour rule contradicted by a green/red rule
later, and a "fills only if requested" line against a "default fill palette"
line. The tool did not fix them. It said where they are.

## How it works

Three passes. The first has no model in it, on purpose.

1. **Segment.** The file is split into units. Frontmatter, headings, code
   fences, tables, and any paragraph containing a backtick span, a path, a
   URL, an env var, a CLI flag, a number with a unit, a version, or an
   @mention are marked untouchable and copied verbatim, whatever a model
   would say about them. So are formulas, ranges, currency amounts, one-line
   labels, and lines that introduce a code block. Across the 107 distinct
   skill files installed on one machine, this pass alone keeps 71% of all
   prose units away from the model, for nothing. `onenoun segment FILE` shows
   the verdicts and costs nothing to run.

```
$ onenoun segment ~/.claude/skills/continuous-improvement-loop/SKILL.md
[  0] L1-14   frontmatter keep:frontmatter '---'
[  2] L16-16   heading     keep:heading     '# Continuous-Improvement Loop'
[  4] L18-18   paragraph   TOUCH            'A loop for shipping, then *truthfully* learning...'
[  8] L22-26   paragraph   TOUCH            'Mock/unit tests prove the code does **what you think**...'
[ 10] L28-28   paragraph   keep:lead_in     'Two failure classes this catches that mocks never will...'
[ 12] L30-32   list        TOUCH            '**Green tests, broken in production.** A streaming...'
```

2. **Classify.** The touchable units go to the model with the whole file as
   context and the lexicon. Each comes back as **FACT** (project-specific,
   keep), **METHOD** with the lexicon terms it re-explains (replace with their
   one-line forms), **FILLER** (already said elsewhere in the file, or changes
   no behaviour; delete), or **UNSURE** (keep, and say why). The rule is
   *when in doubt, FACT*. A METHOD verdict naming a term that is not in the
   lexicon is downgraded to UNSURE. The replacement text comes from the
   lexicon, never from the model, so the output is reproducible and reviewable.
3. **Ablate.** Tasks from the description, two answers per task, a blind
   judge, the judge's own uncertainties in the report. Exit code 2 if the
   pruned skill lost any task. `prune` writes a proposal next to your file;
   nothing is overwritten.

## The lexicon grows from your own files

[`onenoun/lexicon.md`](onenoun/lexicon.md) ships 30 terms, but it is a seed,
not a limit. The classifier is told to name **any** established method your
file re-explains, from any field, whether or not it is listed. For each new
name it also writes the one-line replacement and an **activation test**: a
question naming only the term, and the keyword groups an answer must contain
to count as knowing it.

Every proposed term then has to pass its own test before it is allowed to
replace anything. A term the model cannot expand from its name alone is not a
term, whatever it is called. Verified terms are appended to
`./onenoun-lexicon.md` and reused on later runs; rejected ones leave the prose
exactly where it was, labelled CANDIDATE in the report.

Run on a market-entry review skill that had never met this tool
([examples/discovery](examples/discovery)):

```
$ onenoun prune market-entry-review.md -o out/
  6 new term(s) proposed: TAM/SAM/SOM, Porter's Five Forces, SWOT analysis,
                          RICE scoring, SMART goals, Conway's Law
    rejected  TAM/SAM/SOM  (missing ['market siz|opportunity siz'])
    verified  Porter's Five Forces
    verified  SWOT analysis
    verified  RICE scoring
    verified  SMART goals
    verified  Conway's Law
market-entry-review    452 → 203  -55%   FACT 2  METHOD 5  CAND 1
```

Five paragraphs of explanation became five names. The paragraph the gate could
not verify was left alone, and so were the two real facts: pull four fiscal
years, escalate above the mandate. Note that TAM/SAM/SOM is a term the model
plainly does know; its own generated test was too strict. The gate is
deliberately biased that way, because a false reject costs you nothing and a
false accept costs you a skill.

`--no-discover` turns discovery off and uses only the terms already known.
`onenoun lexicon check` re-runs every activation test, including the learned
ones. On the shipped 30, the first run passed 27; the three that failed
(adversarial review, red team, defense in depth) had correct answers and
too-narrow keyword lists, which were widened and re-run. That is the tool's
own pre-registration being adjusted after seeing the result, written here
rather than hidden. The starting set:

| term | 名词 | replaces the prose with |
|---|---|---|
| first principles | 第一性原理 | Reason from first principles. |
| adversarial review | 对抗式审查 | Run an adversarial review of the result. |
| ablation | 消融实验 | Ablate: remove one component at a time and measure. |
| Occam's razor | 奥卡姆剃刀 | Apply Occam's razor. |
| list every uncertainty | 列出所有不自信的点 | List every uncertainty before concluding. |
| high cohesion, low coupling | 高内聚，低耦合 | Design for high cohesion, low coupling. |
| pre-registration | 预注册 | Pre-register the success criteria before looking at results. |
| Chesterton's fence | 切斯特顿的栅栏 | Check Chesterton's fence before removing. |

…and whatever else your files are re-explaining. Bring a term with a PR; the
activation test is the acceptance gate.

## Inside Claude Code

Drop [`SKILL.md`](SKILL.md) into `~/.claude/skills/onenoun/` and say
"onenoun this skill". It runs the CLI when it can and does the three passes by
hand when it cannot, in the same order, with the same guards.

## On pull requests

[`action.yml`](action.yml) comments the audit table on any PR that touches a
skill file. Beta: it installs the Claude Code CLI on the runner and needs an
`ANTHROPIC_API_KEY` secret. Example workflow in
[`.github/workflows/example-audit.yml.example`](.github/workflows/example-audit.yml.example).

## Other models

`--driver "shell:<command> {prompt}"` runs any CLI; stdout is the answer and
the first JSON object in it is the structured answer. Only the `claude` driver
has been tested here.

## When it makes things worse

- The skill is read by a smaller model than the one that passed the activation
  test. A noun activates what the reader knows.
- The term is ambiguous in the skill's language. The Chinese names in the
  lexicon are the ones used in the slide and in common usage; check them.
- The prose was doing work the classifier called restatement. That is what
  `ablate` is for; read the transcripts, not just the score.
- The classifier is not deterministic. Two runs on the same file differed by
  three percentage points. Audit twice if the number matters.

## What it never does

No hosted service, no API key handling, no telemetry. No free-written
rewrites: replacement text comes only from the lexicon. No overwriting: the
pruned file is written next to yours. No touching a guarded unit, whatever
the model says.

## Verify it yourself

```sh
git clone https://github.com/jcaiagent7143-ui/onenoun && cd onenoun
uv sync && uv run pytest -q          # guards, idempotence, lexicon shape
uv run onenoun lexicon check         # 30 activation tests, ~$0.70
uv run onenoun segment SKILL.md      # this repo's own skill, no model call
```

---

Built by [Jack Chew](https://github.com/jcaiagent7143-ui), who also builds
[LinkDigest](https://linkdigest.dev), which is how a Douyin post became text I
could read. MIT.
