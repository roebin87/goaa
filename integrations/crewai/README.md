# GOAA + CrewAI Integration Example
> **语义形态**：人语义（意图锚·概念解释·阅读）

> Integration example of GOAA's multi-role mechanism with the CrewAI multi-role collaboration framework.

---

## Architecture

```
┌─────────────────────────────┐
│         Human side (controller / final adjudication)   │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│    GOAA governance layer (role-rules substrate)  │
│  controller/editor/executor/reviewer role rules   │
└──────────────┬──────────────┘
               │ role-rule files
┌──────────────▼──────────────┐
│      CrewAI (multi-role execution)      │
│  Agent role definitions + task assignment     │
└─────────────────────────────┘
```

---

## Minimal Runnable Example

```python
#!/usr/bin/env python3
"""
GOAA + CrewAI minimal integration example
Demonstrates: GOAA role rules as CrewAI Agent system prompts
"""

import json
from pathlib import Path

def load_goaa_role(goaa_root, role_name):
    """Load a GOAA role rule as the Agent's backstory (falls back to a built-in concise version)"""
    role_file = Path(goaa_root) / "mechanisms" / "multi-role.md"
    if role_file.exists():
        text = role_file.read_text(encoding="utf-8")
        # Extract the role description for the given role (simplified extraction)
        for line in text.splitlines():
            if role_name in line and ("：" in line or ":" in line):
                return line.split("：", 1)[-1].split(":", 1)[-1].strip()
    roles = {
        "master": "You are the controller role: coordinate the task, assign work, and make the final decision.",
        "editor": "You are the editor role: ensure content quality, polish language, and optimize structure.",
        "executor": "You are the executor role: perform concrete operations, generate content, and write files.",
        "reviewer": "You are the reviewer role: final review, compliance check, and final confirmation.",
    }
    return roles.get(role_name, "You are an AI assistant under the GOAA architecture.")

def run_crew(goaa_root, task):
    """CrewAI multi-role collaboration using GOAA role rules"""
    try:
        from crewai import Agent, Task, Crew, Process
    except ImportError:
        print("Please install crewai first: pip install crewai")
        return

    # Load GOAA role rules
    master_rules = load_goaa_role(goaa_root, "master")
    editor_rules = load_goaa_role(goaa_root, "editor")
    executor_rules = load_goaa_role(goaa_root, "executor")

    # Define Agents (using GOAA role rules)
    master = Agent(
        role="Controller",
        goal="Coordinate the task and ensure the output complies with GOAA core principles",
        backstory=master_rules,
        verbose=True,
    )
    executor = Agent(
        role="Executor",
        goal="Complete the concrete task and generate the output",
        backstory=executor_rules,
        verbose=True,
    )
    editor = Agent(
        role="Editor",
        goal="Optimize output quality, ensure language and structure meet requirements",
        backstory=editor_rules,
        verbose=True,
    )

    # Define tasks
    task1 = Task(
        description=f"Execute the task: {task}, generate the first draft",
        agent=executor,
        expected_output="Task first draft",
    )
    task2 = Task(
        description="Optimize the first draft's language and structure, ensure quality",
        agent=editor,
        expected_output="Optimized final draft",
    )

    # Assemble the Crew (sequential execution)
    crew = Crew(
        agents=[master, executor, editor],
        tasks=[task1, task2],
        process=Process.sequential,
        verbose=True,
    )

    # Execute
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    task = "Write a brief introduction to GOAA multi-role collaboration"
    result = run_crew(goaa_root, task)
    print(f"\nResult: {result}")
```

---

## Integration Points

1. **Role-rule reuse**: GOAA's `mechanisms/multi-role.md` defines the four roles (controller/editor/executor/reviewer); the example directly uses role definitions as CrewAI Agent backstories (falls back to built-in concise versions on read failure)
2. **Controller adjudication**: in CrewAI sequential execution, the controller Agent handles final confirmation, consistent with GOAA's 100% human-decision principle
3. **Memory-last**: the Crew's output can be saved into GOAA's `_Memory/` directory, joining the memory system

---

## Prerequisites

- `pip install crewai`
- Configure an LLM API key (CrewAI uses OpenAI by default)

---

*GOAA + CrewAI Integration Example · Core Edition · 2026-08-28*
