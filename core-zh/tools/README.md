# tools/ · 工具说明

> 本仓库为开源通用母本（核心稳定版 1.0），工具目录仅提供**开源版通用校验能力**；内部定制能力暂未开源（见下）。

## validator.py（一致性校验器·开源通用版）

**运行**：
- `python3 tools/validator.py`——核心部件校验（仓库内运行）
- `python3 tools/validator.py --memory`——**记忆健康检查**（部署区运行·检查记忆四层目录/蒸馏/档案/日志连续性——"文件既是记忆"可验证·详见 [docs/memory-guide.md](../docs/memory-guide.md)）

**开源版校验范围**：
1. **目录结构**：核心部件目录存在性（constitution/rules/mechanisms/methodologies/examples/tools）；
2. **核心文件存在性**：宪法两件 + 规则 + 机制 + 方法论 + DEPLOY.md 硬检；
3. **语义同步检查**：基本法/设计原理关键概念（决断权/公理/文件）软提示（WARN 级·不阻断）；
4. **YAML Schema 合规**：rules.yaml 必填节 + 规则 id 唯一性（FAIL 级·2026-08-26 增强）；
5. **死链/引用检查**：[Rxxx] 规则引用须有定义（FAIL 级·2026-08-26 增强）；
6. **记忆健康检查**（`--memory`）：记忆四层目录/蒸馏/主人档案/日志 + **史书层只追加哈希基线**（2026-08-26 增强）——无记忆目录时 WARN 提示（未部署场景）；
7. **输出判定**：全部硬检通过=[PASS]；有缺失=[FAIL]（附明细）。

**能力边界说明**：开源版 validator 为**通用结构校验**（任何人可独立运行·验证自举闭环）：存在性硬检+语义同步+**YAML Schema 合规+死链检查+史书只追加哈希**；内部完整版额外包含的**目录只读权限强制、规则语义深度校验**等为内部定制能力——**暂未开源**（对应架构「核心稳定版 1.0」·核心设计变更需经设计评审）。

---

## init.py（初始化检查脚本）

**功能**：检查 GOAA 工作区目录结构是否完整，创建缺失的必要目录和空文件，生成初始化报告。

**运行**：
- `python3 tools/init.py`——检查模式（只检查不修改）
- `python3 tools/init.py --fix`——修复模式（自动创建缺失的目录和空文件）
- `python3 tools/init.py --workspace <路径>`——指定工作区路径

**检查范围**：
1. 必要目录（20个）：constitution/identity/rules/mechanisms/methodologies/templates/examples/tools/docs/_Memory（四层）/_Work/_Output
2. 必要文件（20个）：README.md + 宪法两件 + 身份三件 + 规则三件 + 机制八件 + 工具两件
3. 可选文件（10个）：主人档案/DEPLOY/CONTRIBUTING/SECURITY/CODE_OF_CONDUCT/LICENSE/CITATION/VERSION/AGENTS/STRUCTURE/BENCHMARK

**注意**：`--fix` 只会创建空文件，不会写入内容。完整的母本文件请从 GOAA 仓库下载。

---

## shutdown.py（收摊辅助脚本）

**功能**：辅助执行收摊五钩——备份关键治理文件、生成收摊报告模板、检查收摊完整性。

**运行**：
- `python3 tools/shutdown.py`——完整模式（备份+生成报告+完整性检查）
- `python3 tools/shutdown.py --backup-only`——仅备份模式
- `python3 tools/shutdown.py --workspace <路径>`——指定工作区路径

**收摊五钩对应**：
1. **灵魂备份**（钩1）：自动备份宪法/身份/规则等关键治理文件到 `_Memory/history/backup/`
2. **蒸馏**（钩2）：生成报告模板，由 AI 助手填充会话精华
3. **日志**（钩3）：报告中记录日志文件路径，由 AI 助手确认
4. **论语**（钩4）：报告中记录论语文件路径，由 AI 助手确认
5. **收摊报告**（钩5）：生成完整报告模板，含记忆变更/待裁决事项/下次启动要点

**注意**：本脚本是辅助工具，收摊的核心内容（蒸馏、日志、论语）由 AI 助手生成。完整收摊流程见 [mechanisms/shutdown.md](../mechanisms/shutdown.md)。

---

## rule-conflict-check.py（规则冲突检测脚本）

**功能**：扫描 rules/ 目录下的所有规则文件，检测规则 ID 重复、相同触发条件、互斥指令、引用死链，生成冲突检测报告。

**运行**：
- `python3 tools/rule-conflict-check.py`——检测模式
- `python3 tools/rule-conflict-check.py --workspace <路径>`——指定工作区路径

**检测范围**：
1. **规则 ID 重复**：相同 ID 的规则（FAIL 级）
2. **相同触发条件**：触发条件相同的多条规则（潜在冲突·WARN 级）
3. **互斥指令**：针对同一对象的互斥指令（如"允许"vs"禁止"·启发式检测·WARN 级）
4. **引用死链**：[Rxxx] 引用指向不存在的规则（FAIL 级）

**注意**：
- 本脚本只做静态检测，不会修改规则内容
- 检测到的冲突需要由人（主人）裁决，AI 不能自行解决
- 裁决流程见 [mechanisms/ambiguity-governance.md](../mechanisms/ambiguity-governance.md)
- 互斥指令检测为启发式，非穷尽，可能漏报或误报

---

*GOAA · tools 说明 · 核心稳定版 1.0 · 2026-08-28*
