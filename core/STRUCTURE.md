# GOAA 开源项目 · 项目结构说明（定稿 · 外部审议入口）

> **🔴 本文件定位（2026-08-19 定稿）**：本文件=开源项目**整个项目结构说明**——**外部审议的第一入口**。外部审议者（人/AI）只需读本文件，即可对项目结构做判断，无需钻入内部逐个研究。
> **🔴 同步铁律**：本文件必须与项目实际结构**始终一致**——每落地一步，同步更新本文件状态列（✅已落地/🟡待补）。结构落地以本文件为唯一对照基准。
> **版本**：唯一版本 1.0｜**状态**：结构定稿·内容逐步补写中｜**权威**：与 README 同层，README=门面（薄），本文件=结构真相（厚）。

---

## 一、项目一句话定位

GOAA 是 GOAA 治理型 Agent 架构的 2.0 工程化形态——**不解决"怎么让 AI 干活"，解决"怎么让 AI 干得可控"**：人保有 100% 决断权，文件=记忆与规则载体，三语义消解歧义。

## 二、完整结构树（与实际一一对应）

```
GOAA/
├── README.md              # 门面：为什么/特性/快速入口（薄）          ✅
├── README.en.md           # 英文门面                                 ✅
├── LICENSE                # Apache-2.0                                ✅
├── DEPLOY.md              # ★ 自举部署指令（一键部署·复制发给任意 AI） ✅
├── AGENTS.md              # AI 协作规范（对标 dsh AGENTS.md）         ✅
├── CONTRIBUTING.md        # 贡献指南                                 ✅
├── BENCHMARK.md           # 运转基准指标（架构成立=可测量）            ✅
├── SECURITY.md            # 安全政策（漏洞保密报告/响应承诺）          ✅
├── CODE_OF_CONDUCT.md     # 贡献者公约（社区行为准则）                ✅
├── CITATION.cff           # 学术引用格式（论文引用标准入口）           ✅
├── STRUCTURE.md           # 本文件=外部审议第一入口                    ✅
├── STRUCTURE.en.md        # 本文件英文版                              ✅
│
├── constitution/          # L0 宪法层（先立规矩·对应五级分类 L0）
│   ├── basic_law.md        # 基本法（母公理/存亡级/运转级/代际演进）        ✅
│   └── design-principles.md # 设计原理（Why+How 一体·公理解释+落地方法） ✅
│
├── rules/                 # 规则层（写什么·规则↔机制分置之"规则"）
│   ├── classification.md   # 五级分类                               ✅
│   ├── validation.md       # Rule Effect-Gate（写出≠生效）           ✅
│   └── rules.yaml          # ★ 编程语义实例（规则数据化·validator 可校验）✅
│
├── mechanisms/            # 机制层（怎么验·规则↔机制分置之"机制"）
│   ├── startup.md          # 启动序列                                ✅
│   ├── shutdown.md         # 收摊五钩                                ✅
│   ├── onboarding.md       # 首次激活引导                            ✅
│   ├── problem-gate.md     # 立项判定（真问题闸门）                   ✅
│   ├── ambiguity-governance.md  # 歧义治理                          ✅
│   ├── memory-loading.md        # 记忆装载规则（加载/召回/阈值/归档/防篡改）✅
│   ├── reuse.md            # 复用机制                                ✅
│   └── dynamic-rates.md    # 动态率监测                              ✅
│
├── methodologies/         # 方法论（可复用资产·机制的方法要点+指针）
│   ├── methodology-01-true-problem.md        # 真问题判定（指针→problem-gate）      ✅
│   ├── methodology-02-ambiguity-resolution.md # 歧义消解（指针→ambiguity-governance）✅
│   └── methodology-03-dynamic-rates.md       # 动态率设计（指针→dynamic-rates）      ✅
│
├── templates/             # ★ 运行时模板（部署时复制·自举缺口）
│   ├── workspace-structure.md   # 工作区目录总览（部署后身体结构）     ✅
│   ├── identity/                # 身份模板（系统三文件+档案）
│   │   ├── Agent_Profile.md     # 身份档案模板                        ✅
│   │   ├── SOUL.md              # 行为底线模板（三文件之一）           ✅
│   │   ├── IDENTITY.md          # 架构地图模板（三文件之二）           ✅
│   │   └── USER.md              # 用户档案模板（三文件之三·待填）      ✅
│   └── memory/                  # 记忆格式模板（装载分层·四层契约）
│       ├── distill.md           # 蒸馏模板                            ✅
│       ├── 灵魂备份.md           # 收摊产物格式                        ✅
│       ├── 对话记录.md           # A5 逐字格式                         ✅
│       ├── 日志.md               # 日志格式                            ✅
│       └── 论语.md               # 论语格式                            ✅
│
├── docs/                  # 深度文档（薄门户厚体系·L4 参考级）
│   ├── concepts/           # 核心概念逐篇解释（母公理/问答对偶/熵治理/三语义/证伪器/防漂移双法则）
│   │                       #   （每篇一个文件·审议者按需取读）          ✅ 6 篇
│   ├── lightweight-guide.md # 轻量化裁剪指引（标准档/极简档）          ✅
│   ├── applicability.md     # 适用边界说明（作者声明·责任）          ✅
│   ├── project-introduction.md # 项目介绍补充（外部评价/首创性自审/架构画像）✅
│   ├── comparison.md       # 与 LangGraph/AutoGen/dsh 对比（治理层独有性）✅
│   ├── internals/          # 核心机制原理（01-06·双链导航完整版 Core 全开）✅ 6 篇
│   ├── research/           # 学术论文入口（DOI·摘要·三边界声明）      ✅
│   ├── case-studies/       # 治理产出案例集（书稿/论文/开源·作者生产史）✅ 3 例
│   ├── compatibility.md    # 兼容性证明（底座立论·不替代只共存）        ✅
│   ├── falsification-log.md # 证伪登记册（社会验证证据链·Core 完整版） ✅
│   ├── known-limits.md     # 预注册自曝清单（五维度诚实披露）          ✅
│   ├── version-policy.md   # 版本策略声明（建议稿·发布前终裁）        ✅
│   └── adr/                # 架构决策记录（决策留痕）                 ✅ ADR-0001
│
├── examples/              # 示例
│   ├── project-template.md # 项目体四件套                              ✅
│   ├── activation/         # 首次激活引导（README+py+yaml）            ✅
│   └── end-to-end/         # 端到端案例（书稿/自举/压力测试）          ✅ 3 例
│
├── integrations/          # 框架集成示例（LangChain/CrewAI/AutoGen·Core 全开）✅
│   └── integration-guide.md # 通用集成指南（规则前置/记忆后置/决断回调） ✅
│
├── plugins/               # 可选能力插件
│   └── memory-vector/      # 双索引记忆检索（倒排默认·向量可选·诚实降级）✅
│
├── tools/                 # 工具（编程语义·校验/执行）
│   ├── validator.py        # 一致性校验器（部署自检·唯一工具）          ✅
│   └── verify-ownership.py # 所有权验证（5 项自动 + 2 项人工）          ✅
│
└── .github/               # CI/Issue 模板
    ├── workflows/validate.yml  # CI 校验                             ✅
    └── ISSUE_TEMPLATE/          # Issue 模板                          ✅
```

