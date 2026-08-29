# GOAA + AutoGen 集成示例

> GOAA 治理底座与微软 AutoGen 多 Agent 对话框架的集成示例。

---

## 架构图

```
┌─────────────────────────────┐
│     人侧（UserProxy 最终决断） │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│    GOAA 治理层（规则+记忆底座） │
│  宪法/规则/记忆/决断回调       │
└──────────────┬──────────────┘
               │ 文件接口
┌──────────────▼──────────────┐
│      AutoGen（多 Agent 对话）  │
│  AssistantAgent + UserProxy   │
└─────────────────────────────┘
```

---

## 最小运行示例

```python
#!/usr/bin/env python3
"""
GOAA + AutoGen 最小集成示例
演示：规则前置 + 决断回调 + 记忆后置
"""

from pathlib import Path

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
    from datetime import datetime
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
        return

    config_list = [{"model": "gpt-4", "api_key": "YOUR_API_KEY"}]
    llm_config = {"config_list": config_list, "timeout": 120}

    # AssistantAgent 使用 GOAA 系统提示
    assistant = autogen.AssistantAgent(
        name="GOAA_Assistant",
        system_message=load_goaa_system_prompt(goaa_root),
        llm_config=llm_config,
    )

    # UserProxyAgent 代表人侧（100% 人决断）
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="ALWAYS",  # 关键节点需要人输入
        max_consecutive_auto_reply=3,
        code_execution_config=False,
    )

    # 发起对话
    user_proxy.initiate_chat(assistant, message=task)

    # 保存对话到记忆
    conversation = str(user_proxy.chat_messages)
    save_to_memory(goaa_root, conversation)

if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    run_autogen(goaa_root, "请帮我分析 GOAA 架构的优势和局限")
```

---

## 集成要点

1. **规则前置**：GOAA 基本法作为 AssistantAgent 的 system_message
2. **人侧决断**：UserProxyAgent 的 `human_input_mode="ALWAYS"` 确保关键节点由人决断
3. **记忆后置**：对话结束后保存到 GOAA `_Memory/` 目录
4. **治理回调**：可以在 AutoGen 的 hook 中集成 GOAA 规则验证

---

## 前置条件

- `pip install pyautogen`
- 配置 LLM API key

---

*GOAA + AutoGen 集成示例 · Core 版 · 2026-08-28*
