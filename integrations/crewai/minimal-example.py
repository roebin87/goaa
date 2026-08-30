#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA + CrewAI 最小集成示例
演示：GOAA 角色规则作为 CrewAI Agent 的系统提示
详见 README.md
"""

from pathlib import Path


def load_goaa_role(goaa_root, role_name):
    """从 GOAA 加载角色规则（角色定义见 mechanisms/multi-role.md）

    优先读取 multi-role.md 中的角色定义；读取失败时使用内置精简版。
    """
    multi_role = Path(goaa_root) / "mechanisms" / "multi-role.md"
    if multi_role.exists():
        text = multi_role.read_text(encoding="utf-8")
        if role_name in text:
            return text
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
        return None

    master_rules = load_goaa_role(goaa_root, "master")
    editor_rules = load_goaa_role(goaa_root, "editor")
    executor_rules = load_goaa_role(goaa_root, "executor")

    master = Agent(role="主控", goal="统筹任务，确保产出符合 GOAA 核心原则",
                    backstory=master_rules, verbose=True)
    executor = Agent(role="执行", goal="完成具体任务，生成产出",
                     backstory=executor_rules, verbose=True)
    editor = Agent(role="编辑", goal="优化产出质量，确保语言和结构符合要求",
                   backstory=editor_rules, verbose=True)

    task1 = Task(description=f"执行任务：{task}，生成初稿", agent=executor, expected_output="任务初稿")
    task2 = Task(description="优化初稿的语言和结构，确保质量", agent=editor, expected_output="优化后的定稿")

    crew = Crew(agents=[master, executor, editor], tasks=[task1, task2],
                process=Process.sequential, verbose=True)
    result = crew.kickoff()
    return result


if __name__ == "__main__":
    goaa_root = Path(__file__).resolve().parent.parent.parent
    result = run_crew(goaa_root, "写一篇关于 GOAA 多角色协作的简介")
    if result:
        print(f"\n结果：{result}")
