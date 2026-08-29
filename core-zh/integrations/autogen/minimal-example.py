#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA + AutoGen 最小集成示例
演示：规则前置 + 决断回调 + 记忆后置
详见 README.md
"""

from pathlib import Path
from datetime import datetime


def load_goaa_system_prompt(goaa_root):
    """加载 GOAA 规则作为 AssistantAgent 的系统提示"""
    basic_law = Path(goaa_root) / "constitution" / "basic_law.md"
    system = "你是受 GOAA 治理约束的 AI 助手。\n\n"
    if basic_law.exists():
        system += "## GOAA 核心原则\n" + basic_law.read_text(encoding="utf-8") + "\n\n"
    system += "关键决定请提交人侧决断，不要自主决策。"
    return system


def save_to_memory(goaa_root, conversation):
    """将对话保存到 GOAA 记忆"""
    memory_dir = Path(goaa_root) / "_Memory" / "history"
    memory_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    f = memory_dir / f"{ts}_autogen_conversation.md"
    f.write_text(f"# AutoGen 对话记录\n\n{conversation}", encoding="utf-8")
    print(f"✅ 已保存到 GOAA 记忆：{f}")


def run_autogen(goaa_root, task):
    """使用 GOAA 规则的 AutoGen 对话"""
    try:
        import autogen
    except ImportError:
        print("⚠️  请先安装 pyautogen：pip install pyautogen")
        return None

    config_list = [{"model": "gpt-4", "api_key": "YOUR_API_KEY"}]
    llm_config = {"config_list": config_list, "timeout": 120}

    assistant = autogen.AssistantAgent(
        name="GOAA_Assistant",
        system_message=load_goaa_system_prompt(goaa_root),
        llm_config=llm_config,
    )
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="ALWAYS",
        max_consecutive_auto_reply=3,
        code_execution_config=False,
    )
    user_proxy.initiate_chat(assistant, message=task)
    save_to_memory(goaa_root, str(user_proxy.chat_messages))


if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    run_autogen(goaa_root, "请帮我分析 GOAA 架构的优势和局限")
