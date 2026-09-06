# onenoun

**一个名词，激活一整套原理。**

你的 Agent Skill 里，有一部分段落在重新解释模型早就学过的东西。`onenoun`
读你自己的 Skill，判断每个这样的段落到底在讲哪一个有名字的方法，验证模型
是不是真的认识这个名字，然后用名字替换掉整段，最后用盲评消融实验证明：
改完的 Skill 没有变差。它从不碰任何事实。

**词表不是写死的。** 它只是从 30 个词起步，剩下的从你自己的文件里长出来——
不管你的文件属于哪个领域。

[English](README.md)

```sh
uvx onenoun audit  ~/.claude/skills          # 只出报告，不改任何东西
uvx onenoun prune  path/to/SKILL.md -o out/  # 写出精简版 + diff + 报告
uvx onenoun prune  path/to/SKILL.md -o out/ --keep-filler   # 只替换，不删除
uvx onenoun ablate path/to/SKILL.md out/SKILL.pruned.md -k 5   # 证明它
```

需要 [uv](https://docs.astral.sh/uv/) 和已登录的 [Claude Code](https://claude.com/claude-code)
CLI。模型调用走 `claude -p`，不用配 API key，也不会多传任何东西出去。
Sonnet 上审一个 Skill 约 $0.20，消融一次约 $2。

## 这个想法从哪来

B 站 *Build in Public*，卡比老师 Jakevin（[@jakevin7](https://x.com/jakevin7)）
的一页 *Builder Club* 幻灯片：

> **Skill 将死，方法论永生。** 一个名词，激活一整套原理：
> 第一性原理 · 对抗式审查 · 消融实验 · 奥卡姆剃刀 · 列出所有不自信的点 ·
> 保持独立思考 · 批判性思维 · 高内聚，低耦合

模型读过关于"第一性原理""消融实验"的全部文献。说出这个词，它就会照做；
你写的三段解释只花 token，不加信息。"一句顶一万句"。我是在
[Simon聊AI落地的抖音](https://www.douyin.com/note/7682301950289310693)看到这页的。
想法是他们的，工具是这个仓库。

这页幻灯片提出的是一个可以量化的判断。所以这个仓库量了一下。

## 量出来的结果

三个真实 Skill 文件，第一次运行，Sonnet，`onenoun prune`：

| skill | 是什么 | 约 token | 替换 / 删除 | 精简 |
|---|---|---|---|---|
| [continuous-improvement-loop](examples/continuous-improvement-loop) | 纯方法论 Skill，一个路径、一条命令都没有 | 1503 → 1371 | 5 METHOD, 2 FILLER | **−9%** |
| [eval-evolving](examples/eval-evolving) | 同一个 Skill 的中文版 | 1137 → 931 | 2 METHOD, 10 FILLER | **−18%** |
| [dcf-model](examples/dcf-model)（financial-analysis 插件） | 7000 词的建模规范 | 12377 → 10304 | 0 METHOD, 92 FILLER | **−17%** |

幻灯片说对了"名词"，说错了"比例"。这台机器上方法论最重的那个 Skill，
事先人工估计"约 95% 是通用内容"，模型实际回收了 9–12%（两次运行；分类器
不是确定性的）。死掉的是"重新解释"：*"按时间或留出法切分，在训练集上选参数，
在测试集上只判一次"* 变成了 **"Validate out of sample."**。活下来的，也应该
活下来的，是作者自己的决定：带数字的翻车故事、七步循环、那句 *"not validated
— stop"*。这些不在模型里。这些才是 Skill。

换成那种通篇只有端点、模型 id 和文件路径的封装类 Skill，同一条命令只改动
1% 左右。这正是应该要的结果：当文件里没有模型已经知道的东西时，守卫加分类器
会让它原样留着。工具的价值在于逐段分清这两者，不是把指到的每个文件都砍一刀。

**删完之后变差了吗？** `onenoun ablate` 根据 Skill 自己的描述生成五个任务，
每个任务分别加载原版和精简版各答一次，盲评裁判选出更好的一个（A/B 顺序随机）。

英文方法论 Skill，五个自动生成的任务，盲评：

| skill | token | 精简版赢 | 平 | 输 | 结论 |
|---|---|---|---|---|---|
| [continuous-improvement-loop](examples/continuous-improvement-loop/ablate.md) | −9% | 3 | 0 | 2 | 五五开 |
| [eval-evolving](examples/eval-evolving/ablate.md)（中文） | −18% | 1 | 0 | 4 | **精简版更差** |

用这个工具之前，先看第二行。中文那个 Skill 精简后 5 局输了 4 局。裁判说明了
原因：删掉的是用户会点名问的"反模式"清单，和最后一个任务要用的角色映射表。
出问题的不是名词替换，是删除。

所以删除和替换分成了两个开关。`--keep-filler` 只做名词替换，把所有被判为
"重复"的段落原样留下——那才是危险的一半。英文 Skill 从 −9% 变成更小的降幅，
中文 Skill 从 −18% 变成 −2%。在你自己的文件上跑一次 `ablate`，信那个，
别信这张表。

一个值得这次运行费用的副产品：分类器被要求列出所有不自信的点。在 7000 词的
DCF Skill 上，这个列表里有三处该 Skill 一直带着发布的自相矛盾：终值占比阈值
一处写 75% 一处写 80%；"只用蓝灰色"的配色规则被后面的绿红规则推翻；"仅在要求时
填色"和"默认填色方案"两句打架。工具没有改它们，只是指出了在哪。

## 怎么工作

三遍。第一遍故意不用模型。

1. **切分。** 文件切成单元。Frontmatter、标题、代码块、表格，以及任何含有
   反引号、路径、URL、环境变量、命令行参数、带单位的数字、版本号或 @提及 的
   段落，一律标为不可触碰，原样复制，不管模型怎么说。公式、数值区间、金额、
   一行的标签、引出代码块的那行，也一样。在一台机器上安装的 107 个不重复
   Skill 文件里，光这一遍就把 71% 的散文单元挡在模型之外，不花一分钱。
   `onenoun segment FILE` 显示判定，免费。

```
$ onenoun segment ~/.claude/skills/continuous-improvement-loop/SKILL.md
[  0] L1-14   frontmatter keep:frontmatter '---'
[  2] L16-16   heading     keep:heading     '# Continuous-Improvement Loop'
[  4] L18-18   paragraph   TOUCH            'A loop for shipping, then *truthfully* learning...'
[  8] L22-26   paragraph   TOUCH            'Mock/unit tests prove the code does **what you think**...'
[ 10] L28-28   paragraph   keep:lead_in     'Two failure classes this catches that mocks never will...'
[ 12] L30-32   list        TOUCH            '**Green tests, broken in production.** A streaming...'
```

2. **分类。** 可触碰的单元连同整个文件和词典一起交给模型。每个单元回来是
   **FACT**（项目特有，保留）、**METHOD** 附上它重新解释的词典术语（替换成
   术语的一行形式）、**FILLER**（文件里别处已说过，或不改变任何行为；删除）、
   或 **UNSURE**（保留，并说明原因）。规则是 *拿不准就 FACT*。METHOD 指向
   词典里没有的术语会降级为 UNSURE。替换文本来自词典，绝不来自模型，所以
   输出可复现、可审阅。
3. **消融。** 从描述生成任务，每个任务两份回答，盲评裁判，裁判自己的不确定点
   写进报告。精简版输了任何一个任务，退出码 2。`prune` 把提案写在你的文件
   旁边，不覆盖任何东西。

## 词表从你自己的文件里长出来

[`onenoun/lexicon.md`](onenoun/lexicon.md) 自带 30 个术语，但那只是**种子，
不是上限**。分类器被要求：只要你的文件在重新解释**任何一个有确立名字的方法**，
不管属于哪个领域、在不在这 30 个里面，都要把这个名字说出来。对每个新名字，
它同时写出那一行替换语，和一个**激活测试**：只含这个术语的问题，加上回答
必须命中的关键词组。

每个被提出的术语，都必须先通过它自己的测试，才允许替换任何东西。一个模型
无法仅凭名字展开的词，就不是词，不管它叫什么。通过的写进 `./onenoun-lexicon.md`
下次直接复用；没通过的，原文一个字不动，在报告里标成 CANDIDATE。

在一个从没见过这个工具的"市场进入评审" Skill 上跑
（[examples/discovery](examples/discovery)）：

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

五段解释变成五个名字。没验过的那段原样留着，两条真正的事实也留着：
拉四个财年、超授权要上报。注意 TAM/SAM/SOM 明明是模型认识的词，是它自己
生成的测试太严——这个门槛是故意偏保守的：误拒只损失一点压缩，误收会毁掉
一个 Skill。

`--no-discover` 关掉发现，只用已有术语。`onenoun lexicon check` 重跑所有
激活测试，包括学到的那些。自带的 30 个第一次跑过了 27 个；没过的三个
（对抗式审查、红队、纵深防御）回答其实是对的，是关键词列表太窄，放宽后重跑。
这是工具的"预注册"在看到结果后被调整，写在这里而不是藏起来。用 PR 提交新术语；
激活测试就是准入门槛。

## 在 Claude Code 里用

把 [`SKILL.md`](SKILL.md) 放进 `~/.claude/skills/onenoun/`，然后说
"onenoun 这个 skill"。能跑 CLI 就跑 CLI，跑不了就按同样的顺序、同样的守卫
手工做三遍。

## 在 PR 上用

[`action.yml`](action.yml) 在任何改动 Skill 文件的 PR 上评论审计表。Beta：
它在 runner 上安装 Claude Code CLI，需要 `ANTHROPIC_API_KEY` secret。

## 什么时候会更糟

- 读这个 Skill 的模型比通过激活测试的模型小。名词只能激活读者已有的东西。
- 术语在 Skill 的语言里有歧义。词典里的中文名取自幻灯片和常见用法；请核对。
- 被分类器叫作"重复"的那段散文其实在干活。这正是 `ablate` 存在的原因；读
  记录，别只看分数。
- 分类器不是确定性的。同一文件两次运行差了三个百分点。数字要紧就审两次。

## 它永远不做的事

不托管、不管 API key、不上报。不自由改写：替换文本只来自词典。不覆盖：精简版
写在你的文件旁边。不碰任何守卫单元，不管模型怎么说。

---

作者 [Jack Chew](https://github.com/jcaiagent7143-ui)，也在做
[LinkDigest](https://linkdigest.dev)，那条抖音就是这样变成我能读的文字的。MIT。
