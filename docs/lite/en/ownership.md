# Ownership Guide · Why Your AI Memory Is 100% Yours
> **Semantics**: Human (intent/concept layer · reading)

> **Purpose**: explains the five checks of `verify-ownership.py` one by one + manual verification + exit/migration guide.

---

## The Five Checks, Explained

### ✅ Check 1: All memory files are in the local folder

Your memory (distillation, dialogue records, your profiles) lives in **this folder on your own computer** — not on some company's server.

**Meaning**: you owe no platform a "memory". Delete your account? No need — the files are local; no one can withhold them.

### ✅ Check 2: Files are plain-text Markdown

Your memory is **plain text** — Notepad or any editor can open it; it's not some software's private format.

**Meaning**: formats never die out. Ten years from now you can still read today's memory.

### ✅ Check 3: No remote path references

Memory files contain no references pointing to cloud/remote locations — everything is local.

**Meaning**: there is no hidden door where "some file actually lives on someone else's server".

### ✅ Check 4: No absolute-path hardcoding

Files contain no hard-coded paths like "drive C of my computer" — all paths are relative.

**Meaning**: copy the folder to any computer and it works as-is; nothing breaks from path differences.

### ✅ Check 5: No vendor-specific AI dependency

Files contain no references to any specific AI vendor's interfaces.

**Meaning**: whether you use WorkBuddy, Claude, Cursor, or any local AI assistant — the memory is universal. **Switch tools, the memory stays.**

## Two Manual Checks (Why Manual Verification Is Needed)

The script can only verify the file properties themselves; two things must be truly done once:

1. **Run offline**: turn off the network and rerun the script — confirm everything works without connectivity (= evidence of no cloud dependency)
2. **Cross-device migration**: copy this folder to another computer / another AI assistant and reopen — memory intact (= evidence of portability)

> Once these two are done, your trust shifts from "heard it somewhere" to "verified it myself". GOAA doesn't ask you to believe; it asks you to falsify.

## Exit & Migration Guide (Come and Go Freely)

Done with it, or switching tools? Three steps:

1. **Copy**: copy the entire `lite/` folder (including `_Memory/`, `identity/`) to a new location;
2. **Open**: set that folder as the workspace in your new computer / AI assistant;
3. **Speak**: say "hello" — the AI reads your profiles and distillation and continues where you left off.

> Your entire memory is these files. **Nothing exists beyond them** — no cloud accounts, no hidden storage, no lock-in.

## FAQ

**Q: Could an AI vendor secretly save my conversations?**
A: GOAA cannot control the behavior of the AI tool you happen to use. What GOAA guarantees is: **your memory system lives entirely in your own files** — even if you stop using any AI someday, these files still belong to you and remain readable.

**Q: Will this folder keep growing?**
A: Yes, and that's a good thing — that's your accumulation. Memory files are only a few KB to a few MB; plain text is very light.

---

*GOAA Lite · Ownership Guide · Generic concise · 2026-08-28*
