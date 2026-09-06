# Lexicon — one noun, one whole method

Each entry is a term the model was trained on so thoroughly that the term alone
activates the procedure. `replace` is the exact line the pruner writes into a
skill in place of the prose. `subsumes` lists the paraphrases that prose
usually takes. `test` and `expect` are the activation test: the model is asked
the test question with nothing else, and its answer must contain every
`expect` group (groups separated by commas; alternatives within a group by `|`;
case-insensitive). A term that fails the test is not in the model and may not
be used as a replacement. `onenoun lexicon check` runs them all.

Add a term with a PR. The test is the acceptance gate.

## first principles
- zh: 第一性原理
- replace: Reason from first principles.
- subsumes: break the problem down to what is certainly true and build up from there; do not reason by analogy or by what is usually done; question every assumption until you reach the fundamentals
- test: What does it mean to reason from first principles, as a working method? Answer in three short steps.
- expect: fundamental|basic|axiom|certainly true, assumption, analogy|build up|rebuild|from scratch

## adversarial review
- zh: 对抗式审查
- replace: Run an adversarial review of the result.
- subsumes: take the opposing side and try to break the conclusion; look for the strongest objection; assume the answer is wrong and find out why; review your own output as a hostile critic
- test: What is an adversarial review of a piece of work, as a working method? Answer in three short steps.
- expect: attack|break|hostile|opposing|adversar|critic|against, weakness|flaw|objection|counter|assumption, evidence|counterexample|revise|fix|strengthen|address|survive

## ablation
- zh: 消融实验
- replace: Ablate: remove one component at a time and measure.
- subsumes: remove one component at a time and observe what changes; keep everything else fixed; compare each variant against the baseline to see what actually contributes
- test: What does "ablation" mean as a working method for finding out which parts of a system matter? Answer in three short steps.
- expect: remove|disable|drop|knock out, one at a time|one component|each component|individually|single, baseline|compare|measure|contribut

## Occam's razor
- zh: 奥卡姆剃刀
- replace: Apply Occam's razor.
- subsumes: prefer the simplest explanation that fits the evidence; do not add components or assumptions without necessity; when two designs work, choose the one with fewer parts
- test: How do you apply Occam's razor as a working method when choosing between explanations or designs? Answer in three short steps.
- expect: simpl|fewer, assumption|entit|component, evidence|fit|explain

## list every uncertainty
- zh: 列出所有不自信的点
- replace: List every uncertainty before concluding.
- subsumes: state what you are not sure about; flag the points where you might be wrong; separate what you verified from what you inferred; do not present a guess as a fact
- test: Before delivering an answer, what does it mean to "list every uncertainty", as a working method? Answer in three short steps.
- expect: unsure|uncertain|not confident|don't know|confidence, assum|infer|guess|verif, explicit|state|flag|list|label

## independent thinking
- zh: 保持独立思考
- replace: Think independently; do not defer to the premise.
- subsumes: do not accept the framing you are given; form your own view before reading others'; do not agree just because the user or the source says so; check the premise
- test: What does "independent thinking" mean as a working discipline when you are given a question with a premise? Answer in three short steps.
- expect: premise|framing|assumption|given, own|yourself|independent, check|verify|question|evaluate

## critical thinking
- zh: 批判性思维
- replace: Apply critical thinking.
- subsumes: evaluate the evidence for each claim; distinguish fact from opinion; look for gaps, bias, and logical errors before accepting a conclusion
- test: What is critical thinking as a working method for evaluating a claim? Answer in three short steps.
- expect: evidence|support, bias|fallac|logic|gap|assumption, evaluate|assess|weigh|conclu

## high cohesion, low coupling
- zh: 高内聚，低耦合
- replace: Design for high cohesion, low coupling.
- subsumes: each module does one thing and everything inside it belongs together; modules know as little as possible about each other; a change in one place should not require changes elsewhere
- test: What does "high cohesion, low coupling" mean as a design method? Answer in three short steps.
- expect: one thing|single|related|belong|responsib, depend|know|interface|independent, change|modif|isolat

## steelman
- zh: 钢人论证
- replace: Steelman the opposing view first.
- subsumes: state the strongest version of the position you disagree with before answering it; argue the other side as well as its best advocate would
- test: What does it mean to "steelman" a position, as a working method in an argument? Answer in three short steps.
- expect: strongest|best|charitable|most persuasive, oppos|other side|disagree|counter, then|before|respond|address

