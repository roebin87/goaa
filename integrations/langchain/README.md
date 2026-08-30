# GOAA + LangChain Integration Example

> Minimal integration example of GOAA as a governance substrate with LangChain.

---

## Architecture

```
┌─────────────┐
│   Human-side decision   │
└──────┬──────┘
       │
┌──────▼──────────────┐
│  GOAA governance layer (substrate)  │
│  constitution/rules/memory/decision  │
└──────┬──────────────┘
       │ file interface
┌──────▼──────────────┐
│   LangChain (capability)   │
│  Agent/tools/workflow    │
└─────────────────────┘
```

---

## Minimal Runnable Example

```python
#!/usr/bin/env python3
"""
GOAA + LangChain minimal integration example
Demonstrates: rules-first + memory-last
"""

import os
from pathlib import Path

# 1. Load GOAA rules (rules-first)
def load_goaa_rules(goaa_root):
    """Load GOAA basic law and rules as the Agent's system prompt"""
    basic_law = Path(goaa_root) / "constitution" / "basic_law.md"
    rules_yaml = Path(goaa_root) / "rules" / "rules.yaml"

    system_prompt = "You are an AI assistant governed by GOAA constraints.\n\n"
    system_prompt += "## GOAA Core Principles\n"
    if basic_law.exists():
        system_prompt += basic_law.read_text(encoding="utf-8") + "\n\n"
    system_prompt += "## Rules Configuration\n"
    if rules_yaml.exists():
        system_prompt += rules_yaml.read_text(encoding="utf-8") + "\n\n"
    system_prompt += "Execute the task under the above rules. Submit key decisions to the human side."
    return system_prompt

# 2. Save to GOAA memory (memory-last)
def save_to_goaa_memory(goaa_root, task, result):
    """Save the task result into the GOAA memory system"""
    memory_dir = Path(goaa_root) / "_Memory" / "history"
    memory_dir.mkdir(parents=True, exist_ok=True)

    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    memory_file = memory_dir / f"{timestamp}_langchain_task.md"

    content = f"# LangChain task record\n\n"
    content += f"**Time**: {datetime.now().isoformat()}\n\n"
    content += f"**Task**: {task}\n\n"
    content += f"**Result**:\n{result}\n"
    memory_file.write_text(content, encoding="utf-8")
    print(f"Saved to GOAA memory: {memory_file}")

# 3. LangChain Agent (using GOAA rules)
def run_agent(goaa_root, task):
    """A LangChain Agent constrained by GOAA rules"""
    try:
        from langchain.agents import AgentExecutor, create_react_agent
        from langchain_core.tools import tool
        from langchain_openai import ChatOpenAI
    except ImportError:
        print("Please install langchain first: pip install langchain langchain-openai")
        return

    # Load GOAA rules as the system prompt
    system_prompt = load_goaa_rules(goaa_root)

    # Initialize the model (requires an API key)
    llm = ChatOpenAI(model="gpt-4", temperature=0)

    # Define tools
    @tool
    def search_information(query: str) -> str:
        """Search for information"""
        return f"Search results for '{query}' (example)"

    tools = [search_information]

    # Create the Agent (using GOAA rules)
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}"),
    ])

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Execute the task
    result = agent_executor.invoke({"input": task})
    output = result["output"]

    # Save to GOAA memory
    save_to_goaa_memory(goaa_root, task, output)
    return output

if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    task = "Please write a brief introduction to the GOAA architecture"
    result = run_agent(goaa_root, task)
    print(f"\nResult: {result}")
```

---

## Integration Steps

1. Install dependencies: `pip install langchain langchain-openai`
2. Configure an API key (environment variable `OPENAI_API_KEY`)
3. Initialize the GOAA workspace: `python tools/init.py`
4. Run the example: `python integrations/langchain/minimal-example.py`

---

## FAQ

**Q: Will the LangChain Agent obey GOAA rules?**
A: GOAA rules are injected as the system prompt, so the Agent executes under rule constraints. But LLMs are not deterministic — for key nodes, we recommend the decision-callback pattern so the human side makes the final decision.

**Q: Can I use only memory-last without rules-first?**
A: Yes. The three integration patterns can be used independently; choose according to your needs.

---

*GOAA + LangChain Integration Example · Core Edition · 2026-08-28*
