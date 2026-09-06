# onenoun ablation — SKILL.md

**pruned ≥ original in 3/5** (won 3, tied 0, lost 2) · tokens 1503 → 1371 (-9%) · **mixed**
driver: claude, 16 call(s), $0.59. Blind pairwise judge; A/B order randomised per task.

| # | task | winner | judge's reason |
|---|---|---|---|
| 1 | We keep writing eval scripts with mocked API responses and hand-crafted test cases, and our agent always score | pruned | Both answers cover largely the same substance: sourcing eval sets from real production queries with PII scrubbed, using a held-out slice never tuned against, running against staging/sandbox environmen |
| 2 | I want to set up a recurring cycle where after every agent run we capture failures, distill them into a short  | pruned | Both answers map the same eval-to-root-cause-to-fix-to-verify-to-distill discipline onto prompt iteration and hit nearly identical major beats (log real runs, cluster failures by mechanism not symptom |
| 3 | Our evals currently hit our production database and once accidentally sent real emails to customers during a t | original | Both answers cover the same core guardrails (data isolation via replica/snapshot, intercepting the side-effect chokepoint with sandbox mode, environment fencing with separate credentials, recipient al |
| 4 | List the common mistakes teams make when building 'realistic' evaluation harnesses for agents, like reusing tr | original | Both answers cover the same core categories (data contamination, judge bias, mocked environments, metric gaming, silent scope narrowing) with similar quality bullet points, but Answer A repeatedly ref |
| 5 | We built this improvement loop for one internal tool and now want to reuse the same approach for three other p | pruned | Both answers converge on the same five per-project role slots (deploy target, real data source, observability surface, side-effect edge, validation gate), suggesting both drew from a similar underlyin |

## Judge's uncertainties (列出所有不自信的点)

- task 1: I cannot verify with certainty whether the specific session that produced Answer A actually lacked tool access at generation time — it's possible the model was genuinely run in a text-only mode for that turn despite the general system prompt describing tool availability, which would make its claim accurate rather than fabricated.
- task 1: I am not fully certain how much weight to give the missing scoring-methodology section in Answer B versus the fabricated-tools claim in Answer A, since both are legitimate quality issues but affect different criteria (completeness vs. invented facts) and reasonable graders could weigh them differently.
- task 1: I could not confirm whether the user has an existing codebase or eval script in this session (the working directory is an empty temp folder and not a git repo), so I cannot be sure whether Answer A's offer to 'read via tools' was even a relevant or actionable next step versus Answer B's clarifying questions.
- task 1: I do not know if there is a project-specific instruction file (referenced in the task as 'a different version of the same instruction file') that might explain or justify the tools claim in Answer A, since I was not shown the underlying system/instruction file differences between the two assistants.
- task 2: I cannot verify which underlying instruction-file version each assistant was operating under, so I cannot determine whether the observed differences stem from the instruction file itself or from incidental variation in generation, which matters for judging whether the difference is systematic or noise.
- task 2: I have no way to test either proposed loop against a real agent-failure dataset, so my assessment of which practices (e.g., the N=2-3 repeat threshold, held-out set rotation) would actually work better in practice is based on domain reasoning rather than empirical validation.
- task 2: Both answers are close enough in overall quality and structure that reasonable evaluators could weight the specific additions differently (e.g., someone might value Answer A's explicit pitfalls section or its offer to draft a log schema as more useful than I did), so the margin of victory I assigned to B could be seen as too strong or too weak.
- task 2: I could not confirm whether the user has any additional unstated constraints (e.g., team size, tooling, or scale of agent runs) that might make one answer's specific mechanisms (like shadow deployment or N-repeat thresholds) more or less applicable than the other's.
- task 3: I could not determine what "the loop" refers to in Answer A's text, so I cannot be fully certain whether it is a genuine hallucinated reference or an intentional (if oddly phrased) allusion to something the user would recognize from their own tooling, which affects how heavily I penalized it.
- task 3: I am not certain whether Answer A's inclusion of a "post-incident distillation" note-writing step should be counted as valuable process advice or as padding beyond the scope of "guardrails," since reasonable experts could disagree on whether documentation practices belong in this kind of guardrail list.
- task 3: Without knowing the user's actual eval framework or tech stack, I cannot verify whether the specific technical suggestions (transaction rollback, sandbox API keys, Mailtrap/local SMTP catcher, separate DB schema) are equally feasible in their environment, so I judged both answers purely on generic best-practice soundness rather than fit to an unseen real system.
- task 3: I cannot be fully confident that Answer A's automated regression test suggestion isn't a meaningfully more important safeguard than Answer B's manual human-review step, since an automated test is arguably more reliable than a one-time manual log review, which could shift the balance back toward A for some evaluators.
- task 4: I cannot see the actual instruction files each assistant was given, so I cannot confirm whether Answer A's reference to 'the loop above' was an expected callback to system-prompt content considered correct by a hidden rubric rather than a genuine flaw, which materially affects how much weight that issue should carry.
- task 4: I could not verify from the transcript alone whether either assistant fabricated any of the technical claims (e.g., about self-preference bias in LLM judges or specific failure modes) versus drawing on well-established knowledge, since no external sources were cited or checked.
- task 4: It is unclear whether the user's underlying instruction file favored conciseness or exhaustive categorization, so I cannot be fully certain Answer B's slightly longer list of agent-specific points is actually preferred over Answer A's offer to inspect real code, which is a more actionable next step.
- task 4: I do not know if there is a hidden grading criterion that penalizes or rewards ending with a follow-up offer (as Answer A does) versus a summary statement (as Answer B does), so my preference for B's self-contained ending could be miscalibrated.
- task 5: I cannot see the actual underlying skill or instruction document either assistant was working from, so I cannot verify whether Answer B's explicit 'fixed loop skeleton' phrasing is a faithful extraction from that document or a partially invented addition, which directly affects the 'no invented facts' judging criterion.
- task 5: I don't know the real nature of the 'internal tool improvement loop' being generalized (e.g., whether it involves trading, deployment automation, or something else), so I cannot fully confirm that the 'side-effect edge' and 'validation gate' descriptions in either answer accurately reflect the original tool's actual mechanics versus being generic boilerplate that happens to fit the request.
- task 5: I could not determine whether the user's system prompt in each session included different versions of a specific named skill file (as the task framing implies), so my assessment relies on inferring quality purely from the visible text rather than confirming which version's guidance was more accurately followed.
- task 5: It is possible that Answer A's brevity and its offer to 'draft the concrete slot-mapping for each' stack once given details is actually the more appropriate response style for this exploratory question per the guidance to keep exploratory answers short, and I am not fully certain Answer B's longer, more structured format isn't over-delivering relative to what was strictly asked.

## Transcripts

### Task 1

We keep writing eval scripts with mocked API responses and hand-crafted test cases, and our agent always scores great but then fails in production. Can you help me redesign our eval loop so it actually tests against real user queries and real system state instead of fakes?

**With original skill**

The core problem: mocked eval scripts prove your agent does what *you* coded it to do, not what it does against the real world's rate limits, latency, auth quirks, schema drift, or actual user phrasing. A green mock suite and a broken prod agent are not a contradiction — they're measuring different things.

Since I have no tools in this session, I can't inspect your current eval scripts or repo yet — normally I'd start by reading them to see exactly where the mocking happens and what the agent's side effects are. Here's the redesign I'd propose; tell me to proceed and I'll adapt it to your actual code once tools are available.

## 1. Separate "unit tests" from "the eval"

Keep your mocked tests — they're fine as fast regression checks for logic. But stop treating them as the signal for "does the agent work." Rename them internally if needed so nobody confuses the two. The eval is a different artifact entirely.

## 2. Run the real production code path

The eval should invoke the actual agent binary/service — same prompt construction, same retrieval, same tool-calling code — against real dependencies (real API, real DB/index, real auth). The **only** thing you swap is the side-effect at the very edge: if the agent sends emails, books orders, writes to prod DB, etc., swap *that* single call for a dry-run/sandbox equivalent. Everything upstream of it (ingest → retrieve → reason → decide) stays real.

## 3. Real queries, not hand-crafted cases

- Pull a sample of **actual production traffic** (logged user queries, with PII scrubbed) as your eval set, not queries you invented to make the demo look good.
- Split by time: train/tune prompts or retrieval on older logs, judge on a **held-out, more recent slice** you haven't looked at. Judging on the same queries you tuned against is in-sample self-deception — it will look great and mean nothing.
- Include the messy stuff: truncated queries, typos, multi-turn context, queries that previously caused failures (build a "known hard cases" regression set from real incidents).

## 4. Real system state

- Point at a staging environment that mirrors prod data volume/shape, or at prod in read-only/sandboxed mode — not an in-memory fixture with 5 rows.
- Let the eval run long enough to hit real conditions: rate limits, cold caches, concurrent load, token/connection exhaustion. A clean single-shot run hides connection leaks and reconnect storms the same way mocks do.

## 5. Pre-commit the pass/fail bar before you look at results

Decide up front: what accuracy/success rate, what latency ceiling, what error rate, what sample size, on the held-out set. Don't tune the bar after seeing numbers — that's goalpost-moving. If it doesn't clear the bar, the honest output is "not ready," not "let's redefine success."

## 6. Score with something that reflects real success, not surface match

Hand-crafted expected-output string matching is another form of mocking. Prefer:
- Task-completion checks against real system state (did the record actually get created correctly, did the retrieved doc actually answer the question) rather than exact-string diffs.
- LLM-as-judge or human spot-check on a sample, calibrated against known-good/known-bad examples.
- Log what got dropped/truncated/skipped during scoring — silent sampling caps make coverage look better than it is.

## 7. When something fails, root-cause it, don't patch the symptom

Reproduce against the real trace, find the mechanism (bad retrieval chunking, a rate limit, a stale token, a prompt regression), fix it, add a regression test for that mechanism, then re-run it through the *real* eval to confirm it's actually fixed — not just that the new unit test passes.

## 8. Distill every cycle

Keep a running log (a file in the repo, e.g. `EVAL_LEARNINGS.md` or similar) of: symptom → root cause → fix → guard added → real-eval verdict. Read it before each new eval cycle so the same production failure mode doesn't get "fixed" the same way twice.

---

If you want, share (or let me read via tools) your current eval script and the agent's architecture, and I'll turn this into a concrete implementation plan — what to swap for dry-run, where to source real query logs, and what the scoring function should actually check.

**With pruned skill**

Mocks can only prove your code does what you *think* it does — they can't surface things you're wrong about in the real environment (rate limits, auth quirks, schema drift, latency, real query distributions). The fix isn't better mocks, it's shifting the eval to run the real code path against real state, with only the risky side-effect (writes, sends, trades, etc.) sandboxed.

Concrete redesign:

**1. Real query source, not hand-crafted cases**
Pull the eval set from actual production traffic/logs (redacted for PII), not cases you wrote. Split it: a rotating slice for fast iteration, and a **held-out set you never look at until final validation** — the moment you tune against it, it stops being out-of-sample.

**2. Real system state, not stubs**
Run against a staging replica of the DB/index/cache seeded from real production data, and real sandbox accounts for third-party APIs — not response fixtures. If a dependency truly can't be sandboxed, that's the one edge you dry-run; everything upstream (retrieval, tool calls, real API reads) stays real.

**3. Run it long enough to hit steady state**
Single-shot invocations hide connection leaks, memory growth, rate-limit backoff behavior. Shadow real traffic for a sustained window and watch logs/metrics, not just final outputs.

**4. Pre-commit the pass/fail bar before looking at results**
Define the metric and threshold up front. If nothing clears it, the answer is "not validated" — don't redefine "pass" after seeing the numbers.

**5. Log anything the eval drops or caps**
If you sample or truncate real traffic for cost reasons, log what got excluded — a silent cap looks like full coverage when it isn't.

**6. Gate prod rollout**
New agent version only goes live after: out-of-sample real eval passes + friction/cost check (latency, token cost, rate-limit headroom) + explicit sign-off.

**7. Distill every failure**
When production still breaks something the eval missed, don't just patch — add a regression test for the mechanism AND re-run the real eval that should've caught it, then write a short note (symptom → root cause → fix → guard added) to whatever persistent store you use, so the next iteration doesn't repeat it.

To tailor this, tell me: what does your agent's side-effect edge look like (does it write/send/trade, or is it read-only/advisory?), and do you already have a staging environment or sandbox API accounts, or would that need to be built from scratch?

### Task 2

I want to set up a recurring cycle where after every agent run we capture failures, distill them into a short set of rules, and feed those rules back into the next prompt version. Walk me through how that loop should be structured cycle over cycle.

**With original skill**

Here's how I'd structure it, mapping the general "observe reality → root-cause → fix → verify → distill" loop onto prompt iteration specifically:

## The cycle

**1. Capture, don't summarize, at run time**
For every agent run, log the full trace: input, prompt version ID, tool calls, final output, and the actual outcome (task succeeded/failed, and how you know — user correction, downstream error, eval score). Capture failures as raw evidence, not as your interpretation of them. You'll re-derive the interpretation later with more cases in view.

**2. Classify failure vs. success explicitly**
Define "failure" up front (task-outcome based, not vibes) so you're not retroactively deciding what counts — that's goalpost-moving. A run that "looks fine" but produced a wrong answer downstream is still a failure.

**3. Cluster failures by mechanism, not by surface symptom**
Group failures by *why* they happened (ambiguous instruction, missing constraint, wrong tool chosen, format the agent guessed wrong, context truncated) rather than by what task they occurred on. Two failures that look different on the surface often share one root cause — one rule fixes both. Conversely, don't merge two failures into one rule just because the symptom text looks similar if the mechanisms differ.

**4. Root-cause each cluster before writing a rule**
For each cluster, find the actual mechanism: was the prompt silent on this case? Did it say something that was technically satisfiable in a way you didn't intend? Was it a model limitation no prompt text will fix (in which case the answer is a code-level guard, not a rule)? Don't write a rule until you can state the mechanism in one sentence.

**5. Draft rules — small, specific, falsifiable**
Each rule should be traceable to one failure mechanism and stated concretely enough that you could check whether it fired. Avoid vague additions like "be more careful with edge cases" — that's not a rule, it's a wish. Prefer something like "when X input pattern occurs, do Y" tied directly to the observed failure.

**6. Merge into a new prompt version, and prune while you're in there**
Add the new rules, but also look at existing rules: are any now redundant, contradicted, or dead (never observed firing / never observed being needed in recent runs)? Prompts that only ever grow turn into a pile of patches that eventually conflict with each other. Version the prompt (v12, v13...) so you can diff and roll back.

**7. Validate out-of-sample before shipping**
This is the step people skip and it's the one that matters most: don't judge the new prompt only against the failures that inspired the rules (in-sample — of course it fixes those, you wrote it to). Hold out a slice of failures/cases not used to write the rules, and replay the new prompt against those, plus a regression set of previously-*passing* cases to check you didn't break anything. Pre-commit what "good enough to ship" means before you look at the replay results.

**8. Deploy and re-observe on real runs**
Once shipped, watch the next batch of real runs for whether the specific failure mode actually disappeared in production behavior — not just in your replay set. Sometimes a rule "works" in replay but the model interprets it differently in the wild.

**9. Distill to a persistent learnings log**
Append one entry per cycle: symptom observed → root cause → rule added → prompt version → evidence it helped (or didn't). This is what makes it a *loop* rather than repeated one-off patching — the next cycle starts by rereading this log so you don't re-diagnose or re-add something already tried and discarded.

**10. Periodically audit rule health**
Every few cycles, review the full rule set: which rules have fired/mattered recently, which are stale, which have started conflicting as the prompt evolved. Prune before the prompt calcifies into unmaintainable patchwork.

## Pitfalls to design against
- **In-sample self-deception**: "the rule fixes the failures I wrote it from" isn't evidence it generalizes — that's what step 7 is for.
- **Rule bloat**: unlimited additive patching without pruning eventually degrades the prompt (contradictions, dilution, length limits).
- **Symptom patching**: adding a rule that suppresses the visible failure without addressing the mechanism — it resurfaces in a different shape.
- **Silent goalpost redefinition**: if a rule doesn't fix the held-out cases, the honest outcome is "this rule didn't work" — not quietly redefining success to declare victory.

If you want, I can help draft the actual log schema (fields for the learnings store) or a template for how each rule entry should be worded once you've got real failure data to work from.

**With pruned skill**

Here's how I'd structure it, mapped onto the same eval→fix→verify→distill discipline you'd use for any system, adapted to prompt iteration specifically.

## The per-cycle loop

**1. Run on real traffic, log everything**
Capture full transcripts from actual runs (real user inputs, real tool calls/outputs, real final output) — not synthetic test cases you wrote to be easy. Store input, full trace, output, and outcome signal (user correction, downstream error, human grade, task success/fail) per run.

**2. Triage failures, don't just collect them**
From the run log, pull the failures. For each one, write down: what happened, what *should* have happened, and — critically — the **root cause mechanism** (ambiguous instruction, missing constraint, wrong tool chosen, format drift, hallucinated fact, over-eager action, etc.), not just the surface symptom. Two failures that look different on the surface can share one root cause; two that look similar can have different ones. Don't dedupe by symptom text — dedupe by mechanism.

**3. Hold failures until a pattern repeats**
Don't turn a single failure into a rule immediately — that's how prompts accumulate one-off patches that overfit to a single example and bloat over time. Require the same root cause to show up **N times (e.g. 2–3) across independent runs** before promoting it to a candidate rule. One-off failures go into a watchlist, not the prompt.

**4. Distill candidate rules**
For each qualifying pattern, write the rule as: *trigger condition → required behavior*, plus the one example that best illustrates it (for your own record, not necessarily in the prompt). Keep it as short and general as the pattern actually warrants — don't write a rule so narrow it only fixes the exact failing input.

**5. Hold out a validation set before merging**
Split your failure corpus: some failures go into the "fix this cycle" set, some are held back as an out-of-sample check. This is the part people skip and it's exactly where p-hacking creeps in — if you write rules by staring at all your failures including the ones you'll "test" against, you'll always pass. Keep a held-out slice the rule-writer doesn't see.

**6. Draft prompt v(n+1)**
Add/edit the minimum set of rules needed. Actively look for conflicts with existing rules — contradicting or overlapping instructions are one of the most common ways prompts degrade cycle over cycle. If a new rule contradicts or subsumes an old one, replace, don't stack.

**7. Regression-check before rollout (this is the eval gate)**
Run v(n+1) against:
- the full regression set (all previously-fixed failure cases — must still pass)
- the held-out validation set from step 5 (must show the failure rate actually drop, not just the cases you trained the rule on)
- a sample of previously-passing runs (must not newly break — this is where prompt edits silently regress unrelated behavior)

Pre-commit the pass bar *before* running this (e.g., "regression set 100%, held-out set failure rate drops by X, no more than Y% of previously-passing sample flips to failing"). If it doesn't clear the bar, the honest outcome is "this rule set isn't ready" — don't retune until something passes by luck.

**8. Ship and monitor, don't just merge**
Deploy v(n+1), ideally shadow it against v(n) on the same live inputs for a bit before full cutover if the domain has any real-world cost to getting it wrong. Watch real production behavior, not just the offline eval — some failures only show up at real scale/latency/load.

**9. Distill and persist, regardless of outcome**
Append to a durable prompt changelog / learnings store: version number, rules added/changed, the failure pattern and example that motivated it, the eval result (pass/fail, numbers), and any rule that was tried and *rejected* because it didn't clear the bar or caused a regression — that's as valuable as one that worked, and stops you from re-trying it next cycle.

**10. Prune periodically**
Every few cycles, review the accumulated rule set for redundancy, rules that no longer fire (their pattern hasn't recurred in a long time — maybe the underlying cause was fixed elsewhere), or rules that could be merged into a more general one. Left unchecked, this loop tends to monotonically grow the prompt until it's unwieldy and self-contradictory.

## Artifacts to keep across cycles
- **Run log** — raw real transcripts, append-only.
- **Failure/root-cause log** — triaged, with mechanism tags.
- **Regression set** — every past failure that's been fixed; must always pass.
- **Held-out validation set** — rotated/refreshed so it doesn't get contaminated by rules being tuned against it.
- **Prompt changelog** — versioned, with rationale and eval results per version, including rejected attempts.

## Main pitfall to watch for
The biggest risk in this specific loop is overfitting the prompt to your failure log the same way a model can overfit to training data — each cycle nudges the prompt toward whatever the last batch of failures looked like, and without the held-out check and regression set, you can't tell "genuinely more robust" from "happens to fix the cases I looked at." The N-repeat threshold (step 3) and the held-out/regression gate (step 7) are what keep the loop honest rather than just reactive.

### Task 3

Our evals currently hit our production database and once accidentally sent real emails to customers during a test run. What guardrails should I put in place so real-data evals stay safe and don't cause side effects like that again?

**With original skill**

Here's a concrete guardrail set, roughly in order of blast-radius reduction:

**1. Isolate the data layer**
- Point evals at a restored snapshot / read replica / anonymized copy of prod, not prod itself. Never let eval code hold prod write credentials at all — separate DB users with separate, narrower grants (read-only, or write-only to a scratch schema).
- If full snapshotting is too heavy, at minimum use a separate database/schema per eval run so nothing lands in prod tables.

**2. Cut the side-effect edge, not the whole pipeline**
- Keep ingest → parse → decide logic running against real code paths, but swap only the outbound action (email sender, payment charge, webhook call) for a dry-run/no-op implementation behind the same interface. This is the "paper trading" pattern — everything upstream stays real, only the final effectful call is intercepted.
- Concretely for email: route through a sandbox provider mode (e.g. provider's test API keys, Mailtrap/local SMTP catcher) or a feature-flag that logs "would send to X" instead of calling the real send API. Do this at the client/adapter layer, not scattered through business logic, so it can't be bypassed accidentally.

**3. Hard environment fencing**
- Config/env var (`EVAL_ENV=sandbox`) checked at startup that refuses to boot if it detects a prod DB connection string or prod API keys. Fail loudly, not silently.
- Separate credentials/secrets per environment so it's structurally impossible for eval code to authenticate to prod's email provider or write DB — not just a runtime check, but keys that literally don't have those permissions.

**4. Allowlist/denylist as a last-resort net**
- If real customer records are ever in scope (e.g. read-only queries against a prod replica), enforce an allowlist of test/internal email domains for any outbound-capable path, and block anything else even in "safe" mode — defense in depth in case the sandbox swap fails.

**5. Make it observable and reviewable before it's trusted**
- Log every would-be side effect (send, write, charge) during eval runs, and log any *dropped/capped* data too — silent truncation is its own failure mode.
- Have a human review the "would have sent N emails to these addresses" log at least once when introducing a new eval, before trusting the guardrail.

**6. Process control**
- No eval should be runnable with a single command that also happens to hit prod by default — the default/no-args behavior should be sandbox; hitting prod (if ever needed) should require an explicit, hard-to-typo flag plus separate approval.
- CI/CD: evals run in a pipeline whose service account has no prod credentials, period.

If you want, tell me the stack (language, email provider, DB) and I can point to the specific interception point in your code (e.g. which client class to wrap) rather than keeping this generic.

**With pruned skill**

Good instinct to fix this before it happens again. Core principle: keep the real data path real, but isolate the *side-effect edge* so nothing irreversible can fire.

## 1. Separate read path from write path
- Evals should read production data (or a fresh, access-controlled replica/snapshot) but **never write to the production DB**. Point writes at a scratch schema/sandbox DB seeded from a prod snapshot, or run in a transaction that's always rolled back.
- If you need "production-like" writes, use a dedicated eval/staging database that's periodically refreshed from prod, not prod itself.

## 2. Hard-gate every outbound side effect, not just email
Any component that talks to the outside world (email, SMS, push, payment, webhook, third-party API) should have a single chokepoint — one client/wrapper — that all send paths go through. At that chokepoint:
- **Default to dry-run/paper mode** in eval environments: log "would have sent X to Y" instead of calling the real provider.
- Make dry-run the default via environment (`APP_ENV=eval` or similar), not an opt-in flag someone has to remember to pass.
- For providers that support it (e.g. SendGrid, Twilio), use sandbox/test API keys in eval environments so even if dry-run is bypassed, the call physically can't reach a real customer.

## 3. Recipient allowlisting as a second layer of defense
Even with dry-run as the primary guard, add a belt-and-suspenders check: if any send call somehow reaches a real provider client during an eval run, validate the recipient against an allowlist (e.g. only `@yourcompany.com` test addresses or a fixed set of test accounts) and hard-reject/throw otherwise. Two independent guards means one bug doesn't equal an incident.

## 4. Environment identity should be unmistakable and hard to fake
- Tag every eval run with an explicit environment marker (config, not inferred), and have the send-chokepoint refuse to run in "live" mode unless that marker is absent.
- Avoid config where "eval" and "prod" differ by one easily-mistyped flag — prefer a completely separate credentials/config file for eval so there's no live API key present at all to accidentally use.

## 5. Fail closed
If the environment/config is ambiguous or missing, the send chokepoint should refuse to send (fail closed) rather than defaulting to live. This is the "unsafe real evals" anti-pattern from the loop — don't let irreversible actions run before validation.

## 6. Regression test for this specific incident
Add a test that asserts: running the eval suite/config produces zero real provider API calls (mock the actual HTTP client at the network boundary and assert it's never invoked with live credentials). This is a fast mock-based regression check, separate from the real-data eval — it exists specifically to catch "did we accidentally wire this back to prod" mistakes.

## 7. Post-incident distillation
Since this already happened once, worth writing a short durable note (wherever your team keeps engineering learnings): symptom (real emails sent during eval), root cause (no separation between real-data read path and real-effect write path), fix (dry-run chokepoint + allowlist + separate creds), guard added (regression test #6). That way the next person touching eval infra doesn't rediscover this the hard way.

---

If you want, I can look at your actual eval harness code (if you point me to it) and identify the specific chokepoints where sends/writes happen, so this isn't just abstract advice — but I have no tools in this session, so that would need to happen in a follow-up where I can read files.

### Task 4

List the common mistakes teams make when building 'realistic' evaluation harnesses for agents, like reusing training examples as test cases or grading with the same model that generated the answer.

**With original skill**

Common failure modes when teams build "realistic" agent eval harnesses:

**Data contamination**
- Reusing training/fine-tuning examples (or near-duplicates) as test cases — inflates scores without measuring generalization.
- No time-based or holdout split for anything the system was tuned on; picking prompts/params on the same data you judge against.
- Scraping eval sets from the same corpus the base model was pretrained on, so "held out" isn't actually held out.

**Judge bias**
- Grading with the same model (or a model in the same family) that generated the answer — self-preference bias makes it rate its own style/reasoning favorably.
- Using an LLM judge without checking judge-human agreement, or without adversarial/known-bad examples to sanity-check the judge actually penalizes failures.
- Letting the judge see chain-of-thought or extra context the real deployment won't have, making grading easier than reality.

**Mocked environment instead of real one**
- Testing against mocked tools/APIs/sandboxes that don't have the real system's rate limits, latency, auth quirks, schema drift, or error modes — agent looks robust in the harness, breaks in production.
- Synthetic tasks that don't match the real distribution of user requests (shape, ambiguity, adversarial phrasing).
- Not modeling real friction: cost, timeouts, partial/flaky tool responses, concurrent state.

**Metric and process gaming**
- Single aggregate pass rate with no error taxonomy — hides *why* it fails and lets fixes optimize the metric, not the mechanism.
- No pre-committed pass/fail bar — moving the goalposts after seeing results, or cherry-picking the best of many variants (multiple-comparisons/p-hacking).
- Silent truncation/capping of eval samples without logging what was dropped, giving false sense of full coverage.
- Only checking final-answer correctness, not intermediate tool calls/state (agent gets right answer via wrong/unsafe path, which the metric can't see).

**Structural issues**
- Eval harness reimplements the agent's logic instead of running the actual production code path (so eval and prod diverge silently).
- No steady-state observation — only checking a clean cold start, missing failures that appear after N turns/hours (memory leaks, drift, connection buildup).
- Non-reproducible runs (nondeterministic sampling, no seed/version pinning) so "improvement" can't be distinguished from noise.

Net effect: teams end up with a leaderboard number that's an artifact of contaminated data, biased judges, and unrealistic environments — the "green tests, broken in production" pattern rather than a true measure of the agent's real-world behavior.

**With pruned skill**

Here are the common failure modes, grouped by where they bite:

**Data contamination**
- Reusing training examples (or near-duplicates) as test cases — the model has memorized the answer, not solved the task.
- Building the eval set from the same source distribution/time period as training data, so "held-out" isn't really independent (e.g., same web scrape, same internal doc corpus).
- Iterating on prompts/tools against the "test" set until it passes, which turns it into a de facto training set (the p-hacking anti-pattern from the loop above).

**Grading/judge bias**
- Using the same model (or a model from the same family) to both generate and grade — it tends to rate its own style/phrasing favorably and misses its own blind spots.
- LLM-judge with no calibration against human labels, so you don't know the judge's error rate or bias direction.
- Grading criteria that reward surface features (length, confident tone, formatting) instead of correctness.

**Task realism**
- Single-turn, static prompts when the real deployment is multi-turn, interactive, or requires the agent to use tools/observe real outputs.
- Mocked tools/environments in the eval when production tools have real latency, rate limits, flaky APIs, or side effects — this hides exactly the class of bug the loop above calls out ("green tests, broken in production").
- No adversarial or distribution-shift cases — only "happy path" tasks that resemble what the agent was tuned on.

**Metric/statistics issues**
- Small eval sets treated as statistically significant; no confidence intervals, so noise gets read as improvement.
- No out-of-sample split for anything the harness or prompts were tuned against — in-sample numbers are a mirage.
- Cherry-picking which runs/seeds to report, or averaging over runs that were also used for tuning.

**Silent scope narrowing**
- Capping/sampling eval data without logging what was dropped, so "100% pass" quietly means "100% of the easy 20 examples that ran."
- Excluding tasks the agent can't do yet by relabeling them "out of scope" after seeing failures.

**Operational/safety leakage**
- Eval environment not isolated from production state, so runs mutate real data or the eval accidentally coincides with real side effects.
- No regression test tied to root cause after a failure — the same bug reappears in a slightly different form next cycle.

If you want, I can look at your actual eval harness code/config and flag which of these apply concretely — just point me at the files.

### Task 5

We built this improvement loop for one internal tool and now want to reuse the same approach for three other projects with completely different tech stacks. What's the general pattern I should extract so it's not hardcoded to the first project?

**With original skill**

The skill doc above already is that generalized extraction — the "Portability" section is the key part to lean on. The pattern to pull out per-project is five role-slots, not five hardcoded pieces:

1. **Deploy target** — wherever the real system actually runs (staging server, container, sandbox account, notebook against live API).
2. **Real data source** — the actual feed/dataset/API for that domain, at real scale and shape — not a fixture.
3. **Observability surface** — whatever that stack already emits: logs, metrics, dashboards, health checks. Reuse existing tooling rather than building new instrumentation.
4. **Side-effect edge** — the *one* component to make safe (dry-run/paper/sandbox), kept as close to the boundary as possible so everything upstream (ingest → parse → decide → gate) still runs as real production code.
5. **Validation gate** — a pre-committed, out-of-sample pass/fail bar, defined *before* looking at results.

Everything else — root-cause-not-symptom, distill-to-a-learnings-store, no in-sample self-deception, no silent truncation — is stack-agnostic and copies over unchanged.

Practically, for each of the three new projects I'd just fill in those five slots (what's the deploy target, what's the real data, what's already observable, what's the one thing to sandbox, what's the bar) rather than writing three separate loop implementations. If you want, tell me the three tech stacks and I'll draft the concrete slot-mapping for each.

**With pruned skill**

The pattern is already stack-agnostic if you split it into a fixed loop skeleton plus five per-project "role bindings" you swap out. Extract it like this:

**1. Keep the loop mechanics fixed (same for all 4 projects):**
ship → observe → eval against pre-committed bar → root-cause fix → regression test + re-run real eval → verify on real system → distill learning.

**2. Parameterize the five roles per project:**
- **Deploy target** — where it actually runs (staging server, container, notebook against a sandbox account, etc.)
- **Real data source** — the actual feed/dataset/API for that domain, not a stub
- **Observability surface** — whatever that stack already emits (logs, metrics, dashboards, health checks)
- **Side-effect edge** — identify the *one* component with irreversible real-world impact (broker order, email send, DB write, deploy step) and make only that dry-run/paper/sandboxed — everything upstream of it stays real
- **Validation gate** — a pre-registered pass/fail metric with an out-of-sample split, defined *before* looking at results

**3. One shared learnings store, tagged by project**, not four separate ones — so cross-project patterns (e.g. "we keep hardcoding rate limits") surface, but you filter by project when starting a new cycle.

Practically: write this as a template/checklist doc (or a short spec file) with the loop steps fixed and a small table at the top where each project fills in its five role bindings. Don't build shared code/abstractions across the four stacks unless you find real duplication after doing it manually once or twice — premature tooling here will fight the "completely different tech stacks" constraint.

Want me to draft that template as a file you can copy into each project?

