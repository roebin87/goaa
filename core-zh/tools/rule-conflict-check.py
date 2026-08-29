#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA 规则冲突检测脚本 (rule-conflict-check.py)

功能：
  1. 扫描 rules/ 目录下的所有规则文件
  2. 检测规则 ID 重复
  3. 检测相同触发条件的规则（潜在冲突）
  4. 检测互斥指令的规则（潜在冲突）
  5. 检测规则引用死链
  6. 生成冲突检测报告

用法：
  python tools/rule-conflict-check.py [--workspace <路径>] [--fix]

选项：
  --workspace  指定工作区路径（默认：脚本所在目录的上一级）
  --fix        自动修复可修复的问题（如规则 ID 重复时重命名）

注意：
  本脚本只做静态检测，不会修改规则内容。
  --fix 模式只会重命名重复的规则 ID，不会修改规则逻辑。
  检测到的冲突需要由人（主人）裁决，AI 不能自行解决。
"""

import os
import sys
import argparse
import re
import yaml
from datetime import datetime
from collections import defaultdict


def load_rules(workspace):
    """加载所有规则文件"""
    rules_dir = os.path.join(workspace, "rules")
    if not os.path.isdir(rules_dir):
        print(f"[错误] 规则目录不存在: {rules_dir}")
        return []

    rules = []
    for filename in os.listdir(rules_dir):
        if filename.endswith(".yaml") or filename.endswith(".yml"):
            filepath = os.path.join(rules_dir, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    # 尝试解析 YAML
                    data = yaml.safe_load(content)
                    if data and "rules" in data:
                        for rule in data["rules"]:
                            rule["_source_file"] = filename
                            rules.append(rule)
                    elif data and isinstance(data, list):
                        for rule in data:
                            rule["_source_file"] = filename
                            rules.append(rule)
            except Exception as e:
                print(f"[警告] 解析规则文件失败 {filename}: {e}")

    return rules


def check_duplicate_ids(rules):
    """检测规则 ID 重复"""
    id_map = defaultdict(list)
    for rule in rules:
        rule_id = rule.get("id", "UNKNOWN")
        id_map[rule_id].append(rule)

    duplicates = {rid: rlist for rid, rlist in id_map.items() if len(rlist) > 1}
    return duplicates


def check_same_triggers(rules):
    """检测相同触发条件的规则"""
    trigger_map = defaultdict(list)
    for rule in rules:
        trigger = rule.get("trigger", "")
        if trigger:
            trigger_map[trigger].append(rule)

    conflicts = {trig: rlist for trig, rlist in trigger_map.items() if len(rlist) > 1}
    return conflicts


def check_mutex_instructions(rules):
    """检测互斥指令的规则（简单启发式）"""
    # 互斥关键词对（简单启发式，非穷尽）
    mutex_pairs = [
        ("允许", "禁止"),
        ("可以", "不可以"),
        ("必须", "不得"),
        ("enable", "disable"),
        ("allow", "deny"),
        ("must", "must not"),
    ]

    conflicts = []
    for i, rule1 in enumerate(rules):
        for rule2 in rules[i+1:]:
            instr1 = rule1.get("instruction", "") + rule1.get("action", "")
            instr2 = rule2.get("instruction", "") + rule2.get("action", "")

            for pos, neg in mutex_pairs:
                if (pos in instr1 and neg in instr2) or (neg in instr1 and pos in instr2):
                    # 进一步检查是否针对同一对象
                    obj1 = rule1.get("target", "") + rule1.get("scope", "")
                    obj2 = rule2.get("target", "") + rule2.get("scope", "")
                    if obj1 and obj2 and (obj1 in obj2 or obj2 in obj1 or obj1 == obj2):
                        conflicts.append((rule1, rule2, pos, neg))

    return conflicts


def check_dead_references(rules):
    """检测规则引用死链"""
    all_ids = set(rule.get("id", "") for rule in rules)
    dead_refs = []

    ref_pattern = re.compile(r'\[R(\d+)\]')

    for rule in rules:
        # 检查规则描述中的引用
        for field in ["description", "instruction", "action", "notes"]:
            content = rule.get(field, "")
            if isinstance(content, str):
                refs = ref_pattern.findall(content)
                for ref in refs:
                    ref_id = f"R{ref}"
                    if ref_id not in all_ids:
                        dead_refs.append((rule.get("id", "UNKNOWN"), ref_id, field))

        # 检查规则的 references 字段
        if "references" in rule:
            for ref in rule["references"]:
                if ref not in all_ids:
                    dead_refs.append((rule.get("id", "UNKNOWN"), ref, "references"))

    return dead_refs


def generate_report(workspace, duplicates, trigger_conflicts, mutex_conflicts, dead_refs):
    """生成冲突检测报告"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = []
    report.append("# GOAA 规则冲突检测报告")
    report.append("")
    report.append(f"> 检测时间：{timestamp}")
    report.append(f"> 工作区：{workspace}")
    report.append("")

    # 总结
    total_issues = len(duplicates) + len(trigger_conflicts) + len(mutex_conflicts) + len(dead_refs)
    report.append("## 检测总结")
    report.append("")
    report.append(f"| 检测项 | 问题数 |")
    report.append(f"|--------|--------|")
    report.append(f"| 规则 ID 重复 | {len(duplicates)} |")
    report.append(f"| 相同触发条件 | {len(trigger_conflicts)} |")
    report.append(f"| 互斥指令 | {len(mutex_conflicts)} |")
    report.append(f"| 引用死链 | {len(dead_refs)} |")
    report.append(f"| **总计** | **{total_issues}** |")
    report.append("")

    if total_issues == 0:
        report.append("**[PASS] 未检测到规则冲突。**")
        report.append("")
    else:
        report.append("**[WARN] 检测到规则冲突，请人工裁决。**")
        report.append("")
        report.append("> 注意：规则冲突不能由 AI 自行解决，必须提交裁决循环，由人（主人）最终决策。")
        report.append("> 裁决流程见 mechanisms/ambiguity-governance.md")
        report.append("")

    # 详细报告
    if duplicates:
        report.append("## 一、规则 ID 重复")
        report.append("")
        for rid, rlist in duplicates.items():
            report.append(f"### 重复 ID: {rid}")
            report.append("")
            for rule in rlist:
                report.append(f"- 文件: {rule.get('_source_file', '?')}")
                report.append(f"  描述: {rule.get('description', '无描述')[:80]}")
            report.append("")

    if trigger_conflicts:
        report.append("## 二、相同触发条件（潜在冲突）")
        report.append("")
        for trig, rlist in trigger_conflicts.items():
            report.append(f"### 触发条件: {trig[:80]}")
            report.append("")
            for rule in rlist:
                report.append(f"- ID: {rule.get('id', '?')} | 文件: {rule.get('_source_file', '?')}")
                report.append(f"  指令: {rule.get('instruction', rule.get('action', '无'))[:80]}")
            report.append("")

    if mutex_conflicts:
        report.append("## 三、互斥指令（潜在冲突）")
        report.append("")
        for rule1, rule2, pos, neg in mutex_conflicts:
            report.append(f"### {rule1.get('id', '?')} vs {rule2.get('id', '?')}")
            report.append("")
            report.append(f"- 规则1 ({rule1.get('_source_file', '?')}): {rule1.get('instruction', rule1.get('action', ''))[:80]}")
            report.append(f"- 规则2 ({rule2.get('_source_file', '?')}): {rule2.get('instruction', rule2.get('action', ''))[:80]}")
            report.append(f"- 互斥关键词: {pos} / {neg}")
            report.append("")

    if dead_refs:
        report.append("## 四、引用死链")
        report.append("")
        for rule_id, ref_id, field in dead_refs:
            report.append(f"- 规则 {rule_id} 的 {field} 字段引用了不存在的规则 {ref_id}")
        report.append("")

    report.append("---")
    report.append("")
    report.append("*GOAA 规则冲突检测报告 · 生成于 " + timestamp + "*")
    report.append("*裁决流程见 mechanisms/ambiguity-governance.md*")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="GOAA 规则冲突检测脚本")
    parser.add_argument("--workspace", default=None, help="工作区路径（默认：脚本上一级目录）")
    parser.add_argument("--fix", action="store_true", help="自动修复可修复的问题（规则 ID 重命名）")
    args = parser.parse_args()

    # 确定工作区路径
    if args.workspace:
        workspace = os.path.abspath(args.workspace)
    else:
        workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("=" * 60)
    print("GOAA 规则冲突检测")
    print("=" * 60)
    print(f"工作区路径: {workspace}")
    print(f"检测时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 加载规则
    print("--- 加载规则文件 ---")
    rules = load_rules(workspace)
    print(f"已加载 {len(rules)} 条规则")
    print()

    if not rules:
        print("[警告] 未加载到任何规则，可能是规则目录为空或格式不正确。")
        print()
        print("=" * 60)
        print("检测完成（无规则可检测）")
        print("=" * 60)
        return

    # 检测
    print("--- 执行检测 ---")
    duplicates = check_duplicate_ids(rules)
    print(f"  规则 ID 重复: {len(duplicates)}")

    trigger_conflicts = check_same_triggers(rules)
    print(f"  相同触发条件: {len(trigger_conflicts)}")

    mutex_conflicts = check_mutex_instructions(rules)
    print(f"  互斥指令: {len(mutex_conflicts)}")

    dead_refs = check_dead_references(rules)
    print(f"  引用死链: {len(dead_refs)}")
    print()

    # 生成报告
    report = generate_report(workspace, duplicates, trigger_conflicts, mutex_conflicts, dead_refs)

    # 写入报告
    report_dir = os.path.join(workspace, "_Memory", "history", "rule-checks")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"rule-conflict-{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"--- 检测报告 ---")
    print(f"报告已保存: {report_path}")
    print()

    # 总结
    total_issues = len(duplicates) + len(trigger_conflicts) + len(mutex_conflicts) + len(dead_refs)
    print("=" * 60)
    if total_issues == 0:
        print("[PASS] 未检测到规则冲突。")
    else:
        print(f"[WARN] 检测到 {total_issues} 个潜在问题。")
        print()
        print("注意：规则冲突不能由 AI 自行解决，必须提交裁决循环。")
        print("裁决流程见 mechanisms/ambiguity-governance.md")
    print("=" * 60)
    print()
    print("GOAA · 规则冲突检测脚本 v1.0 · 2026-08-28")


if __name__ == "__main__":
    main()
