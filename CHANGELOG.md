# CHANGELOG

所有显著变更均记录于本文件。格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本遵循语义化版本（SemVer）。

## [v0.1.0] - 2026-08-29

### 首次发布 · GOAA 三发行版

GOAA（治理导向型 Agent 架构）v0.1.0 正式发布——治理基座 + 能力外挂。

#### 新增

- **三发行版架构**（严格真子集 Lite ⊂ Personal ⊂ Core·0 缺失）：
  - **Lite（启蒙版）**· 15 件——5 分钟验证「你的记忆属于你」·所有权验证五✅
  - **Personal（个人生产力版）**· 151 件（zh 80 + en 71）——多角色协作机制 + memory-vector 记忆向量插件 + 端到端示例×3
  - **Core（全成果开源版）**· 192 件（zh 107 + en 85）——学术论文入口 + 双链导航完整版 + 框架集成示例（LangChain/CrewAI/AutoGen）+ 治理产出案例集 + 证伪登记册 + 预注册自曝清单 + 兼容性证明 + 版本策略声明
- **en/ 英文镜像**：核心文档中英双语（concepts/constitution/mechanisms/docs 核心件）
- **证伪机制**：`docs/falsification-log.md`（9 字段登记册）+ `docs/known-limits.md`（5 维度预注册自曝清单）
- **诚实性设计**：verify-ownership.py 5 项自动 + 2 项人工验证 · memory-vector 插件零依赖双索引·无端点自动降级

#### 文档

- 根 README（仓库总门面·三版导航·决策树·证伪入口）
- 构建报告：E2 Personal / E3 Core（`docs/build-reports/`）
- 发布检查清单 RELEASE-CHECKLIST.md

#### 已知局限

完整清单见 [docs/known-limits.md](core/docs/known-limits.md)。要点：

- 核心主张（100% 人决断降低总成本等）以理论论证 + 案例为主，严格对照实验待学术线推进
- 框架集成示例为最小可运行演示（证明可集成·非生产级性能对比）
- 社区生态从零起步·社会验证（3.0 代际）待社区质疑与验证兑现