## pre-registration
- zh: 预注册（先定标准，再看结果）
- replace: Pre-register the success criteria before looking at results.
- subsumes: decide the pass bar, the sample size, and the metric before seeing any results so the goalposts cannot move; write down what would count as failure in advance
- test: What is "pre-registration" as a working method for evaluating an experiment or a change? Answer in three short steps.
- expect: before|in advance|ahead|prior, criteri|metric|hypothes|threshold|bar, goalpost|bias|cherry|change|move

## root cause
- zh: 根因分析
- replace: Fix the root cause, not the symptom.
- subsumes: do not patch the log line, fix the mechanism; ask why the failure was possible, not just where it appeared; a fix that addresses only the symptom will recur
- test: What does "root cause analysis" mean as a working method when a system fails? Answer in three short steps.
- expect: symptom|surface, underlying|root|mechanism|origin|why, recur|prevent|fix|address

## single-variable change
- zh: 单变量控制
- replace: Change one variable at a time.
- subsumes: change one thing, verify, then the next; if you change several things at once you cannot attribute the effect; isolate each change
- test: What is the "change one variable at a time" method and why is it used? Answer in three short steps.
- expect: one|single, attribut|isolat|cause|which, control|constant|fixed|same

## out-of-sample validation
- zh: 样本外验证
- replace: Validate out of sample.
- subsumes: test on data that was not used to build or tune the thing; a result that only holds in-sample is overfit; hold back a set before you start
- test: What does "out-of-sample validation" mean as a working method? Answer in three short steps.
- expect: hold|unseen|not used|separate|new data|test set, overfit|generaliz|in-sample|train, evaluat|measure|test|check

## five whys
- zh: 五个为什么
- replace: Ask the five whys.
- subsumes: ask why repeatedly, each answer becoming the next question, until you reach a cause you can actually act on
- test: What is the "five whys" method? Answer in three short steps.
- expect: why, repeat|again|each|chain|five|successive, root|underlying|cause

