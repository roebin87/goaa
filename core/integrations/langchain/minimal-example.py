#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA + LangChain 最小集成示例
演示：规则前置 + 记忆后置
详见 README.md
"""

from pathlib import Path
from datetime import datetime


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


def save_to_goaa_memory(goaa_root, task, result):
    """将任务结果保存到 GOAA 记忆体系"""
    memory_dir = Path(goaa_root) / "_Memory" / "history"
    memory_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    memory_file = memory_dir / f"{timestamp}_langchain_task.md"

    content = f"# LangChain 任务记录\n\n"
    content += f"**时间**：{datetime.now().isoformat()}\n\n"
    content += f"**任务**：{task}\n\n"
    content += f"**结果**：\n{result}\n"
    memory_file.write_text(content, encoding="utf-8")
    print(f"✅ 已保存到 GOAA 记忆：{memory_file}")


def run_agent(goaa_root, task):
    """使用 GOAA 规则约束的 LangChain Agent"""
    try:
        from langchain.agents import AgentExecutor, create_react_agent
        from langchain_core.tools import tool
        from langchain_openai import ChatOpenAI
        from langchain_core.prompts import ChatPromptTemplate
    except ImportError:
        print("⚠️  请先安装依赖：pip install langchain langchain-openai")
        return None

    system_prompt = load_goaa_rules(goaa_root)
    llm = ChatOpenAI(model="gpt-4", temperature=0)

    @tool
    def search_information(query: str) -> str:
        """搜索信息"""
        return f"关于 '{query}' 的搜索结果（示例）"

    tools = [search_information]
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{input}"),
        ("agent_scratchpad", "{agent_scratchpad}"),
    ])

    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    result = agent_executor.invoke({"input": task})
    output = result["output"]
    save_to_goaa_memory(goaa_root, task, output)
    return output


if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    task = "请帮我写一篇关于 GOAA 架构的简介"
    result = run_agent(goaa_root, task)
    if result:
        print(f"\n结果：{result}")
