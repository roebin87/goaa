#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
memory-vector.py · GOAA 记忆向量索引插件（可选）
=================================================
给记忆检索加"双索引"：
  - 倒排索引：关键词 → 文件映射（Python 标准库·零依赖·默认）
  - 向量索引：语义向量检索（可选·本地 embedding·OpenAI 兼容 /v1/embeddings）

设计原则（诚实性）：
  - 索引文件全部在本地（memory-index.json），不调用任何云端服务；
  - 向量索引检测不到本地 embedding 时自动降级为关键词索引并明确提示；
  - 本脚本只建立"索引"，不复制、不修改任何记忆文件本体。

用法：
  python3 memory-vector.py --build                 # 构建倒排索引
  python3 memory-vector.py --build --vector        # 构建双索引（向量可选·本地）
  python3 memory-vector.py --search "关键词"        # 关键词检索
  python3 memory-vector.py --search "关键词" --vector  # 向量检索（若已构建）
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# 工作区根 = 本文件所在目录上三级（plugins/memory-vector/memory-vector.py -> 工作区根）
ROOT = Path(__file__).resolve().parent.parent.parent

# 记忆目录（存在即纳入索引；缺失则提醒）
MEMORY_DIRS = ["_Memory", "templates/memory"]

# 索引文件（本地）
INDEX_FILE = Path(__file__).resolve().parent / "memory-index.json"

# 本地 embedding 端点（OpenAI 兼容·纯本地·默认 llama.cpp 风格）
EMBEDDING_URL = os.environ.get("EMBEDDING_URL", "http://127.0.0.1:8080/v1")

# 中文分词退化：按字符 n-gram 索引（无第三方分词器时的诚实近似）
NGRAM = 2


def collect_md_files():
    """收集记忆目录下的全部 Markdown 文件。"""
    files = []
    for d in MEMORY_DIRS:
        p = ROOT / d
        if p.exists():
            files.extend(p.rglob("*.md"))
    return sorted(set(files))


def tokenize(text):
    """零依赖分词：英文按词、中文按字符 n-gram。"""
    tokens = set()
    for m in re.finditer(r"[A-Za-z0-9_]+|[\u4e00-\u9fff]", text):
        tok = m.group(0)
        if re.fullmatch(r"[A-Za-z0-9_]+", tok):
            tokens.add(tok.lower())
        else:
            # 中文单字 + 相邻双字
            tokens.add(tok)
            for i in range(len(tok) - 1):
                tokens.add(tok[i:i + NGRAM])
    return tokens


def build_inverted(md_files):
    """构建倒排索引：词 → {文件: 词频}。"""
    index = {}
    for p in md_files:
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        toks = tokenize(text)
        for t in toks:
            d = index.setdefault(t, {})
            d[str(p)] = d.get(str(p), 0) + 1
    return index


def build_vector(md_files):
    """构建向量索引：文件 → 向量（本地 embedding·失败降级）。"""
    vectors = {}
    try:
        import urllib.request
        import json as _json

        def embed(text):
            body = _json.dumps({"input": text[:2000], "model": "local"}).encode("utf-8")
            req = urllib.request.Request(
                EMBEDDING_URL + "/embeddings",
                data=body,
                headers={"Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = _json.loads(resp.read().decode("utf-8"))
            return data["data"][0]["embedding"]

        for p in md_files:
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if text.strip():
                vectors[str(p)] = embed(text[:2000])
    except Exception as e:  # 连接失败/未安装 → 诚实降级
        print(f"[memory-vector] 向量索引不可用（{e}）→ 降级为关键词索引。")
        return None
    return vectors


def build(args):
    md_files = collect_md_files()
    if not md_files:
        print("[memory-vector] 未找到记忆文件（_Memory/ 或 templates/memory/ 为空）。先激活体系生成记忆再建索引。")
        return 1

    inverted = build_inverted(md_files)
    vectors = build_vector(md_files) if args.vector else None

    data = {
        "version": 1,
        "local_only": True,
        "files": [str(p) for p in md_files],
        "inverted": inverted,
        "vectors": vectors,
    }
    INDEX_FILE.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    n_vec = len(vectors) if vectors else 0
    print(f"[memory-vector] 索引构建完成：{len(md_files)} 个文件 · 倒排词 {len(inverted)} 个 · 向量 {n_vec} 个（本地）")
    print(f"[memory-vector] 索引文件：{INDEX_FILE}")
    return 0


def search(args):
    if not INDEX_FILE.exists():
        print("[memory-vector] 尚未构建索引。先运行：python3 memory-vector.py --build")
        return 1
    data = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    q = args.search.lower()

    if args.vector and data.get("vectors"):
        return _search_vector(data, q)
    return _search_inverted(data, q)


def _search_inverted(data, q):
    q_tokens = tokenize(q)
    scores = {}
    for t in q_tokens:
        for f, cnt in data["inverted"].get(t, {}).items():
            scores[f] = scores.get(f, 0) + cnt
    return _print_results(scores, "关键词索引")


def _search_vector(data, q):
    try:
        import urllib.request
        import json as _json

        def embed(text):
            body = _json.dumps({"input": text, "model": "local"}).encode("utf-8")
            req = urllib.request.Request(
                EMBEDDING_URL + "/embeddings", data=body,
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                return _json.loads(resp.read().decode("utf-8"))["data"][0]["embedding"]
    except Exception as e:
        print(f"[memory-vector] 本地向量端点不可用（{e}）→ 回退关键词检索。")
        return _search_inverted(data, q)

    try:
        qv = embed(q)
    except Exception as e:
        print(f"[memory-vector] 向量检索失败（{e}）→ 回退关键词检索。")
        return _search_inverted(data, q)

    scores = {}
    for f, vec in (data.get("vectors") or {}).items():
        if len(vec) == len(qv):
            dot = sum(a * b for a, b in zip(vec, qv))
            scores[f] = dot
    return _print_results(scores, "向量索引", top=10)


def _print_results(scores, kind, top=5):
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    if not ranked:
        print(f"[memory-vector] {kind}：无匹配结果。")
        return 0
    print(f"[memory-vector] {kind}命中（Top {min(top, len(ranked))}）：")
    for f, s in ranked[:top]:
        rel = Path(f).name
        print(f"  {s:.2f}  {rel}  <-  {f}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="GOAA 记忆双索引插件（本地·零云端）")
    ap.add_argument("--build", action="store_true", help="构建索引")
    ap.add_argument("--vector", action="store_true", help="构建/使用向量索引（可选）")
    ap.add_argument("--search", metavar="关键词", help="检索关键词")
    args = ap.parse_args()

    if args.build:
        return build(args)
    if args.search:
        return search(args)
    ap.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
