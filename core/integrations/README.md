# GOAA 框架集成示例

> GOAA 作为治理底座，与主流增强型 Agent 框架的集成示例。

---

## 集成总览

GOAA 不替代任何增强型框架，而是作为治理底座与它们共存：

| 框架 | 定位 | 集成模式 | 示例路径 |
|------|------|---------|---------|
| **LangChain** | 最主流的 Python Agent 框架 | 规则前置 + 记忆后置 | [`langchain/`](langchain/) |
| **CrewAI** | 多角色协作框架 | 多角色规则基础 | [`crewai/`](crewai/) |
| **AutoGen** | 微软多 Agent 对话框架 | 治理 + 记忆底座 | [`autogen/`](autogen/) |

---

## 通用集成模式

所有框架集成都遵循以下三种模式（可单独或组合使用）：

### 模式一：规则前置
Agent 在执行任务前，读取 GOAA 的 `constitution/basic_law.md` 和 `rules/rules.yaml`，在规则约束下执行。

### 模式二：记忆后置
Agent 完成任务后，将产出和过程写入 GOAA 的 `_Memory/` 目录，纳入 GOAA 的记忆体系。

### 模式三：决断回调
Agent 遇到规则未覆盖的关键节点时，暂停执行，将选项提交给 GOAA 治理层，由人侧决断后继续。

---

## 每个示例包含

- `README.md`：集成说明、架构图、最小运行示例
- `minimal-example.py`：最小可运行代码
- `integration-guide.md`：集成步骤、接口说明、常见问题

---

## 前置条件

所有集成示例需要：
- Python 3.8+
- GOAA 工作区已初始化（`python tools/init.py`）
- 对应框架的 Python SDK（`pip install langchain` / `pip install crewai` / `pip install pyautogen`）

---

## 一句话总结

**GOAA 为所有增强型框架提供治理底座，治理基座 + 能力外挂 = 最优 Agent 架构方向。**

---

*GOAA 框架集成示例 · Core 版 · 2026-08-28*
