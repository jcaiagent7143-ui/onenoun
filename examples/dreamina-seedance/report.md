# onenoun audit — ~/.claude/skills/dreamina-seedance/SKILL.md

approx tokens: **1495 → 1480** (+1%)  ·  units: 74 total, 12 touchable, 21 guarded  ·  labels: FACT 11, METHOD 0, FILLER 1, UNSURE 0
driver: claude, 1 call(s), $0.406

| # | lines | label | term | tokens | saved | why |
|---|---|---|---|---|---|---|
| 4 | 9-9 | FACT |  | 54 |  | Describes the specific behavior/scope of this particular skill (BytePlus Ark API, POST→poll→download flow) — project-specific, not a lexicon method. |
| 12 | 19-19 | FACT |  | 16 |  | Describes a specific script behavior (checks BYTEPLUS_ARK_API_KEY env var, gives clear message) tied to this tool; though it echoes the general shape of 'fail fast', it names a concrete precondition (env var) so per the rule 'if only part of the unit is generic, it is FACT' it stays FACT. |
| 37 | 55-55 | FACT |  | 18 |  | Concrete, tool-specific technique for maintaining continuity across Seedance clips — not derivable from general knowledge. |
| 38 | 56-56 | FACT |  | 34 |  | Gives a concrete worked example (sphere glowing → dissolving into dashboard) specific to this workflow; a war story/example with concrete details. |
| 39 | 57-57 | FILLER |  | 14 | 14 | Purely a cross-reference reminder to the no-text rule documented in detail later in the same file ('below') — adds no new information. |
| 47 | 65-65 | FACT |  | 87 |  | States a specific empirical/domain finding about video diffusion models and text rendering, with concrete example prompt phrases — not general knowledge, not a lexicon method. |
| 50 | 68-68 | FACT |  | 17 |  | Specific actionable prompting guidance (use colors/icons/shapes/motion instead of typography) for this tool's domain; not a restatement of a lexicon term. |
| 51 | 69-69 | FACT |  | 44 |  | Names concrete brands and their specific colors (WhatsApp green, Messenger blue, etc.) — clearly project/domain-specific detail. |
| 52 | 70-70 | FACT |  | 34 |  | Concrete, specific visual guidance for dashboard scenes in this tool's prompts. |
| 53 | 71-71 | FACT |  | 29 |  | Concrete, specific visual guidance for 'AI brain' scenes in this tool's prompts. |
| 55 | 73-73 | FACT |  | 28 |  | Names specific tools (After Effects, browser overlay) as a fallback recommendation — concrete and project-specific. |
| 57 | 75-75 | FACT |  | 40 |  | Gives exact phrases to include in prompts and where to place them — concrete, actionable, tool-specific instruction. |

## Guarded (never sent to the model)

- lines 13-13 · backtick · Set once in `~/.claude/settings.json`:
- lines 23-23 · lead_in · One-shot orchestrator — use this unless you need granular control:
- lines 38-38 · backtick · `--prompt` takes a **file path** (not inline text) so large multi-beat prompts survive she
- lines 42-42 · backtick · `scripts/generate.sh` — reads a JSON payload on stdin, POSTs to `/tasks`, echoes the task 
- lines 43-43 · backtick · `scripts/poll.sh <task_id>` — polls `/tasks/{id}` every 10s (≤10 min), prints the video UR
- lines 44-44 · backtick · `scripts/concat.sh --out OUT.mp4 IN1.mp4 IN2.mp4 [IN3.mp4 …]` — ffmpeg-merges multiple cli
- lines 48-48 · lead_in · Chain two or three generations for a longer story, then merge:
- lines 50-50 · backtick · **Generate clip 1** with `run.sh --out clipA.mp4`. It writes a sidecar `clipA.url.txt` con
- lines 51-51 · backtick · **Generate clip 2** with `run.sh --out clipB.mp4 --ref-video "$(cat clipA.url.txt)"` — the
- lines 52-52 · backtick · **Merge** with `concat.sh --out final.mp4 clipA.mp4 clipB.mp4`.
- lines 54-54 · short · Cross-clip continuity tips:
- lines 61-61 · number_unit · Seedance 2.0 responds best to prompts that are **cinematic scene direction**, not bullet-l
- lines 67-67 · short · **Do this instead:**
- lines 72-72 · backtick · If the user insists on a logo or wordmark, **supply it as a reference image** (`--ref-imag
- lines 77-77 · lead_in · Reuse the reference curl example shape when adapting:
- lines 94-94 · backtick · Detailed API schema and error codes: see `reference.md`.
- lines 98-98 · short · For this user's website pattern:
- lines 100-100 · backtick · Save MP4 to `<repo>/public/videos/<slug>.mp4` (served at `/videos/<slug>.mp4`).
- lines 101-101 · backtick · Import the shared `VideoPlayer` component (`src/components/VideoPlayer.tsx`) and render it
- lines 102-102 · backtick · No `next.config.ts` change needed — local files bypass remote pattern allowlists.
- lines 104-104 · backtick · If `VideoPlayer` doesn't exist in the project, create one: a thin client component wrappin

## The model's own uncertainties (列出所有不自信的点)

- Unit 12 ('Scripts fail fast with a clear message if the env var is missing') closely paraphrases the lexicon's 'fail fast' definition; I labeled it FACT because it names a concrete precondition (the env var check) per the partial-specificity rule, but a stricter reading could call it METHOD since replacing it with 'fail fast' would lose little.
- Unit 39 ('Keep the no-text rule... consistent across all clips') I labeled FILLER as a pure cross-reference to content stated elsewhere, but it could arguably be read as a distinct actionable instruction (apply the rule per-clip) rather than mere restatement, which would make it FACT instead.
- Unit 50 ('Tell the story with colors, icons, shapes, motion — not typography') sits close to being a generic restatement of the problem stated in unit 47; I judged it FACT because it's the prescribed solution rather than a duplicate of the problem statement, but reasonable readers could see it as redundant/FILLER given 47 already implies the same fix.
