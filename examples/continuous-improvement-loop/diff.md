--- continuous-improvement-loop (original)
+++ continuous-improvement-loop (pruned)
@@ -14,8 +14,6 @@
 ---
 
 # Continuous-Improvement Loop
-
-A loop for shipping, then *truthfully* learning whether it works, then evolving it.
 
 ## Core principle: evaluate against reality, not fakes
 
@@ -41,7 +39,7 @@
    Watch long enough to see **steady state**, not just a clean startup.
 3. **Eval** against the real signal with a **pre-committed pass/fail bar**. Use **out-of-sample**
    for anything fit/tuned. A null or negative result is valid and valuable.
-4. On any anomaly: **root-cause** it — reproduce, find the *mechanism*. Do not patch the symptom.
+4. Fix the root cause, not the symptom.
 5. **Fix.** Add a regression test for the mechanism, AND where possible re-run the **real eval**
    that exposed it.
 6. **Re-deploy and verify** the fix on the real system (anomaly gone in real behavior, not just
@@ -55,19 +53,15 @@
   only the side-effect at the very edge (paper/dry-run executor, sandbox account). Keep
   ingest → parse → decide → gates real.
 - **Use real data at real scale and shape.** Synthetic data hides distribution problems.
-- **Out-of-sample is mandatory** for anything fit/tuned/learned: split by time or holdout; pick
-  parameters on the train split, judge **once** on the test split. An in-sample number is not
-  evidence.
+- Validate out of sample.
 - **Model real frictions** — fees, slippage, latency, rate limits, quotas. A thin edge often
   dies on costs alone.
-- **Pre-commit the bar** (sample size, win-rate, effect size, significance) *before* seeing
-  results — it prevents moving the goalposts.
+- Pre-register the success criteria before looking at results.
 
 ## Anti-patterns (do not do)
 
-- **Fake-eval-only** — declaring success because mocked tests pass.
-- **In-sample self-deception** — judging on the data you tuned on.
-- **Symptom patching** — fixing the log line, not the mechanism.
+- Validate out of sample.
+- Fix the root cause, not the symptom.
 - **p-hacking / goalpost-moving** — tweaking variants until one randomly passes, or redefining
   "pass" after seeing the data. If nothing clears the pre-committed bar, the honest result is
   "not validated — stop," and say so plainly.
