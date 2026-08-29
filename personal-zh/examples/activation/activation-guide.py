#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GOAA 首次激活引导执行器
========================
读取 首次激活引导.yaml → 身体初始化（单轨：zh/ 即身体·建 _Memory/ 四层 + 展开 identity/ 三文件）
→ 按流程逐步引导（CLI 交互）→ 生成 identity/主人档案.md（机侧只读）

用法:
    python3 首次激活引导.py                    # 默认引导流程
    python3 首次激活引导.py --dry-run          # 只展示流程不交互

设计:
    - 单轨身体（2026-08-27 设计者裁定）：本工作区即身体——激活即补齐记忆层/身份层，机制引用可闭环
    - 分层引导（C 方案）: 首次激活只采集必需项，持续补采由日常对话完成
    - 落盘产物机侧不可修改（修改权仅在人）
"""

import argparse
import datetime
import os
import sys

try:
    import yaml
except ImportError:
    print("[FAIL] 缺少 PyYAML，请先安装: pip install pyyaml")
    sys.exit(1)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(SCRIPT_DIR, "首次激活引导.yaml")
DEFAULT_TARGET = os.path.join(SCRIPT_DIR, "..", "..", "identity", "主人档案.md")


def load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ask(prompt: str, required: bool = True, hint: str = "") -> str:
    """向主人提问，收集回答。"""
    full = prompt
    if hint:
        full += f"\n  （提示：{hint}）"
    while True:
        try:
            answer = input(full + "\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n[中断] 引导中止，已收集内容不落盘。")
            sys.exit(0)
        if answer or not required:
            return answer
        print("  ⚠️ 此项必填，请回答：")


def build_profile(data: dict, frozen_note: str) -> str:
    """生成主人档案 Markdown（人语义 · 机侧只读）。"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    fields = data.get("master_series", {})
    lines = [
        "# 主人档案（机侧不可修改 · 仅主人可改）",
        "",
        f"> 本档案由首次激活引导生成（{now}）· 机侧只读 · 修改权仅在人",
        f"> {frozen_note}",
        "",
        "## 基本信息",
        "| 项 | 值 |",
        "|----|----|",
        f"| 实例名 | {data.get('agent_name', '')} |",
        f"| 主人称呼 | {fields.get('master_name', '')} |",
        "",
        "## 背景",
        fields.get("background", ""),
        "",
        "## 工作目标",
        fields.get("goals", ""),
        "",
        "## 协作偏好",
        f"- 沟通方式：{fields.get('comm_style', '')}",
        f"- 工作节奏：{fields.get('rhythm', '未说明')}",
        "",
        "## 边界与授权",
        f"- 🔴 红线（绝不能做）：{fields.get('boundaries', '')}",
        f"- ✅ 授权（可自主）：{fields.get('authorizations', '未说明')}",
        "",
        "## 补充",
        fields.get("extra", ""),
        "",
        "---",
        "*本档案持续补采：日常对话中机了解到的新偏好/习惯，由主人确认后追加至此。*",
        "",
    ]
    return "\n".join(lines)


def ensure_body(script_dir: str, dry_run: bool = False) -> dict:
    """单轨身体初始化（2026-08-27 单轨化）：
    zh/ 即身体——补齐记忆层与身份层，使机制引用（_Memory/、identity/）可闭环。
    dry_run=True 时只计算路径并展示，不落盘。
    返回 {body_root, memory_root, identity_root}。
    """
    body_root = os.path.normpath(os.path.join(script_dir, "..", ".."))  # zh/
    memory_root = os.path.join(body_root, "_Memory")
    identity_root = os.path.join(body_root, "identity")

    if dry_run:
        return {"body_root": body_root, "memory_root": memory_root, "identity_root": identity_root}

    # ① 记忆层四层（机制引用 _Memory/distill·history·index·snapshot）
    for sub in ("distill", "history", "index", "snapshot"):
        os.makedirs(os.path.join(memory_root, sub), exist_ok=True)

    # ② 身份层三文件模板展开（templates/identity/ → identity/）·已存在则不覆盖（主人可改）
    tpl_dir = os.path.join(body_root, "templates", "identity")
    if os.path.isdir(tpl_dir):
        for fname in ("SOUL.md", "IDENTITY.md", "USER.md"):
            src = os.path.join(tpl_dir, fname)
            dst = os.path.join(identity_root, fname)
            if os.path.isfile(src) and not os.path.exists(dst):
                try:
                    with open(src, "r", encoding="utf-8") as f:
                        content = f.read()
                    os.makedirs(identity_root, exist_ok=True)
                    with open(dst, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"   🧩 身份模板展开: {fname} → identity/{fname}")
                except OSError as e:
                    print(f"   ⚠️ 身份模板展开失败 {fname}: {e}")

    return {"body_root": body_root, "memory_root": memory_root, "identity_root": identity_root}


