#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA 收摊辅助脚本 (shutdown.py)

功能：
  1. 生成收摊报告模板（五钩结构）
  2. 备份关键治理文件到 _Memory/history/backup/
  3. 生成会话摘要框架（由 AI 助手填充内容）
  4. 检查收摊完整性

用法：
  python tools/shutdown.py [--workspace <路径>] [--backup-only]

选项：
  --workspace    指定工作区路径（默认：脚本所在目录的上一级）
  --backup-only  只执行备份，不生成报告模板

注意：
  本脚本是辅助工具，收摊的核心内容（蒸馏、日志、论语）由 AI 助手生成。
  本脚本只负责：备份文件、生成报告模板、检查完整性。
  完整的收摊五钩流程见 mechanisms/shutdown.md。
"""

import os
import sys
import argparse
import shutil
from datetime import datetime


# 需要备份的关键治理文件
BACKUP_FILES = [
    "constitution/basic_law.md",
    "constitution/design-principles.md",
    "identity/SOUL.md",
    "identity/IDENTITY.md",
    "identity/USER.md",
    "identity/主人档案.md",
    "rules/rules.yaml",
    "rules/classification.md",
    "rules/validation.md",
]

# 收摊报告模板
REPORT_TEMPLATE = """# GOAA 收摊报告

> 生成时间：{timestamp}
> 工作区：{workspace}

## 一、灵魂备份（钩 1/5）

- 备份状态：{backup_status}
- 备份文件数：{backup_count}
- 备份路径：{backup_path}

## 二、蒸馏（钩 2/5）

> 由 AI 助手生成本次会话精华，经主人确认后写入 _Memory/distill/

### 本次会话核心决策
- [ ] 待 AI 助手填充

### 本次会话关键共识
- [ ] 待 AI 助手填充

### 待办事项（下次启动需处理）
- [ ] 待 AI 助手填充

### 规则变更
- [ ] 待 AI 助手填充（如有）

### 重要记忆
- [ ] 待 AI 助手填充

## 三、日志（钩 3/5）

> 本次会话操作日志已记录到 _Memory/history/logs/

- 日志文件：{log_path}
- 状态：[ ] 待 AI 助手确认已记录

## 四、论语（钩 4/5）

> 重要决策和共识已记录到 _Memory/history/analects/（只追加不删改）

- 论语文件：{analects_path}
- 状态：[ ] 待 AI 助手确认已记录

## 五、收摊报告（钩 5/5）

### 本次会话记忆变更摘要
- [ ] 待 AI 助手填充

### 待裁决事项（如有）
- [ ] 待 AI 助手填充

### 下次启动要点
- [ ] 待 AI 助手填充

### 主人确认
- [ ] 主人已审阅本报告
- [ ] 主人确认蒸馏内容
- [ ] 主人确认收摊完成

---

