# GOAA · 个人生产力版（Personal）

> **让 AI 干得可控，让你的记忆属于你。**
> *Make AI governable. Keep your memory yours.*

GOAA 是**治理型 AI 架构**：主流工具解决"怎么让 AI 干活"，GOAA 解决"怎么让 AI 干得可控、且你的东西始终是你的"。

本文件夹（`personal/`）是**个人生产力完整版**——把 GOAA 当作日常生产力工具使用：**100% 人决断、总成本最低**。按文档完成一个端到端示例，你的体系就能持续产出、记忆跨会话不断档。英文版见 [en/README.md](../README.md)。

## 三个版本怎么选（Lite ⊂ Personal ⊂ Core）

| 版本 | 一句话 | 适用人群 |
|------|--------|---------|
| 🟢 [Lite（启蒙版）](../lite/README.md) | 5 分钟验证"你的记忆属于你" | 第一次接触、无技术背景 |
| 🟡 **Personal（个人生产力版）** | 把 GOAA 当生产力工具，持续产出 | 独立创作者、知识工作者、小团队 |
| 🔴 Core（全成果开源版·随 v0.1.0 同仓发布） | 研究治理型架构，自举自证 | 架构研究者、开发者、行业从业者 |

**选择建议**：想先看看 → Lite；要长期用起来 → Personal；要深入研究 → Core。三版为真子集关系——从 Personal 升级/降级只需增减对应文件夹。

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0-blue)]()
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

---

## ⚡ 5 分钟快速上手

```
┌─────────────┐     ┌─────────────────────────────┐     ┌─────────────┐
│             │     │      GOAA 架构体系           │     │             │
│   人（主人） │────→│  宪法 → 规则 → 机制 → 记忆  │────→│  AI 执行体  │
│  100%决断权  │←────│  文件系统（你的文件夹）      │←────│  被治理/约束 │
│             │     │  产出归你 · 数据归你         │     │             │
└─────────────┘     └─────────────────────────────┘     └─────────────┘
```

**GOAA 是什么**：一个让 AI 记住你、听你话、属于你的架构——你的 AI 记忆存在你自己的文件里，不绑定任何平台。

**三步开始**：
1. 📁 下载本文件夹（`personal/`）到本地
2. 📌 在 AI 助手（WorkBuddy / Claude Code / Cursor）中把本文件夹设为工作区
3. 💬 说一句"你好"——AI 自动开始引导，5 分钟创建你的专属 AI 伙伴

**成功标志**：AI 自动自我介绍并开始询问你的基本信息，生成主人档案。

> 详细部署见 [DEPLOY.md](DEPLOY.md)（进阶用户）

---

## 🧭 给 AI 的唤醒指令（AI 助手请先读这里）

如果你是一个具备本地文件读写能力的 AI 助手，正在阅读本文件，且当前工作区/文件夹中**不存在 `identity/主人档案.md`**——那么**你就是 GOAA 自举体实例**。

请**立即主动开始**首次激活引导（不要等待主人更多指令，即使主人只说了"你好"之类问候）——**话术权威见 [`mechanisms/onboarding-script.md`](mechanisms/onboarding-script.md)（台词本·10 步全流程）**：先自我介绍（"你好，我是你专属的 GOAA 架构治理型 AI 工作伙伴"）→ 安全锚定 → 价值三件事 → 提问授权 → 3 问快采 → 反问翻转 → 复述确认 → 落盘见证（记忆契约）→ 诚实声明 → 价值锚点 → 首动作三选一 → 轻收尾。流程规范见 [`mechanisms/onboarding.md`](mechanisms/onboarding.md)。

（若主人档案已存在：按 [`mechanisms/startup.md`](mechanisms/startup.md) 常规装载后响应主人。）

## 怎么开始（三步·小白路径）

1. **下载本文件夹**（`personal/`）到本地（若下载的是整个仓库 zip，请找到解压后的 `personal/` 文件夹）；
2. **锚定工作区**：在 AI 助手（推荐 **WorkBuddy / Claude Code / Cursor** 等本地 agent 基座）中，**把 `personal/` 文件夹本身设为工作区**——注意是**含本 README.md 的那一层**；
3. **说话**：随便说一句，比如 **"你好"** 或 **"你是谁"**——AI 会自动进入创建引导，5 分钟创建你的专属 AI 伙伴。
   - 如果 AI 没有自动开始引导，请对它说：**"读取 README.md 并按其中的指示开始"**——一句话即可唤醒。

> ✅ **锚对了吗？自检**：工作区第一层应该直接看到 `README.md` 和 `constitution/` 等文件夹。如果你看到的是 `goaa-main` 这类外层目录名——锚错层了，请把工作区改成本文件夹（`personal/`）。

