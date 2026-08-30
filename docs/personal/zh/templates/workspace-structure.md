# 工作区目录总览（模板）—— 单轨身体结构（V2.0）
> **语义形态**：编程语义（强制可校验·执行层）

> **用途**：本文件=身体（本工作区）的目录结构总览——**单轨原则（2026-08-27 设计者裁定）：本工作区即身体**·`constitution/` `rules/` `mechanisms/` 等即身体各层·无需二次部署复制。
> **与 V1.0 差异**：V1.0 曾采用「新建第二套目录 + 复制部件」的双轨布局——已废弃；单轨=仓库即身体·激活脚本自动建 `_Memory/` 与 `identity/`。
> **填法**：`【】`内为确认项；身体层不可缺（宪法/身份/记忆）。

---

# 工作区目录总览（单轨身体）

> 身体根目录：【绝对路径，如 C:/Users/<你>/zh 或 ~/GOAA/zh】

## 目录树

```
[身体根·本工作区]              # 即下载的 zh/（或 en/）文件夹
├── README.md                  # 门面：为什么/特性/快速入口
├── AGENTS.md                  # AI 协作规范（含唤醒钩子）
├── constitution/              # 宪法层（基本法 + 设计原理·Why+How 一体）🔒只读
├── rules/                     # 规则层（写什么·五级分类/生效闸门/rules.yaml）🔒只读
├── mechanisms/                # 机制层（怎么验·启动/收摊/激活/立项/歧义）🔒只读
├── methodologies/             # 方法论层（跨情境可复用方法）🔒只读
├── examples/                  # 示例（激活引导/项目模板）✍️可参考
├── tools/                     # 工具（validator 校验器）🔒只读
├── templates/                 # 模板（identity/ 三文件·memory/ 五件）🔒只读
├── docs/                      # 文档（指南/概念/对照/退出指南）✍️可参考
├── identity/                  # 身份层（激活时自动建：三文件+主人档案）🔒只读（主人可改）
└── _Memory/                   # 记忆层（激活时自动建·四层）
    ├── distill/               # 蒸馏（跨会话接续核心·覆盖写入）✍️可覆盖（先备份）
    ├── history/               # 史书（灵魂备份/对话记录/日志·只追加）📌只追加不可删改
    ├── index/                 # 索引（MEMORY 索引/论语）✍️可覆盖
    └── snapshot/              # 快照（可选·身体级快照）✍️可覆盖
```

> **身份层/记忆层自动初始化**：首次激活时由 `examples/activation/首次激活引导.py` 自动创建（`identity/` 三文件从 `templates/identity/` 展开 + `_Memory/` 四层）·无需手工建。

### 目录权限映射（对接 validator 自动校验）

| 层级 | 权限 | 说明 |
|------|------|------|
| `constitution`/`rules`/`mechanisms`/`methodologies`/`tools`/`templates`/identity | 🔒 只读 | 系统级·Agent 不可改（修改须主人指令+留痕） |
| `_Memory/history/` | 📌 只追加 | 史书·永不删改 |
| `_Memory/distill/`、`index/` | ✍️ 可覆盖 | 覆盖前备份上一版 |
| `docs/`、`examples/` | ✍️ 参考 | 可读·建议不改（如需改走贡献流程） |

## 记忆四层契约

| 层 | 内容 | 规则 |
|----|------|------|
| 蒸馏 | 跨会话接续核心 | 覆盖写入·启动主装载 |
| 史书 | 灵魂备份/对话记录/日志 | 只追加·永不删改·存亡级 |
| 索引 | MEMORY/论语 | 索引非档案馆·精确信息读源 |

## 项目工作（可选扩展）

需要多项目并行时，可在身体根下建 `projects/`（项目四件套：全量备份/蒸馏/索引/执行）——单实例无需可省略。

## 部署核对清单（激活后）

- [ ] 身体目录树完整（constitution/rules/mechanisms/methodologies/examples/tools/templates 在位）
- [ ] `identity/` 已生成（三文件 + 主人档案）
- [ ] `_Memory/` 四层已建（distill/history/index/snapshot）
- [ ] `python3 tools/validator.py` → [PASS]
- [ ] `python3 tools/validator.py --memory` → [PASS]（首次 WARN 可接受）

---

*工作区目录总览模板（单轨版 V2.0）· 2026-08-27 设计者裁定单轨化 · 本工作区即身体*
