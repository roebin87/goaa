# GOAA + AutoGen Integration Example
> **Governance strength**: L1–L2 (prompt-injection + decision callback) — see [overview](../README.md#governance-strength-levels).
> **语义形态**：人语义（意图锚·概念解释·阅读）

> Integration example of the GOAA governance substrate with Microsoft's AutoGen multi-agent dialogue framework.

---

## Architecture

```
┌─────────────────────────────┐
│      Human side (UserProxy final decision) │
└──────────────┬──────────────┘
               │
┌──────────────▼──────────────┐
│    GOAA governance layer (rules + memory substrate) │
│  constitution/rules/memory/decision callback       │
└──────────────┬──────────────┘
               │ file interface
┌──────────────▼──────────────┐
│      AutoGen (multi-agent dialogue)  │
│  AssistantAgent + UserProxy   │
└─────────────────────────────┘
```

---

## Minimal Runnable Example

```python
#!/usr/bin/env python3
"""
GOAA + AutoGen minimal integration example
Demonstrates: rules-first + decision callback + memory-last
"""

from pathlib import Path

def load_goaa_system_prompt(goaa_root):
    """Load GOAA rules as the AssistantAgent system prompt"""
    basic_law = Path(goaa_root) / "constitution" / "basic_law.md"
    system = "You are an AI assistant governed by GOAA constraints.\n\n"
    if basic_law.exists():
        system += "## GOAA Core Principles\n" + basic_law.read_text(encoding="utf-8") + "\n\n"
    system += "Submit key decisions to the human side; do not decide autonomously."
    return system

def save_to_memory(goaa_root, conversation):
    """Save the conversation into GOAA memory"""
    from datetime import datetime
    memory_dir = Path(goaa_root) / "_Memory" / "history"
    memory_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    f = memory_dir / f"{ts}_autogen_conversation.md"
    f.write_text(f"# AutoGen conversation record\n\n{conversation}", encoding="utf-8")
    print(f"Saved to GOAA memory: {f}")

def run_autogen(goaa_root, task):
    """AutoGen dialogue governed by GOAA rules"""
    try:
        import autogen
    except ImportError:
        print("Please install pyautogen first: pip install pyautogen")
        return

    config_list = [{"model": "gpt-4", "api_key": "YOUR_API_KEY"}]
    llm_config = {"config_list": config_list, "timeout": 120}

    # AssistantAgent uses the GOAA system prompt
    assistant = autogen.AssistantAgent(
        name="GOAA_Assistant",
        system_message=load_goaa_system_prompt(goaa_root),
        llm_config=llm_config,
    )

    # UserProxyAgent represents the human side (100% human decision)
    user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="ALWAYS",  # key nodes require human input
        max_consecutive_auto_reply=3,
        code_execution_config=False,
    )

    # Initiate the dialogue
    user_proxy.initiate_chat(assistant, message=task)

    # Save the conversation to memory
    conversation = str(user_proxy.chat_messages)
    save_to_memory(goaa_root, conversation)

if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    run_autogen(goaa_root, "Please analyze the strengths and limitations of the GOAA architecture")
```

---

## Integration Points

1. **Rules-first**: GOAA basic law as the AssistantAgent's `system_message`
2. **Human-side decision**: `human_input_mode="ALWAYS"` on UserProxyAgent ensures key nodes are decided by the human
3. **Memory-last**: the conversation is saved into GOAA's `_Memory/` directory after it ends
4. **Governance callback**: GOAA rule validation can be integrated into AutoGen hooks

---

## Prerequisites

- `pip install pyautogen`
- Configure an LLM API key

---

*GOAA + AutoGen Integration Example · Core Edition · 2026-08-28*