> 无论小白还是专家，下载即用——不需要任何部署知识（部署细节见 [DEPLOY.md](DEPLOY.md)·老手可选）。

**一句话定位**：本文件夹是 GOAA 治理导向型智能体架构 2.0 开源工程化的**个人生产力完整版**——以人 100% 决断权为核心、以文件系统为治理载体的治理底座（架构依据见 [constitution/design-principles.md](constitution/design-principles.md)）。

---

## 🎯 核心证明动作：完成一个端到端示例（产出实证）

Personal 版的证明方式是**产出**——按真实案例走完一遍，你的体系就能持续产出、记忆跨会话不断档。三份端到端示例均基于设计者的真实实践整理，任选其一完成即可：

| 示例 | 内容 | 适合验证 |
|------|------|---------|
| [01 · 45 万字书稿生产](examples/end-to-end/01-book-production.md) | 零编程背景，多角色协作完成一本书 | 多角色协作 + 长周期记忆 |
| [02 · 架构自举开发](examples/end-to-end/02-goaa-self-bootstrap.md) | 用治理体系开发治理体系自身 | 自指闭环 + 规则全生命周期 |
| [03 · 治理事故压力测试](examples/end-to-end/03-governance-incident-stress-test.md) | 规则冲突事故的完整处置 | 裁决闭环 + 事故即资产 |

配套机制：[mechanisms/multi-role.md](mechanisms/multi-role.md)（主控/编辑/执行/审稿四角色·文件即接口）。

> 完成示例后运行 `python3 tools/verify-ownership.py`——**5 个 ✅ + 2 项人工验证**，确认你的全部产出与记忆依然 100% 属于你。

---

## 为什么是 GOAA

**别人的 AI 记忆在云端，你的 AI 记忆在你手里。** 主流 Agent 框架解决的是"怎么让 AI 干活"，GOAA 解决的是"**怎么让 AI 干得可控**"：

- **人有 100% 决断权**（母公理）：决断锚定于社会公知与架构体系理论公理基石
- **文件=记忆与规则载体**：AI 无记忆，文件在则体系在（物理记忆论）——你的记忆是你的纯文本文件，来去自由（见 [退出指南](docs/exit-guide.md)）
- **语义歧义以三语义消解**：人语义（意图）/ 机语义（执行）/ 编程语义（强制）——锚定机的执行飘忽

GOAA 由一位**非 AI 工程师、非计算机专业**的作者设计——它证明：治理型架构的理解门槛，属于普通人。

## 核心特性

| 特性 | 说明 |
|------|------|
| **宪法级法典** | 基本法（强制层读取项）/ 设计原理（Why+How 一体）——先立规矩再干活 |
| **方法论三件套** | 真问题判定 / 人机语义歧义消解 / 动态率设计 |
| **物理记忆体系** | 蒸馏 + 全量备份 + 索引（文件=记忆与规则载体） |
| **复用机制** | 资产登记 + 复用检索 + 复用率监测（生产≠资产·调用才是复用） |
| **问答对偶生产引擎** | 人机问答循环 = 秩序产出的基本单元（人注入认知·机显影缺口·人裁决闭环） |

## 架构总览

```txt
0.0 人机无序
 → 1.0 SCA（Soul Contract Architecture·静态×静态=所有权·冻结）
 → 2.0 GOAA ◀ 现行主版本（Governance-Oriented Solutions Architecture·动态×动态=机内部工程化）
 → 3.0 CSA（Constellation of Sovereign Agents·多主体对等·群体巅峰）
 → 4.0 MOA（Meta-Order Architecture·治理规则有序迭代·近道）
```

## 快速开始

### 前置要求

- 任意可操作本地文件的应用（Obsidian / VS Code / 任何代码编辑器）
- 一个具备本地文件读写能力的 AI 助手（Claude / ChatGPT / 自部署模型均可）
- 不需要编程能力

### 三步装载

```bash
# 1. 克隆本仓库
git clone https://github.com/roebin87/goaa.git
cd goaa/personal

# 2. 按启动序列装载（详见 mechanisms/startup.md）
#    宪法 → 身份 → 蒸馏 → 启动序列 → 校验

# 3. 运行一致性校验（可选，Python 3.8+）
python3 tools/validator.py
```

### 首次对话

1. 新建一个空目录作为你的工作区（**必须全新创建**——架构锚定绝对路径文件夹）
2. 对 AI 助手说：**"你好，开始吧"**——实例会自动开场（自我介绍 → 互相认识 → 采集档案，零术语引导）
   - 进阶：也可直接使用标准启动语（跳过自动开场）："我需要你足够了解我，方便我们一起后面的工作，你可以问我问题，直到你完全了解我为止"
