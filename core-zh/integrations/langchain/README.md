# GOAA + LangChain 集成示例

> GOAA 作为治理底座，与 LangChain 的最小集成示例。

---

## 架构图

```
┌─────────────┐
│   人侧决断    │
└──────┬──────┘
       │
┌──────▼──────────────┐
│  GOAA 治理层（底座）  │
│  宪法/规则/记忆/决断  │
└──────┬──────────────┘
       │ 文件接口
┌──────▼──────────────┐
│   LangChain（能力）   │
│  Agent/工具/工作流    │
└─────────────────────┘
```

---

## 最小运行示例

```python
#!/usr/bin/env python3
"""
GOAA + LangChain 最小集成示例
演示：规则前置 + 记忆后置
"""

import os
from pathlib import Path

# 1. 加载 GOAA 规则（规则前置）
def load_goaa_rules(goaa_root):
    """加载 GOAA 基本法和规则，作为 Agent 的系统提示词"""
    basic_law = Path(goaa_root) / "constitution" / "basic_law.md"
    rules_yaml = Path(goaa_root) / "rules" / "rules.yaml"

    system_prompt = "你是一个受 GOAA 治理约束的 AI 助手。\n\n"
    system_prompt += "## GOAA 核心原则\n"
    if basic_law.exists():
        system_prompt += basic_law.read_text(encoding="utf-8") + "\n\n"
    system_prompt += "## 规则配置\n"
    if rules_yaml.exists():
        system_prompt += rules_yaml.read_text(encoding="utf-8") + "\n\n"
    system_prompt += "请在上述规则约束下执行任务。关键决定请提交人侧决断。"
    return system_prompt

# 2. 保存到 GOAA 记忆（记忆后置）
def save_to_goaa_memory(goaa_root, task, result):
    """将任务结果保存到 GOAA 记忆体系"""
    memory_dir = Path(goaa_root) / "_Memory" / "history"
    memory_dir.mkdir(parents=True, exist_ok=True)

    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    memory_file = memory_dir / f"{timestamp}_langchain_task.md"

    content = f"# LangChain 任务记录\n\n"
    content += f"**时间**：{datetime.now().isoformat()}\n\n"
    content += f"**任务**：{task}\n\n"
    content += f"**结果**：\n{result}\n"
    memory_file.write_text(content, encoding="utf-8")
    print(f"✅ 已保存到 GOAA 记忆：{memory_file}")

# 3. LangChain Agent（使用 GOAA 规则）
def run_agent(goaa_root, task):
    """使用 GOAA 规则约束的 LangChain Agent"""
    try:
        from langchain.agents import AgentExecutor, create_react_agent
        from langchain_core.tools import tool
        from langchain_openai import ChatOpenAI
    except ImportError:
        print("⚠️  请先安装 langchain：pip install langchain langchain-openai")
        return

    # 加载 GOAA 规则作为系统提示
    system_prompt = load_goaa_rules(goaa_root)

    # 初始化模型（需要配置 API key）
    llm = ChatOpenAI(model="gpt-4", temperature=0)

    # 定义工具
    @tool
    def search_information(query: str) -> str:
        """搜索信息"""
        return f"关于 '{query}' 的搜索结果（示例）"

    tools = [search_information]

    # 创建 Agent（使用 GOAA 规则）
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}"),
    ])

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 执行任务
    result = agent_executor.invoke({"input": task})
    output = result["output"]

    # 保存到 GOAA 记忆
    save_to_goaa_memory(goaa_root, task, output)
    return output

if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    task = "请帮我写一篇关于 GOAA 架构的简介"
    result = run_agent(goaa_root, task)
    print(f"\n结果：{result}")
```

---

## 集成步骤

1. 安装依赖：`pip install langchain langchain-openai`
2. 配置 API key（环境变量 `OPENAI_API_KEY`）
3. 初始化 GOAA 工作区：`python tools/init.py`
4. 运行示例：`python integrations/langchain/minimal-example.py`

---

## 常见问题

**Q：LangChain Agent 会遵守 GOAA 规则吗？**
A：GOAA 规则作为系统提示词注入，Agent 会在规则约束下执行。但大模型不是确定性的，关键节点建议使用决断回调模式，由人侧最终决断。

**Q：可以只使用记忆后置，不使用规则前置吗？**
A：可以。三种集成模式可单独使用，根据你的需求选择。

---

*GOAA + LangChain 集成示例 · Core 版 · 2026-08-28*
