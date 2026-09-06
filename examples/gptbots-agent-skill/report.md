# onenoun audit — ~/.claude/skills/gptbots-agent-skill/SKILL.md

approx tokens: **3563 → 3512** (+1%)  ·  units: 86 total, 7 touchable, 37 guarded  ·  labels: FACT 5, METHOD 1, FILLER 1, UNSURE 0
driver: claude, 1 call(s), $0.137

| # | lines | label | term | tokens | saved | why |
|---|---|---|---|---|---|---|
| 10 | 18-18 | FACT |  | 41 |  | Describes this specific skill's capability set (evaluation, quality assessment, RAG testing, scheduled triggering, KB management) tied to the GPTBots Open API — not a re-explanation of a lexicon term. |
| 11 | 19-19 | FACT |  | 36 |  | Names the platform's three specific storage formats (Document/Table/Q&A) and specific tuning knobs (chunking, metadata, retrieval) — project-specific, not lexicon. |
| 33 | 59-59 | FACT |  | 30 |  | Specifies concrete material types particular to this domain (FAQ/docs, data, examples) as a workflow step; not a restatement of a lexicon term. |
| 36 | 62-62 | FILLER |  | 13 | 13 | Merely points to the fuller 'Quality check' and 'Delivery' sections already documented later in the file; adds no new information itself. |
| 54 | 80-80 | FACT |  | 73 |  | Specific prompt-writing guidance for this skill's LLM-capable nodes; doesn't match any lexicon term precisely (not the same as Occam's razor, which concerns explanations/designs, not writing style). |
| 55 | 81-81 | METHOD | separation of concerns; DRY | 45 | 37 | Content is exactly separation of concerns (single responsibility per node) plus DRY (state shared rules once, in the identity prompt) applied to prompt design; nothing beyond those two principles is asserted. |
| 57 | 83-83 | FACT |  | 81 |  | Specific QA step naming exact node/prompt types in this config (identity, LLM/classifier/condition) and a specific consequence claim ('no amount of flow design can fix'); not a clean restatement of a single lexicon term. |

## Guarded (never sent to the model)

- lines 12-12 · url · A platform-level skill for working with **GPTBots** (https://www.gptbots.ai) Agents and Wo
- lines 14-14 · short · Use this skill to:
- lines 15-15 · backtick · **Read / update / optimize** an Agent or Workflow config from a **user-provided `.bot` or 
- lines 16-16 · backtick · **Create a new** Agent or Workflow from scratch (scenario + requirements → importable `.bo
- lines 17-17 · backtick · **Import & publish** a generated `.bot`/`.flow` to a **test-mode** Agent/Workflow via API 
- lines 45-45 · backtick · Don't hand-write config JSON. Write a small Python generation script that imports the buil
- lines 47-47 · backtick · Always keep the prompts **out of the build script**. The standard layout for every bot is 
- lines 49-49 · backtick · **Convention: make each prompt file's name equal the component's `name`** in `b.add(type, 
- lines 53-53 · backtick · This skill does not bundle any config. The target `.bot` / `.flow` is **provided by the us
- lines 58-58 · backtick · Read the user's `.bot` (or `.flow`) file to understand the current design. Identify its ty
- lines 60-60 · backtick · Edit **only** the documented fields needed (see the matching `references/create-gptbots-*.
- lines 61-61 · backtick · For a **Workflow / FlowAgent**, generate an `overview.md` next to the output file containi
- lines 65-65 · lead_in · Follow the reference matching the target type, then quality-check and deliver:
- lines 66-66 · backtick · QuestionAnswer → `references/create-gptbots-agent.md`
- lines 67-67 · backtick · FlowAgent (`botType=Flow`) → `references/create-gptbots-flowagent.md`
- lines 68-68 · backtick · Workflow → `references/create-gptbots-workflow.md`
- lines 71-71 · backtick · For evaluation / quality assessment / RAG testing / scheduled triggering / data & knowledg
- lines 74-74 · backtick · When the user wants to turn raw/messy material (PDF, Word, Excel, web export, FAQ, notes) 
- lines 78-78 · backtick · Several nodes carry an LLM prompt: the top-level identity `prompt` of a QuestionAnswer age
- lines 82-82 · backtick · **Classifier branch rules are prompts too.** Each `Branch` category rule and `INTENT` inte
- lines 87-88 · lead_in · These mistakes pass casual inspection but break import or the imported bot. The builder sc
- lines 90-90 · backtick · **Strong-typed integers must be bare integers**, never quoted strings or `vueflow__…` ids.
- lines 91-91 · backtick · **Top-level `multiModal` is mandatory on every BOT**: imported without a non-null `multiMo
- lines 92-92 · backtick · **Prompt messages use `text`, not `content`** — a `content` key imports as a BLANK prompt.
- lines 93-93 · backtick · **Classifier (`Branch`) rules live in the edge's `condition` as natural-language text**, w
- lines 94-94 · backtick · **Platform variables need double braces `{{var}}`** — never run `str.format()`/f-strings o
- lines 95-95 · backtick · **Variable assignments** are `{variableName, operation, value}` with `operation` ∈ `Cover`
- lines 98-98 · backtick · After producing or editing any `.bot`/`.flow`, run:
- lines 102-102 · backtick · On a non-zero exit code, fix the JSON per the reported `path`/`fix`, rerun, and only deliv
- lines 105-105 · backtick · Place the new/updated `.bot` / `.flow` file (and `overview.md` with its mermaid diagram, f
- lines 106-106 · lead_in · Tell the user one of two ways to apply it:
- lines 107-107 · url · **Manual:** on **www.gptbots.ai** (developer space), **Create Agent / Workflow → Import**,
- lines 108-108 · backtick · **API (test-mode target):** if the target Agent/Workflow was created in **test mode**, run
- lines 111-111 · url · Docs (authoritative): https://www.gptbots.ai/docs/api-reference/overview
- lines 112-112 · backtick · Base URL by region: `https://api-${endpoint}.gptbots.ai/` — `sg`=Singapore (default), `jp`
- lines 113-113 · backtick · Auth: `Authorization: Bearer <YOUR_API_KEY>` — never write a real key into any file. You m
- lines 114-114 · backtick · Playbooks: `references/call-gptbots-api.md`.

## The model's own uncertainties (列出所有不自信的点)

- Unit 33: borderline between FACT and FILLER — 'do not invent requirements' is fairly generic advice, though the material types listed are project-specific.
- Unit 54: considered mapping to Occam's razor ('cut filler') but the lexicon term is about explanations/design simplicity, not prompt-writing style, so I kept it FACT — low confidence on this boundary.
- Unit 55: labelling as METHOD assumes the node/identity-prompt framing carries no extra project-specific constraint beyond applying separation of concerns + DRY; if the identity-prompt-as-single-source-of-truth convention is considered a project-specific architectural decision, this should be FACT instead.
- Unit 57: could partially overlap with 'red team' or 'adversarial review' (self-critique pass) but the described action (checking for contradictions across prompts) isn't a clean match to any single lexicon term, so I called it FACT rather than METHOD — moderate confidence only.