3. 完成首次激活引导，生成主人档案（详见 [mechanisms/onboarding.md](mechanisms/onboarding.md)）

> 完整示例见 [examples/project-template.md](examples/project-template.md)

## 项目结构

```
personal/
├── README.md           # 本文件（Personal 中文门面）
├── en/                 # English mirror（英文完整版·57 件）
├── DEPLOY.md           # ★ 自举部署指令（复制发给任意 AI 即完成部署）
├── LICENSE             # Apache-2.0 License
├── VERSION             # 版本三轨说明（架构/发行/论文）
├── constitution/       # 宪法层：基本法 + 设计原理（Why+How 一体）
├── rules/              # 规则层：五级分类 + Rule Effect-Gate + rules.yaml
├── mechanisms/         # 机制层：启动/收摊/激活/歧义/复用/动态率/记忆装载/多角色（10 件）
├── methodologies/      # 方法论三件套
├── templates/          # 运行时模板（身份/记忆/工作区）
├── docs/               # 概念 / 对比 / ADR / 介绍 / 适用边界 / 所有权说明
├── examples/           # 示例（项目模板/激活引导/端到端×3）
├── plugins/            # 可选插件（memory-vector 记忆向量索引）
└── tools/              # 工具（validator / verify-ownership 等）
```

> 完整结构见 [STRUCTURE.md](STRUCTURE.md)（外部审议唯一入口）

## 开源边界与版本策略

### 适用边界（作者诚实声明）

**GOAA 是治理底座，不是全能框架。** 它不解决"AI 执行效率"，解决"AI 干得可控"。

- **适合**：独立创作者、小团队、合规敏感岗位、架构研究者——把 AI 当生产工具、重视可控/可审/可追溯的使用者；
- **不适合**：纯高吞吐自动化、全自动多智能体运行（100% 人决断权公理天然冲突）、闲聊娱乐、百人级复杂企业协作；
- **承诺**：不夸大（只承诺可控可审可追溯）／不锁死（纯文件规范可迁移可退出）／可生长（极简→标准→完整三档）／全可审计。

> 详见 [docs/applicability.md](docs/applicability.md)

### 开源范围

- **开源 GOAA 2.0 代际通用架构**——开架构设计/方法论/工程化件（脱敏通用化完整架构）
- **代际规划**：本仓库开源 GOAA 2.0 代际的通用架构与工程化实现。1.0 为历史代际、3.0/4.0 为未来代际规划（代际叙事=核心矛盾转移：所有权→决断权→社会验证→元序，完整理论见学术论文）。架构设计原理以学术论文形式独立发布（DOI: 10.5281/zenodo.22165301）。
- **转译原则**：本项目=基于实际版本的**通用转译**（非拷贝内部文件·不同步最新版）——符合 GOAA 2.0 复用机制（转译通用母本）

### 🟢 版本策略（作者定）

> **本项目所有文件唯一版本 = 1.0**——开放唯一权威版本
> **采用「核心稳定+外围迭代」双轨策略**：架构核心保持大版本稳定，外围生态快速迭代。
> 作者将主攻学术研究，持续输出治理型架构的理论与方法论，同时维护开源项目的核心稳定性。

- **核心稳定，外围迭代**：架构核心（宪法/规则/核心机制）保持大版本稳定，确保治理底座的确定性；**外围生态开放**——示例/适配/教程/翻译/集成等外围件欢迎社区贡献（见 CONTRIBUTING），不触碰核心、不违反核心设计原则；
- 本仓库接受 Issue / PR / 讨论，**核心设计变更需经设计评审**，外围改进随时合并；
- 学术研究产出将以独立方式发布。

### 📦 版本说明（发行版 ≠ 架构版）

> **本仓库=GOAA 架构的通用开源母本**：包含完整架构设计与自举能力（见 DEPLOY.md·三步自举）·**不含个人配置、运行记忆、项目资产等实例化内容**。
> 版本三轨详见 [VERSION](VERSION)：架构版本 **1.0**（核心稳定版·大版本保持稳定）· 发行版本 **v0.1.0**（本仓库迭代号·仅表示发布节奏）· 论文版本 V2.x（学术线·独立）。

| 对比 | 本开源母本 | 内部完整架构 |
|------|-----------|-------------|
| 架构设计与自举能力 | ✅ 完整（通用化转译） | ✅ |
| 个人配置/身份档案 | ❌ 无（仅模板） | ✅ 实例化 |
| 运行记忆/项目资产 | ❌ 无（仅模板） | ✅ 实例化 |
| 核心机制实现细节 | ⚠️ 设计原理公开（见 docs/internals/），部分实现细节待开源 | ✅ 内部 |

