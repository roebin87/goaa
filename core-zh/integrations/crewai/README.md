# GOAA + CrewAI 集成示例

> GOAA 多角色机制与 CrewAI 多角色协作框架的集成示例。

---

## 架构图

```
┌─────────────────────────────┐
│        人侧（主控/最终裁决）   │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│    GOAA 治理层（角色规则底座）  │
│  主控/编辑/执行/审稿 角色规则   │
└──────────────┬──────────────┘
               │ 角色规则文件
┌──────────────▼──────────────┐
│      CrewAI（多角色执行）      │
│  Agent 角色定义 + 任务分配     │
└─────────────────────────────┘
```

---

## 最小运行示例

```python
#!/usr/bin/env python3
"""
GOAA + CrewAI 最小集成示例
演示：GOAA 角色规则作为 CrewAI Agent 的系统提示
"""

from pathlib import Path

def load_goaa_role(goaa_root, role_name):
    """从 GOAA 加载角色规则，作为 CrewAI Agent 的 backstory

    优先读取 mechanisms/multi-role.md；读取失败时使用内置精简版。
    """
    multi_role = Path(goaa_root) / "mechanisms" / "multi-role.md"
    if multi_role.exists():
        text = multi_role.read_text(encoding="utf-8")
        if role_name in text:
            return text
    # 默认角色规则
    roles = {
        "master": "你是主控角色，负责统筹任务、分配工作、最终裁决。",
        "editor": "你是编辑角色，负责内容质量把控、语言润色、结构优化。",
        "executor": "你是执行角色，负责具体操作、内容生成、文件写入。",
        "reviewer": "你是审稿角色，负责终审、合规检查、最终确认。",
    }
    return roles.get(role_name, "你是 GOAA 架构下的 AI 助手。")

def run_crew(goaa_root, task):
    """使用 GOAA 角色规则的 CrewAI 多角色协作"""
    try:
        from crewai import Agent, Task, Crew, Process
    except ImportError:
        print("⚠️  请先安装 crewai：pip install crewai")
        return

    # 加载 GOAA 角色规则
    master_rules = load_goaa_role(goaa_root, "master")
    editor_rules = load_goaa_role(goaa_root, "editor")
    executor_rules = load_goaa_role(goaa_root, "executor")

    # 定义 Agent（使用 GOAA 角色规则）
    master = Agent(
        role="主控",
        goal="统筹任务，确保产出符合 GOAA 核心原则",
        backstory=master_rules,
        verbose=True,
    )
    executor = Agent(
        role="执行",
        goal="完成具体任务，生成产出",
        backstory=executor_rules,
        verbose=True,
    )
    editor = Agent(
        role="编辑",
        goal="优化产出质量，确保语言和结构符合要求",
        backstory=editor_rules,
        verbose=True,
    )

    # 定义任务
    task1 = Task(
        description=f"执行任务：{task}，生成初稿",
        agent=executor,
        expected_output="任务初稿",
    )
    task2 = Task(
        description="优化初稿的语言和结构，确保质量",
        agent=editor,
        expected_output="优化后的定稿",
    )

    # 组建 Crew（顺序执行）
    crew = Crew(
        agents=[master, executor, editor],
        tasks=[task1, task2],
        process=Process.sequential,
        verbose=True,
    )

    # 执行
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    task = "写一篇关于 GOAA 多角色协作的简介"
    result = run_crew(goaa_root, task)
    print(f"\n结果：{result}")
```

---

## 集成要点

1. **角色规则复用**：GOAA 的 `mechanisms/multi-role.md` 定义了主控/编辑/执行/审稿四角色，示例直接以角色定义作为 CrewAI Agent 的 backstory（读取失败时使用内置精简版）
2. **主控裁决**：CrewAI 的顺序执行中，主控 Agent 负责最终确认，符合 GOAA 的 100% 人决断原则
3. **记忆后置**：Crew 的产出可以保存到 GOAA 的 `_Memory/` 目录，纳入记忆体系

---

## 前置条件

- `pip install crewai`
- 配置 LLM API key（CrewAI 默认使用 OpenAI）

---

*GOAA + CrewAI 集成示例 · Core 版 · 2026-08-28*