## inversion
- zh: 逆向思维
- replace: Invert: ask what would guarantee failure.
- subsumes: instead of asking how to succeed, ask what would guarantee failure and avoid that; work backwards from the outcome you do not want
- test: What is "inversion" as a thinking method (as in Charlie Munger's "invert, always invert")? Answer in three short steps.
- expect: fail|wrong|worst|opposite|avoid, backward|reverse|instead|flip, avoid|prevent|eliminat|don't

## red team
- zh: 红队
- replace: Red-team it.
- subsumes: assign someone, or yourself in a separate pass, to attack the plan as an adversary would; find the ways it can be abused, broken, or gamed before shipping
- test: What does it mean to "red team" a plan or system, as a working method? Answer in three short steps.
- expect: attack|adversar|break|exploit|abuse, weakness|vulnerab|gap|flaw|hole|fail|assumption|edge case, fix|harden|mitigat|address|report|revise|feed

## postmortem
- zh: 复盘
- replace: Write a blameless postmortem.
- subsumes: after a failure, write down the timeline, what happened, why, what was learned and what will change; without blame; re-read it before the next cycle
- test: What is a blameless postmortem, as a working method after an incident? Answer in three short steps.
- expect: timeline|what happened|sequence|fact, cause|why|contribut, action|learn|prevent|change|follow

## principle of least astonishment
- zh: 最小惊讶原则
- replace: Follow the principle of least astonishment.
- subsumes: behave the way a user would expect; do not surprise; a name, an option, or a default should do what it looks like it does
- test: What is the "principle of least astonishment" in interface and API design? Answer in three short steps.
- expect: expect|surprise|astonish|intuit, user|caller|reader, consistent|convention|predictab|obvious

## separation of concerns
- zh: 关注点分离
- replace: Keep separation of concerns.
- subsumes: each part handles one concern; do not mix parsing with rendering with persistence; keep the layers distinct so each can change alone
- test: What does "separation of concerns" mean as a design method? Answer in three short steps.
- expect: one|single|distinct|separate, concern|responsib|aspect|layer, mix|independ|change|modular

## idempotence
- zh: 幂等
- replace: Make it idempotent.
- subsumes: running it twice must give the same result as running it once; safe to retry; check state before acting rather than assuming a clean start
- test: What does "idempotent" mean for an operation, and how do you design one? Answer in three short steps.
- expect: same|once|twice|repeat|multiple, retry|safe|rerun, state|check|exist|no effect|no change

## fail fast
- zh: 快速失败
- replace: Fail fast with a clear message.
- subsumes: check preconditions at the start and stop immediately with a clear error rather than continuing into an undefined state
- test: What is the "fail fast" principle, as a working method in software? Answer in three short steps.
- expect: early|immediat|start|precondition|upfront|as soon, error|exception|stop|abort|halt, clear|message|visible|obvious|detect

## defense in depth
- zh: 纵深防御
- replace: Apply defense in depth.
- subsumes: never rely on a single check; layer independent safeguards so one failing does not expose the system
- test: What is "defense in depth" as a security design method? Answer in three short steps.
- expect: layer|multiple|several, single|one|independent|fail, redundan|backstop|still|another|compensat|bypass|breach|compromise

## YAGNI
- zh: 你不会需要它（YAGNI）
- replace: YAGNI.
- subsumes: do not build for a need you do not have yet; add the feature when it is actually required, not when you imagine it might be
- test: What does the acronym YAGNI stand for and how is it applied? Answer in three short steps.
- expect: aren't gonna need|ain't gonna need|not going to need|not gonna need, speculat|future|might|anticipat|hypothetical, now|actual|need|require|when

## DRY
- zh: 不要重复自己（DRY）
- replace: DRY.
- subsumes: every piece of knowledge lives in one place; if you write the same thing twice, extract it; a fact stated in two places will drift
- test: What does DRY stand for in software and how is it applied? Answer in three short steps.
- expect: repeat|duplicat, single|one place|source of truth|once, extract|refactor|abstract|reuse|function

## rubber duck debugging
- zh: 小黄鸭调试法
- replace: Rubber-duck it.
- subsumes: explain the problem out loud line by line to someone who knows nothing; the act of explaining exposes the gap
- test: What is "rubber duck debugging"? Answer in three short steps.
- expect: explain|describe|talk|say, line|step|aloud|out loud|detail, realiz|notice|gap|assumption|spot|find

## Chesterton's fence
- zh: 切斯特顿的栅栏
- replace: Check Chesterton's fence before removing.
- subsumes: do not remove something until you know why it was put there; find the original reason first, then decide
- test: What is "Chesterton's fence" as a working principle before removing something? Answer in three short steps.
- expect: why|reason|purpose|put there|exist, before|first|until|understand, remove|change|delete|tear down|keep

## base rates
- zh: 基础比率
- replace: Start from the base rate.
- subsumes: before judging a specific case, ask how often this outcome happens in general; anchor on the prior, then adjust for the specifics
- test: What does it mean to use "base rates" when estimating the likelihood of an outcome? Answer in three short steps.
- expect: general|prior|reference class|how often|overall|population, specific|particular|this case|individual|detail, adjust|update|anchor|start|then

## falsifiability
- zh: 可证伪性
- replace: State what would falsify the claim.
- subsumes: say what evidence would prove this wrong; a claim that no observation could contradict is not a claim; design the test that could fail
- test: What is "falsifiability" as a working criterion for a claim or hypothesis? Answer in three short steps.
- expect: wrong|false|refut|disprov|contradict, evidence|observation|test|experiment|prediction, specific|what would|state|identify|design

## MECE
- zh: 相互独立，完全穷尽（MECE）
- replace: Make the breakdown MECE.
- subsumes: categories must not overlap and together must cover everything; no item fits two buckets, no item fits none
- test: What does MECE stand for and how do you apply it when breaking a problem down? Answer in three short steps.
- expect: mutually exclusive, collectively exhaustive, overlap|gap|cover|every

## Pareto
- zh: 二八法则
- replace: Pareto: find the 20% that gives 80%.
- subsumes: most of the effect comes from a small share of the causes; find and do that share first; do not spread effort evenly
- test: What is the Pareto principle as a working method for prioritising effort? Answer in three short steps.
- expect: 80|eighty, 20|twenty|few|small|vital, prioriti|focus|first|most|impact