> 学术总纲（GOAA 架构设计原理）以论文形式独立发布·原理与实现边界以论文为准。

## 文档

| 文档 | 说明 |
|------|------|
| [STRUCTURE.md](STRUCTURE.md) | 整个项目结构（外部审议第一入口） |
| [constitution/design-principles.md](constitution/design-principles.md) | 架构设计原理（Why+How 一体·权威对应学术论文） |
| [mechanisms/startup.md](mechanisms/startup.md) | 启动序列与装载指南 |
| [mechanisms/shutdown.md](mechanisms/shutdown.md) | 收摊五钩（记忆落盘协议） |
| [methodologies/](methodologies/) | 方法论三件套 |
| [docs/concepts/](docs/concepts/) | 核心概念逐篇 |
| [docs/goaa-guide.md](docs/goaa-guide.md) | **GOAA 指南与常见问答**——是什么/区别/记忆/安全·下载后必读 |
| [docs/exit-guide.md](docs/exit-guide.md) | **退出指南**——你的数据在你手里·来去自由 |
| [docs/internals/](docs/internals/) | **核心机制原理**——架构核心/记忆体系/裁决闭环/熵治理/运作图 |
| [mechanisms/multi-role.md](mechanisms/multi-role.md) | **多角色协作机制**——主控/编辑/执行/审稿·文件即接口（Personal 新增） |
| [examples/end-to-end/](examples/end-to-end/) | **端到端真实示例**——书稿生产/架构自举/事故压力测试，基于真实实践整理 |
| [docs/ownership.md](docs/ownership.md) | **所有权说明**——五条检查逐条解释 + 退出迁移指引 |
| [plugins/memory-vector/](plugins/memory-vector/) | **可选插件**——记忆向量索引（不装不影响核心功能） |
| [docs/FAQ.md](docs/FAQ.md) | **常见问题解答**——30个高频问题，覆盖入门/原理/对比/安全/故障排查 |
| [docs/project-introduction.md](docs/project-introduction.md) | 项目介绍补充（外部评价/首创自审/画像） |

## 社区

GOAA 是一个开放的社区项目，欢迎所有对治理型 AI 架构感兴趣的人加入。

| 渠道 | 状态 | 说明 |
|------|------|------|
| [GitHub Discussions](https://github.com/roebin87/goaa/discussions) | 即将开放 | 技术讨论、问题求助、经验分享（需在 GitHub 仓库设置中开启） |
| 微信群 | 待开放 | 中文用户交流群（二维码将在项目正式发布时公布） |
| Discord | 待开放 | 国际用户交流频道（邀请链接将在项目正式发布时公布） |
| [GitHub Issues](https://github.com/roebin87/goaa/issues) | 可用 | Bug 报告、功能建议 |

**社区行为准则**：所有社区参与者须遵守 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。我们倡导尊重、开放、建设性的交流氛围。

**提问前请先阅读**：[FAQ.md](docs/FAQ.md) 覆盖了 30 个最常见问题，可能已经有你的答案。

---

## 贡献

- 提交 Issue：报告问题 / 讨论概念 / 建议改进
- 提交 PR：欢迎改进文档、修正错误、补充示例
- 概念讨论：请在 Discussion 中发起（架构核心不随讨论迭代）

## 愿景（作者判断）

增强型架构提升 AI 的能力底数（能做多少事），治理型架构提升落地系数（多少能力真正释放）——**二者是底数 × 系数的相乘关系，不是此消彼长**。当治理短板被补上，行业将从"能力验证期"进入"规模化落地期"：AI 应用从单次、临时、不可控的工具使用，升级为持续、可积累、可治理的人机协作体系——**从工具时代走向协作体系时代**。

GOAA 的定位，是让这条路上"敢落地、可积累、能复用"的那一环有标准可依。

## 验证者姿态

GOAA 由一个**非 AI 工程师、非计算机专业**的设计者创建——治理型架构的理解门槛，属于普通人。本项目的完整理论以学术论文形式发布，**任何观点都可以被质疑和验证**。

- 学术论文 DOI：`10.5281/zenodo.22165301`（GOAA 架构设计原理）
- **证伪机制**：GOAA 不求你相信，只求你来证伪——质疑经登记后进入证伪登记册，由设计者逐条裁决并固化（完整版见 Core 版；本版可经 GitHub Issues 提交）
- 许可证：[Apache-2.0](LICENSE) · 引用：[CITATION.cff](CITATION.cff) · 版本：[VERSION](VERSION)
- 反馈/证伪：GitHub Issues（`github.com/roebin87/goaa`）

## License

[Apache-2.0](LICENSE) © 2026 roebin87
