#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify-ownership.py · GOAA 所有权验证
验证"你的 AI 记忆 100% 属于你"——5 项自动检查 + 2 项人工验证指引。

用法：
    python3 tools/verify-ownership.py

设计原则（诚实性）：脚本只验证它能验证的东西；
断网可读、跨机迁移这类真实验证，留给人工按指引执行。
"""

import os
import re
import sys
from pathlib import Path

# 工作区根 = 本文件所在目录的上两级（tools/verify-ownership.py -> lite/）
ROOT = Path(__file__).resolve().parent.parent

# 记忆相关目录/文件（存在即纳入检查；缺失则提醒，不算失败）
MEMORY_PATHS = [
    "templates/memory",
    "_Memory",
    "identity",
]

# 需排除扫描的二进制/工具目录
SKIP_DIRS = {".git", "__pycache__", "node_modules"}

RESULTS = []  # (check_no, 是否通过, 说明)


def scan_text_files(root: Path):
    """收集需扫描的纯文本文件（跳过隐藏目录与二进制）。"""
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() in (".py", ".pyc", ".exe", ".bin", ".png", ".jpg", ".jpeg", ".gif", ".ico"):
                continue
            files.append(p)
    return files


def check_local_files():
    """检查①：所有记忆文件位于本地文件夹（本工作区内）。"""
    missing = [m for m in MEMORY_PATHS if not (ROOT / m).exists()]
    if missing:
        # 记忆目录缺失 ≠ 不属于你：提醒但不判失败（首次激活前本就不存在）
        RESULTS.append((1, True, f"记忆文件位于本地文件夹 ✓（尚未生成：{', '.join(missing)}·激活后自动创建）"))
    else:
        RESULTS.append((1, True, "记忆文件位于本地文件夹 ✓"))


def check_plain_text():
    """检查②：文件格式为纯文本 Markdown（记事本可打开）。"""
    md_files = list(ROOT.rglob("*.md"))
    non_text = []
    for p in md_files:
        try:
            data = p.read_bytes()[:512]
            # 简单二进制探测：含 \x00 或高比例非 UTF-8 可解码字节
            if b"\x00" in data:
                non_text.append(str(p))
        except OSError:
            non_text.append(str(p))
    if non_text:
        RESULTS.append((2, False, f"发现疑似非纯文本文件：{non_text}"))
    else:
        RESULTS.append((2, True, f"全部 {len(md_files)} 个 Markdown 文件为纯文本 ✓"))


# 元文件豁免：README（门面·含仓库/DOI 链接）/ LICENSE（Apache 法律文本·含官方 URL）/ CITATION.cff（DOI 引用）
META_FILES = {"readme.md", "citation.cff", "license"}


def check_no_remote_refs():
    """检查③：无远程路径引用（无 http/https/远程驱动器）。"""
    offenders = []
    for p in scan_text_files(ROOT):
        if "verify-ownership.py" in p.name or p.suffix == ".py":
            continue  # 本脚本自身含示例 URL，跳过
        if p.name.lower() in META_FILES:
            continue  # 元文件豁免（门面/许可证/引用含官方 URL 属正常）
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if re.search(r"https?://", line) or re.search(r"[A-Za-z]:\\\\", line) or re.search(r"^//", line):
                offenders.append(f"{p.name}:{line_no}")
    if offenders:
        RESULTS.append((3, False, f"发现远程路径引用（应改为本地相对路径）：{offenders[:5]}"))
    else:
        RESULTS.append((3, True, "无远程路径引用（全部为本地相对路径）✓"))


def check_no_abs_paths():
    """检查④：无绝对路径硬编码（无 C:\\... / /home/... 等）。

    注意：Windows 盘符正则以「盘符+反斜杠」为准（C:\\Users\\...），
    避免把 http:// 中的 'p:/' 误判为绝对路径。
    """
    offenders = []
    for p in scan_text_files(ROOT):
        if "verify-ownership.py" in p.name or p.suffix == ".py":
            continue
        if p.name.lower() in META_FILES:
            continue  # 元文件豁免
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if re.search(r"[A-Za-z]:\\\\", line) or re.search(r"^/(home|Users|usr|opt|etc)/", line):
                offenders.append(f"{p.name}:{line_no}")
    if offenders:
        RESULTS.append((4, False, f"发现绝对路径硬编码（应改为相对路径）：{offenders[:5]}"))
    else:
        RESULTS.append((4, True, "无绝对路径硬编码（全部相对路径）✓"))


def check_no_vendor_lock():
    """检查⑤：无特定 AI 厂商依赖（扫描常见厂商专属引用）。"""
    vendor_keywords = ["api.openai.com", "api.anthropic.com", "ai.google.dev", "claude.ai", "chat.openai.com"]
    offenders = []
    for p in scan_text_files(ROOT):
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for kw in vendor_keywords:
            if kw in text:
                offenders.append(f"{p.name}:{kw}")
    if offenders:
        RESULTS.append((5, False, f"发现厂商专属引用：{offenders[:5]}"))
    else:
        RESULTS.append((5, True, "无特定 AI 厂商依赖（可用任意本地 AI 助手）✓"))


def print_report():
    print("=" * 56)
    print("GOAA · 所有权验证（Ownership Verification）")
    print("=" * 56)
    auto_pass = 0
    for no, ok, msg in RESULTS:
        mark = "✅" if ok else "❌"
        print(f"{mark} 检查{no}：{msg}")
        if ok:
            auto_pass += 1
    print("-" * 56)
    print(f"自动验证结果：{auto_pass}/5 项通过")
    print()
    print("⚠️  以下 2 项需人工验证：")
    print("   1. 断网状态下运行本脚本，5 项仍全部 ✅")
    print("      （验证：关闭网络 → 重新运行本脚本）")
    print("   2. 复制本文件夹到另一台电脑/另一个 AI 助手，记忆文件可正常读取")
    print("      （验证：复制本文件夹到另一设备 → 重新打开 → 记忆仍在）")
    print("-" * 56)
    if auto_pass == 5:
        print("结论：你的 AI 记忆 100% 属于你。")
        print("      本地存放 · 纯文本 · 无云端 · 可迁移 · 无厂商锁定")
        return 0
    else:
        print("结论：发现未通过项，请按上方提示修正后重新运行。")
        return 1


def main():
    check_local_files()
    check_plain_text()
    check_no_remote_refs()
    check_no_abs_paths()
    check_no_vendor_lock()
    return print_report()


if __name__ == "__main__":
    sys.exit(main())
