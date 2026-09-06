---
name: continuous-improvement-loop
description: >-
  A disciplined loop for evolving any system after it ships: evaluate against REAL execution
  (real systems, real data, real outputs) — NOT mocks — then root-cause failures, fix,
  re-deploy, verify on the real system, and distill the learning so it cannot recur. Use
  whenever building or iterating on a system that touches the real world (deployments, data
  pipelines, API/stream integrations, agents, ML/trading strategies, schedulers) and you need
  to know it ACTUALLY works — not just that it passed tests. Strong triggers: "does this
  actually work", "eval on real data not fake tests", "validate before going live", "test on
  the actual run", "self-improving / self-evolving loop", "continuous improvement", "why did
  it pass tests but fail in production", "backtest / out-of-sample", "prove the edge".
  Project-agnostic — works for any codebase or domain.
---

# Continuous-Improvement Loop

A loop for shipping, then *truthfully* learning whether it works, then evolving it.

## Core principle: evaluate against reality, not fakes

Mock/unit tests prove the code does **what you think**. They cannot reveal what you got
**wrong about the real world** — external rate/connection limits, auth, quotas, latency,
timing, data distributions, schema drift, costs. They are necessary as fast regression, but
they are **not the eval**. The eval gate runs the **actual system against the actual
environment/data** and observes real behavior.

Two failure classes this catches that mocks never will (real cases — keep them in mind):

- **Green tests, broken in production.** A streaming client passed a mock-socket test but
  reconnect-stormed against the real server's 1-connection limit (root cause: a socket *leak*,
  not a flaky network). Mocks had no connection cap, so they couldn't surface it.
- **Great in-sample, fails out-of-sample.** A strategy showed an in-sample t≈5; on held-out
  data it *lost* (negative median, sub-50% win) — even before costs. The in-sample number was
  a mirage.

## The loop — run every cycle

1. **Ship** to a real (or representative) target — safely (see Safety).
2. **Observe** real behavior: logs, metrics, real outputs, resource/connection state, timings.
   Watch long enough to see **steady state**, not just a clean startup.
3. **Eval** against the real signal with a **pre-committed pass/fail bar**. Use **out-of-sample**
   for anything fit/tuned. A null or negative result is valid and valuable.
4. On any anomaly: **root-cause** it — reproduce, find the *mechanism*. Do not patch the symptom.
5. **Fix.** Add a regression test for the mechanism, AND where possible re-run the **real eval**
   that exposed it.
6. **Re-deploy and verify** the fix on the real system (anomaly gone in real behavior, not just
   in tests).
7. **Distill** the learning to a persistent store (symptom → root cause → fix → guard added),
   so the system evolves and can't repeat it.

## Real-eval design rules

- **Run the production code path**, not a re-implementation. Reuse the real components; swap
  only the side-effect at the very edge (paper/dry-run executor, sandbox account). Keep
  ingest → parse → decide → gates real.
- **Use real data at real scale and shape.** Synthetic data hides distribution problems.
- **Out-of-sample is mandatory** for anything fit/tuned/learned: split by time or holdout; pick
  parameters on the train split, judge **once** on the test split. An in-sample number is not
  evidence.
- **Model real frictions** — fees, slippage, latency, rate limits, quotas. A thin edge often
  dies on costs alone.
- **Pre-commit the bar** (sample size, win-rate, effect size, significance) *before* seeing
  results — it prevents moving the goalposts.

## Anti-patterns (do not do)

- **Fake-eval-only** — declaring success because mocked tests pass.
- **In-sample self-deception** — judging on the data you tuned on.
- **Symptom patching** — fixing the log line, not the mechanism.
- **p-hacking / goalpost-moving** — tweaking variants until one randomly passes, or redefining
  "pass" after seeing the data. If nothing clears the pre-committed bar, the honest result is
  "not validated — stop," and say so plainly.
- **Silent truncation/caps** — if the eval samples, caps, or drops data, **log what was
  dropped**; silent limits read as "covered everything" when they didn't.
- **Unsafe real evals** — running irreversible / real-money / destructive actions before
  validation.

## Safety for real evals

- **Isolate**: separate state/dirs, sandbox or paper mode, dry-run side effects, no irreversible
  writes until validated.
- **Don't disrupt the running system**: separate process/state; verify the primary system is
  idle or unaffected before and after.
- **Gate real-world commitment** (real money, prod cutover, mass/outbound action) behind a
  **passed out-of-sample + cost eval AND explicit owner approval**.

## Distillation — the self-evolving part

- After **every** cycle (pass or fail) append a durable note: what was observed, the root cause,
  the fix, the guard added, and the **honest verdict + limitations**. Use the project's
  persistent memory/learnings store.
- **Re-read prior learnings before the next cycle** so mistakes aren't repeated. Verify any
  file/flag/symbol a past note cites still exists before acting on it.

## Portability — mapping to any project

This loop is project-agnostic. Before starting, identify the project's instances of these roles:

- **Deploy target** — server / container / staging / sandbox.
- **Real data source** — production feed, historical dataset, live API.
- **Observability surface** — logs, metrics, dashboards, health endpoints.
- **Side-effect edge to make safe** — the one component to dry-run/paper (broker, mailer,
  writer, deployer) while everything upstream stays real.
- **Validation gate** — the pre-committed pass/fail metric (+ out-of-sample split).
- **Learnings store** — where distilled notes persist across cycles.