def run(config: dict, dry_run: bool = False) -> str:
    act = config["activation"]
    data = {"agent_name": "", "master_series": {}}

    # ⓪ 身体初始化（单轨·zh/ 即身体）
    body = ensure_body(SCRIPT_DIR, dry_run=dry_run)
    if dry_run:
        print(f"\n[dry-run] 身体初始化: {body['body_root']}（_Memory/ 四层 + identity/ 三文件·不落盘）")

    # ① 欢迎+自我介绍
    intro = act.get("intro", {})
    print("=" * 60)
    print(intro.get("title", "欢迎"))
    print("=" * 60)
    print(intro.get("content", ""))
    print("=" * 60)

    # ② 定名
    naming = act.get("naming", {})
    print(f"\n【第 2 步 · 定名】")
    if dry_run:
        data["agent_name"] = "（示例名）"
    else:
        data["agent_name"] = ask(naming.get("prompt", "你想怎么称呼我？"),
                                 naming.get("required", True),
                                 naming.get("hint", ""))

    # ③ 主人信息采集
    series = act.get("master_series", {})
    print(f"\n【第 3 步 · 了解主人】共 {len(series.get('fields', []))} 项（*为必填）")
    for field in series.get("fields", []):
        fname = field["field"]
        required = field.get("required", True)
        mark = "*" if required else " "
        prompt = f"[{mark}] {field['prompt']}"
        if dry_run:
            data["master_series"][fname] = "（示例回答）"
        else:
            data["master_series"][fname] = ask(prompt, required)

    # ④ 复述确认
    review = act.get("review", {})
    print(f"\n【第 4 步 · 复述确认】")
    print(review.get("prompt", ""))
    print(build_profile(data, act.get("finalize", {}).get("frozen_note", "")))
    if not dry_run:
        while True:
            ok = input("确认无误？(y/修改意见) > ").strip().lower()
            if ok in ("y", "yes", "对", "没错", "ok"):
                break
            print("  ⚠️ 当前为演示版：请直接编辑生成后的档案文件做修改；生产版将支持逐项修正。")

    # ⑤ 落盘
    finalize = act.get("finalize", {})
    target = finalize.get("target", "identity/主人档案.md")
    if dry_run:
        print(f"\n[dry-run] 将落盘至: {target}")
        return target

    # 单轨：target 相对身体根（zh/）解析（2026-08-27 修正·此前相对 SCRIPT_DIR 会误写至 examples/activation/）
    if not os.path.isabs(target):
        target = os.path.normpath(os.path.join(body["body_root"], target))
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(build_profile(data, finalize.get("frozen_note", "")))
    print(f"\n✅ 激活完成！主人档案已冻结于：{target}")
    print(f"   🔒 机侧只读：后续对话中机仅读取执行，不修改。")
    print(f"   ✏️ 主人唯一可改：直接编辑该文件即可。")
    return target


def main():
    parser = argparse.ArgumentParser(description="GOAA 首次激活引导")
    parser.add_argument("--config", default=CONFIG_PATH, help="流程定义 YAML 路径")
    parser.add_argument("--dry-run", action="store_true", help="只展示流程不交互")
    args = parser.parse_args()

    config = load_config(args.config)
    run(config, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
