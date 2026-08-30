#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA 一致性校验器（开源通用版）

校验核心部件文件的存在性、基本同步性与可机械验证项。
用法:
  python3 tools/validator.py           # 核心部件校验（仓库内运行）
  python3 tools/validator.py --memory  # 记忆健康检查（部署区运行·有 _Memory 的实例）
输出: [PASS] 或 [FAIL]（带明细）
"""

import os
import re
import sys

# 核心部件文件清单（存在性硬检）
CORE_FILES = [
    "docs/personal/en/constitution/basic_law.md",
    "docs/personal/en/constitution/design-principles.md",
    "docs/personal/en/rules/classification.md",
    "docs/personal/en/rules/validation.md",
    "docs/personal/en/mechanisms/startup.md",
    "docs/personal/en/mechanisms/shutdown.md",
    "docs/personal/en/mechanisms/onboarding.md",
    "docs/personal/en/mechanisms/problem-gate.md",
    "docs/personal/en/mechanisms/ambiguity-governance.md",
    "docs/personal/en/mechanisms/reuse.md",
    "docs/personal/en/mechanisms/dynamic-rates.md",
    "docs/personal/en/methodologies/methodology-01-true-problem.md",
    "docs/personal/en/methodologies/methodology-02-ambiguity-resolution.md",
    "docs/personal/en/methodologies/methodology-03-dynamic-rates.md",
    "docs/personal/en/DEPLOY.md",
]

# 必备目录（存在性硬检）
CORE_DIRS = [
    "docs/personal/en/constitution",
    "docs/personal/en/rules",
    "docs/personal/en/mechanisms",
    "docs/personal/en/methodologies",
    "examples",
    "tools",
]

# 记忆健康检查项（--memory 模式·部署区运行）
MEMORY_DIRS = [
    "_Memory/distill",
    "_Memory/history",
    "_Memory/index",
    "_Memory/snapshot",
    "_Memory/history/日志",
    "_Memory/history/对话记录",
    "_Memory/history/灵魂备份",
    "identity",
]
MEMORY_FILES = [
    "_Memory/distill/蒸馏_当前.md",
    "identity/主人档案.md",
]

# 只追加层（史书层·哈希基线校验对象）
APPEND_ONLY_DIRS = [
    "_Memory/history/日志",
    "_Memory/history/对话记录",
    "_Memory/history/灵魂备份",
]
HASH_BASELINE = "_Memory/history/.hashes.json"

def normalize(text: str) -> str:
    """归一化：去标点/空白/大小写，仅保留语义 token。"""
    text = re.sub(r"[\s\-—_·，。！？、；：\"\"''（）()[]【】]+", "", text)
    return text.lower()

def extract_tokens(text: str) -> set:
    """提取语义 token 集（简化版：按行取关键短语）。"""
    lines = text.splitlines()
    tokens = set()
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = re.split(r"[:：=]", line)
        if parts:
            tokens.add(normalize(parts[0]))
    return tokens

def check_yaml_schema(ok: list) -> bool:
    """YAML Schema 合规（轻量结构检查）：rules/rules.yaml 必填键与规则 id 唯一性。"""
    print("--- YAML Schema 合规（rules/rules.yaml）---")
    yaml_path = "docs/personal/en/rules/rules.yaml"
    if not os.path.exists(yaml_path):
        print(f"[WARN] 跳过: 未找到 {yaml_path}")
        return True
    try:
        with open(yaml_path, "r", encoding="utf-8") as fh:
            content = fh.read()
    except OSError as e:
        print(f"[WARN] 读取失败: {e}")
        return True
    required_keys = ["schema_version", "体系", "规则分级", "核心规则", "优先级"]
    missing = [k for k in required_keys if k not in content]
    if missing:
        print(f"[FAIL] rules.yaml 缺失必填节: {missing}")
        return False
    rule_ids = re.findall(r"^\s*-\s*id:\s*(R\d{3})", content, re.M)
    dup = sorted({rid for rid in rule_ids if rule_ids.count(rid) > 1})
    if dup:
        print(f"[FAIL] rules.yaml 规则 id 重复: {dup}")
        return False
    print(f"[OK]   rules.yaml 结构合规（必填节 ✓·规则 id {len(rule_ids)} 个无重复）")
    return True

def check_dead_links(ok: list) -> bool:
    """死链/引用检查：机制/规则文件中 [Rxxx] 引用须在 rules.yaml 已定义。"""
    print("--- 死链/引用检查（[Rxxx] 标准格式）---")
    yaml_path = "docs/personal/en/rules/rules.yaml"
    if not os.path.exists(yaml_path):
        print("[WARN] 跳过: 未找到 rules.yaml（无法核对规则引用）")
        return True
    with open(yaml_path, "r", encoding="utf-8") as fh:
        content = fh.read()
    defined = set(re.findall(r"^\s*-\s*id:\s*(R\d{3})", content, re.M))
    if not defined:
        print("[WARN] rules.yaml 未解析到规则 id（引用检查降级为跳过）")
        return True
    scan_targets = [
        "docs/personal/en/rules/validation.md", "docs/personal/en/rules/classification.md",
        "mechanisms", "docs/personal/en/constitution/design-principles.md",
    ]
    ref_pattern = re.compile(r"\[(R\d{3})\]")
    dangling = []
    total = 0
    for base in scan_targets:
        if os.path.isfile(base):
            files = [base]
        elif os.path.isdir(base):
            files = [os.path.join(base, f) for f in os.listdir(base) if f.endswith(".md")]
        else:
            continue
        for f in files:
            try:
                with open(f, "r", encoding="utf-8") as fh:
                    text = fh.read()
            except OSError:
                continue
            for m in ref_pattern.finditer(text):
                total += 1
                if m.group(1) not in defined:
                    dangling.append(f"{f}: {m.group(0)}")
    if dangling:
        print(f"[FAIL] 悬空规则引用 {len(dangling)} 处:")
        for d in dangling[:10]:
            print(f"       {d}")
        return False
    print(f"[OK]   规则引用 {total} 处全部有定义")
    return True

def check_append_only(ok: list) -> bool:
    """只追加检测（史书层哈希基线）：--memory 模式·对比 .hashes.json 基线，防已落盘史书被改。"""
    print("--- 只追加检测（史书层哈希基线）---")
    baseline_path = HASH_BASELINE
    import json, hashlib
    current = {}
    for d in APPEND_ONLY_DIRS:
        if not os.path.isdir(d):
            continue
        for root, _, files in os.walk(d):
            for f in files:
                if f == ".hashes.json":
                    continue
                p = os.path.join(root, f)
                try:
                    with open(p, "rb") as fh:
                        current[p] = hashlib.sha256(fh.read()).hexdigest()[:16]
                except OSError:
                    continue
    if not current:
        print("[WARN] 史书层为空或未部署（无只追加文件·跳过）")
        return True
    if os.path.exists(baseline_path):
        try:
            with open(baseline_path, "r", encoding="utf-8") as fh:
                base = json.load(fh)
        except (OSError, ValueError):
            base = {}
    else:
        base = {}
    tampered = [p for p, h in current.items() if p in base and base[p] != h]
    if tampered:
        print(f"[FAIL] 史书层文件被修改（违反只追加）: {tampered[:5]}")
        return False
    try:
        with open(baseline_path, "w", encoding="utf-8") as fh:
            json.dump(current, fh, ensure_ascii=False, indent=1)
    except OSError as e:
        print(f"[WARN] 基线写入失败（仅本次比对生效）: {e}")
    print(f"[OK]   只追加层 {len(current)} 个文件哈希基线一致")
    return True

def memory_check() -> int:
    """记忆健康检查：记忆四层目录/核心记忆文件存在性 + 史书只追加哈希（无记忆目录=WARN 非 FAIL）。"""
    print("=== GOAA 记忆健康检查（--memory）===")
    ok = True
    if not os.path.isdir("_Memory"):
        print("[WARN] 未发现 _Memory 目录——当前可能未部署/未生成记忆（本检查应在部署区运行）")
        return 0
    for d in MEMORY_DIRS:
        if os.path.isdir(d):
            print(f"[OK]   记忆目录: {d} ✓")
        else:
            print(f"[WARN] 记忆目录缺失: {d}（未生成该层·可接受）")
    for f in MEMORY_FILES:
        if os.path.exists(f):
            print(f"[OK]   记忆文件: {f} ✓")
        else:
            print(f"[WARN] 记忆文件缺失: {f}（首次激活后生成）")
    if not check_append_only(ok):
        ok = False
    if ok:
        print("[PASS] 记忆健康检查通过")
    return 0 if ok else 1

def main() -> int:
    if "--memory" in sys.argv:
        return memory_check()

    print("=== GOAA 核心部件校验器 ===")
    ok = True

    # 目录检查
    for d in CORE_DIRS:
        if os.path.isdir(d):
            print(f"[OK]   目录: {d} ✓")
        else:
            print(f"[FAIL] 缺失目录: {d}")
            ok = False

    # 文件存在性检查
    for f in CORE_FILES:
        if os.path.exists(f):
            print(f"[OK]   文件: {f} ✓")
        else:
            print(f"[FAIL] 缺失文件: {f}")
            ok = False

    # 宪法层基本同步（basic_law 核心条款 vs design-principles 核心概念）
    try:
        with open("docs/personal/en/constitution/basic_law.md", "r", encoding="utf-8") as fh:
            law = fh.read()
        with open("docs/personal/en/constitution/design-principles.md", "r", encoding="utf-8") as fh:
            prin = fh.read()
        key_terms = ["decision rights", "axioms", "files"]
        for term in key_terms:
            if term.lower() in law.lower() and term.lower() in prin.lower():
                print(f"[OK]   semantic sync: basic_law/design-principles contain '{term}' ✓")
            else:
                print(f"[WARN] semantic drift: '{term}' not found in both basic_law and design-principles")
    except OSError as e:
        print(f"[WARN] 宪法同步检查跳过: {e}")

    # YAML Schema 合规
    if not check_yaml_schema(ok):
        ok = False

    # 死链/引用检查
    if not check_dead_links(ok):
        ok = False

    if ok:
        print("[PASS] 核心部件校验通过：目录 ✓ + 文件 ✓ + Schema ✓ + 引用 ✓")
        return 0
    else:
        print("[FAIL] 存在缺失项，请补齐后重跑")
        return 1

if __name__ == "__main__":
    sys.exit(main())
