# memory-vector · Memory Vector Index Plugin (optional)

> **Purpose**: An **optional enhancement plugin** for the Personal edition — adds "dual indexing" to memory retrieval: a zero-dependency keyword inverted index by default, plus an optional local vector index.
> **Core promise**: Index files **all stay local** — no cloud service calls, no API key needed — **the ownership five checks still pass** (running `tools/verify-ownership.py` remains all-green).
> **What if I don't install it**: Nothing changes. GOAA core functions (startup/closeout/memory/multi-role) don't depend on this plugin; it only makes retrieval faster and more accurate when "memory has grown and search is slow".

---

## 1. Dual-index design

| Index | Implementation | Dependency | Default |
|-------|----------------|------------|---------|
| **Inverted index** | keyword → file mapping (memory + local JSON) | Python standard library (zero dependency) | ✅ works out of the box |
| **Vector index** | semantic vector retrieval (synonym/fuzzy recall) | local embedding (see below) | ⏸ optional |

**Why dual index**: the inverted index is fast and precise (exact keywords); the vector index excels at semantics ("that thing we talked about on architecture evolution" recalls "generational contradiction shift"). They complement each other — use inverted for daily search, vector for fuzzy recall.

## 2. Installation (three steps)

```bash
# 1. Copy the plugin into your workspace (using personal/ as example)
cp -r plugins/memory-vector /your-workspace/plugins/memory-vector

# 2. Build the index (scans memory dir _Memory/ and templates/memory/)
python3 plugins/memory-vector/memory-vector.py --build

# 3. Search
python3 plugins/memory-vector/memory-vector.py --search "rule conflict"
```

> The index file `memory-index.json` is generated inside the plugin directory — **in your local folder**, deletable and rebuildable at any time.

## 3. Enabling the vector index (optional · zero cloud)

Disabled by default. If you already have local embedding capability (e.g. a llama.cpp local service, or sentence-transformers installed), switch the vector index from `auto` to enabled:

```bash
python3 plugins/memory-vector/memory-vector.py --build --vector
```

The script detects the local embedding endpoint (environment variable `EMBEDDING_URL`, OpenAI-compatible `/v1/embeddings`, default `http://127.0.0.1:8080/v1` — a purely local address). When not detected, it **automatically degrades to the keyword index with an explicit notice** — it never silently uses the cloud.

## 4. Relationship with core mechanisms

- **Memory is still files**: this plugin only builds an "index"; it neither copies nor modifies your memory files themselves — the single authoritative source of memory remains the plain-text files in `_Memory/`;
- **Not loaded at startup**: the plugin is not in the startup sequence; call it manually on demand (keeping startup lightweight);
- **Removable anytime**: delete the plugin directory + index file and you're done — zero impact on memory files.

## 5. Honest declaration

- Keyword index: 100% local, zero dependency, works offline;
- Vector index: semantic retrieval quality depends on your local embedding model, unrelated to the GOAA system;
- This plugin **includes no cloud retrieval and collects no usage data** — consistent with the GOAA ownership axiom.

---

*GOAA · memory-vector plugin · v0.1.0 · 2026-08-29 · Genericized translation*