*GOAA 收摊报告 · 生成于 {timestamp}*
*完整收摊流程见 mechanisms/shutdown.md*
"""


def backup_files(workspace, backup_dir):
    """备份关键治理文件"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_subdir = os.path.join(backup_dir, f"shutdown_{timestamp}")
    os.makedirs(backup_subdir, exist_ok=True)

    backed_up = 0
    for f in BACKUP_FILES:
        src = os.path.join(workspace, f)
        if os.path.isfile(src):
            # 保持目录结构
            dst = os.path.join(backup_subdir, f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            backed_up += 1

    return backed_up, backup_subdir


def generate_report(workspace, backup_count, backup_path):
    """生成收摊报告模板"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_str = datetime.now().strftime("%Y%m%d")

    log_path = f"_Memory/history/logs/session_{date_str}.md"
    analects_path = "_Memory/history/analects/analects.md"

    report = REPORT_TEMPLATE.format(
        timestamp=timestamp,
        workspace=workspace,
        backup_status="已完成" if backup_count > 0 else "未执行",
        backup_count=backup_count,
        backup_path=backup_path,
        log_path=log_path,
        analects_path=analects_path,
    )

    # 写入报告
    report_dir = os.path.join(workspace, "_Memory", "history", "shutdown-reports")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"shutdown_{date_str}.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    return report_path


def check_completeness(workspace):
    """检查收摊完整性"""
    checks = []

    # 检查蒸馏目录
    distill_dir = os.path.join(workspace, "_Memory", "distill")
    if os.path.isdir(distill_dir):
        distill_files = [f for f in os.listdir(distill_dir) if f.endswith(".md")]
        checks.append(("蒸馏层文件", f"{len(distill_files)} 个", len(distill_files) > 0))
    else:
        checks.append(("蒸馏层目录", "不存在", False))

    # 检查日志目录
    logs_dir = os.path.join(workspace, "_Memory", "history", "logs")
    if os.path.isdir(logs_dir):
        log_files = [f for f in os.listdir(logs_dir) if f.endswith(".md")]
        checks.append(("日志文件", f"{len(log_files)} 个", True))
    else:
        checks.append(("日志目录", "不存在", False))

    # 检查论语目录
    analects_dir = os.path.join(workspace, "_Memory", "history", "analects")
    if os.path.isdir(analects_dir):
        checks.append(("论语目录", "存在", True))
    else:
        checks.append(("论语目录", "不存在", False))

    return checks


def main():
    parser = argparse.ArgumentParser(description="GOAA 收摊辅助脚本")
    parser.add_argument("--workspace", default=None, help="工作区路径（默认：脚本上一级目录）")
    parser.add_argument("--backup-only", action="store_true", help="只执行备份，不生成报告")
    args = parser.parse_args()

    # 确定工作区路径
    if args.workspace:
        workspace = os.path.abspath(args.workspace)
    else:
        workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("=" * 60)
    print("GOAA 收摊辅助脚本")
    print("=" * 60)
    print(f"工作区路径: {workspace}")
    print(f"执行时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # 检查工作区
    if not os.path.isdir(workspace):
        print(f"[错误] 工作区路径不存在: {workspace}")
        sys.exit(1)

    # 钩 1：灵魂备份
    print("--- 钩 1/5：灵魂备份 ---")
    backup_dir = os.path.join(workspace, "_Memory", "history", "backup")
    backup_count, backup_path = backup_files(workspace, backup_dir)
    print(f"已备份 {backup_count} 个关键治理文件")
    print(f"备份路径: {backup_path}")
    print()

    if args.backup_only:
        print("备份模式：仅执行备份，不生成报告。")
        print()
        print("=" * 60)
        print("收摊辅助完成（备份模式）")
        print("=" * 60)
        return

    # 钩 2-5：生成报告模板
    print("--- 钩 2-5：生成收摊报告模板 ---")
    report_path = generate_report(workspace, backup_count, backup_path)
    print(f"报告模板已生成: {report_path}")
    print()
    print("注意：报告中的蒸馏、日志、论语内容需要由 AI 助手填充。")
    print("      完整收摊流程见 mechanisms/shutdown.md。")
    print()

    # 完整性检查
    print("--- 收摊完整性检查 ---")
    checks = check_completeness(workspace)
    for name, status, ok in checks:
        icon = "✓" if ok else "✗"
        print(f"  [{icon}] {name}: {status}")
    print()

    # 总结
    print("=" * 60)
    print("收摊辅助完成")
    print("=" * 60)
    print()
    print("下一步（由 AI 助手执行）：")
    print("  1. 填充收摊报告中的蒸馏内容（钩 2）")
    print("  2. 记录本次会话日志（钩 3）")
    print("  3. 记录重要决策到论语（钩 4）")
    print("  4. 主人审阅并确认收摊报告（钩 5）")
    print()
    print("完整流程见 mechanisms/shutdown.md")
    print()
    print("=" * 60)
    print("GOAA · 收摊辅助脚本 v1.0 · 2026-08-28")
    print("=" * 60)


if __name__ == "__main__":
    main()