## 三、结构-原理对照（为什么这样分）

| 结构 | 2.0 原理依据 | 解决的问题 |
|------|------------|-----------|
| `constitution/` | 五级分类 L0·强制读取层 | 先立规矩 |
| `rules/`+`mechanisms/` | 规则↔机制分置（写什么 vs 怎么验） | 规则数据化可校验 |
| `rules.yaml` | 三语义之编程语义 | 规则可校验（非纯文档） |
| `templates/identity/` | L1 身份级·自举 | 系统三文件模板（自举致命缺口） |
| `templates/memory/` | 装载分层·四层契约 | 蒸馏/收摊格式（自举致命缺口） |
| `docs/adr/` | 决策留痕·防文档态自嗨 | 对标 dsh 的 ADR 仪式 |
| `BENCHMARK.md` | 验证生效原则（写出≠生效） | 架构成立=可测量 |
| `docs/concepts/` | 三语义之人语义 | 解决"别人理解不了" |
| `SECURITY.md` | 非自主公理·防利用 | 设计缺陷保密报告通道 |
| `CITATION.cff` | 学术研究命中 | 论文引用标准入口 |

## 四、外部审议指引（审议者怎么用本文件）

1. **看结构**：读本文件第二节结构树——判断层级是否清晰、职责是否分离、是否缺必要件；
2. **看状态**：读状态列（✅/🟡）——判断项目成熟度（🟡 均为"已定结构、内容待补"）；
3. **看原理**：读第三节结构-原理对照——判断每个结构是否有理论依据（无依据=冗余）；
4. **深挖按需**：需要深入某个结构时，按第二节路径取读对应文件，无需全库通读；
5. **审议输出**：给出"结构是否合理/哪些冗余/哪些缺失"的判断即可，无需研究实现细节。

## 五、补写顺序（书稿式·一章一节·每步可审议）

1. ✅ 根级仪式件（SECURITY/CODE_OF_CONDUCT/CITATION·2026-08-19）
2. ✅ templates/identity（Agent_Profile + 系统三文件·4 件·2026-08-19）
3. ✅ templates/workspace-structure + memory（6 件·2026-08-19）
4. ✅ docs/concepts（6 篇核心概念）+ lightweight-guide（2026-08-19）
5. ✅ rules.yaml（编程语义实例·2026-08-19·YAML 校验实跑 PASS）
6. ✅ docs/comparison.md（治理层独有性对照·2026-08-19）
7. ✅ docs/adr/ADR-0001（项目结构定稿·2026-08-19）
8. ✅ AGENTS.md + BENCHMARK.md（2026-08-19）
9. ✅ 英文版全量（README.en/STRUCTURE.en/SECURITY.en/CONDUCT.en/CONTRIBUTING.en/BENCHMARK.en·2026-08-19·术语表统一）

> **根级文件已全部齐备且中英双版**（README/LICENSE/DEPLOY/CONTRIBUTING/AGENTS/BENCHMARK/SECURITY/CODE_OF_CONDUCT/CITATION/STRUCTURE，各含 .en 副版）——达发布标准。

---

*GOAA 开源项目 · 项目结构说明 · 唯一版本 1.0 · 2026-08-19 · 本文件=外部审议第一入口·结构落地唯一对照基准*
