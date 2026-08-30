#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA 初始化脚本 (init.py)

功能：
  1. 检查 GOAA 工作区目录结构是否完整
  2. 创建缺失的必要目录和空文件
  3. 生成初始化报告

用法：
  python tools/init.py [--workspace <路径>] [--fix]

选项：
  --workspace  指定工作区路径（默认：脚本所在目录的上一级）
  --fix        自动创建缺失的目录和文件（默认只检查不修改）

注意：
  本脚本只创建目录结构和空文件，不会修改任何已有文件。
  首次激活引导请通过 AI 助手完成（说"你好"即可）。
"""

import os
import sys
import argparse
from datetime import datetime

# GOAA 必要目录结构
REQUIRED_DIRS = [
    "constitution",
    "identity",
    "rules",
    "mechanisms",
    "methodologies",
    "templates",
    "examples",
    "tools",
    "docs",
    "_Memory",
    "_Memory/distill",
    "_Memory/history",
    "_Memory/history/logs",
    "_Memory/history/analects",
    "_Memory/history/rule-archive",
    "_Memory/index",
    "_Memory/snapshot",
    "_Work",
    "_Output",
]

# GOAA 必要文件（存在性检查，不检查内容）
REQUIRED_FILES = [
    "README.md",
    "constitution/basic_law.md",
    "constitution/design-principles.md",
    "identity/SOUL.md",
    "identity/IDENTITY.md",
    "identity/USER.md",
    "rules/rules.yaml",
    "rules/classification.md",
    "rules/validation.md",
    "mechanisms/startup.md",
    "mechanisms/shutdown.md",
    "mechanisms/onboarding.md",
    "mechanisms/onboarding-script.md",
    "mechanisms/ambiguity-governance.md",
    "mechanisms/memory-loading.md",
    "mechanisms/problem-gate.md",
    "mechanisms/reuse.md",
    "tools/validator.py",
    "tools/init.py",
]

# 可选文件（存在则好，不存在也不报错）
OPTIONAL_FILES = [
    "identity/主人档案.md",
    "DEPLOY.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    "CITATION.cff",
    "VERSION",
    "AGENTS.md",
    "STRUCTURE.md",
    "BENCHMARK.md",
]


def check_directory(workspace, fix=False):
    """检查目录结构，返回缺失的目录列表"""
    missing = []
    for d in REQUIRED_DIRS:
        path = os.path.join(workspace, d)
        if not os.path.isdir(path):
            missing.append(d)
            if fix:
                os.makedirs(path, exist_ok=True)
                print(f"  [创建] {d}/")
    return missing


def check_files(workspace, fix=False):
    """检查必要文件，返回缺失的文件列表"""
    missing = []
    for f in REQUIRED_FILES:
        path = os.path.join(workspace, f)
        if not os.path.isfile(path):
            missing.append(f)
            if fix:
                # 创建空文件（仅创建，不写入内容——内容由AI助手或母本提供）
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write("")
                print(f"  [创建空文件] {f}")
    return missing


def check_optional(workspace):
    """检查可选文件，返回存在的和缺失的"""
    present = []
    absent = []
    for f in OPTIONAL_FILES:
        path = os.path.join(workspace, f)
        if os.path.isfile(path):
            present.append(f)
        else:
            absent.append(f)
    return present, absent


def main():
    parser = argparse.ArgumentParser(description="GOAA 工作区初始化检查脚本")
    parser.add_argument("--workspace", default=None, help="工作区路径（默认：脚本上一级目录）")
    parser.add_argument("--fix", action="store_true", help="自动创建缺失的目录和文件")
    args = parser.parse_args()

    # 确定工作区路径
    if args.workspace:
        workspace = os.path.abspath(args.workspace)
    else:
        # 默认：脚本所在目录的上一级（tools/ 的上一级是工作区根）
        workspace = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    print("=" * 60)
    print("GOAA 工作区初始化检查")
    print("=" * 60)
    print(f"工作区路径: {workspace}")
    print(f"检查时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"模式: {'修复模式（自动创建缺失项）' if args.fix else '检查模式（只检查不修改）'}")
    print()

    # 检查工作区是否存在
    if not os.path.isdir(workspace):
        print(f"[错误] 工作区路径不存在: {workspace}")
        sys.exit(1)

    # 检查目录
    print("--- 目录结构检查 ---")
    missing_dirs = check_directory(workspace, fix=args.fix)
    if missing_dirs:
        print(f"缺失目录: {len(missing_dirs)} 个")
        if not args.fix:
            for d in missing_dirs:
                print(f"  - {d}/")
    else:
        print("所有必要目录存在 ✓")
    print()

    # 检查文件
    print("--- 必要文件检查 ---")
    missing_files = check_files(workspace, fix=args.fix)
    if missing_files:
        print(f"缺失文件: {len(missing_files)} 个")
        if not args.fix:
            for f in missing_files:
                print(f"  - {f}")
    else:
        print("所有必要文件存在 ✓")
    print()

    # 检查可选文件
    print("--- 可选文件检查 ---")
    present_opt, absent_opt = check_optional(workspace)
    print(f"存在: {len(present_opt)} 个")
    print(f"缺失（可选）: {len(absent_opt)} 个")
    print()

    # 总结
    print("=" * 60)
    print("检查总结")
    print("=" * 60)
    total_missing = len(missing_dirs) + len(missing_files)
    if total_missing == 0:
        print("[PASS] 工作区结构完整，可以开始使用 GOAA。")
        print()
        print("下一步：")
        print("  1. 在 AI 助手中将本文件夹设为工作区")
        print("  2. 说一句'你好'，AI 会自动开始首次激活引导")
        print("  3. 跟随引导完成主人档案采集，约 5-10 分钟")
    else:
        print(f"[WARN] 发现 {total_missing} 个缺失项（目录 {len(missing_dirs)} + 文件 {len(missing_files)}）")
        if args.fix:
            print("已自动创建缺失项。建议重新运行本脚本确认。")
        else:
            print()
            print("修复方法：")
            print(f"  python tools/init.py --workspace {workspace} --fix")
            print()
            print("注意：--fix 只会创建空文件，不会写入内容。")
            print("      完整的母本文件请从 GOAA 仓库下载。")

    print()
    print("=" * 60)
    print("GOAA · 初始化脚本 v1.0 · 2026-08-28")
    print("=" * 60)


if __name__ == "__main__":
    main()
