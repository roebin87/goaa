# Ownership · Why your AI memory is 100% yours
> **Semantics**: Human (intent/concept layer · reading)

> **Purpose**: A line-by-line explanation of the five checks in `verify-ownership.py`, the two manual verifications, and the exit/migration guide.

---

## The five checks, explained line by line

### Check 1: All memory files live in a local folder

Your memory (distill, dialogue records, your profile) is stored in **this folder on your own computer** — not on some company's server.

**Meaning**: You owe no platform a "memory". Delete your account? No need — the files are local, and no one can hold them hostage.

### Check 2: Files are plain-text Markdown

Your memory is **plain text** — openable in Notepad or any editor, not a proprietary format.

**Meaning**: The format never dies. Ten years from now you can still read today's memory.

### Check 3: No remote path references

Memory files contain no references pointing to cloud/remote locations — everything lives locally.

**Meaning**: There is no hidden door where "some file actually lives on someone else's server".

### Check 4: No hardcoded absolute paths

Files contain no hardcoded paths like "C: drive on my computer" — all paths are relative.

**Meaning**: Copy the folder to any computer and it works as-is; nothing breaks because of path differences.

### Check 5: No vendor lock-in

Files contain no references tied to any specific AI vendor's interface.

**Meaning**: Whether you use WorkBuddy, Claude, Cursor, or any local AI assistant — your memory is universal. **Switch tools, and your memory stays.**

## Two manual verifications (why they're needed)

The script can only verify properties of "the files themselves". Two things must actually be done once:

1. **Offline re-run**: disconnect the network and re-run the script — confirm everything works without connectivity (empirical proof of no cloud dependency)
2. **Cross-machine migration**: copy this folder to another computer / another AI assistant and reopen it — memory is intact (empirical proof of portability)

> Once these two are done, your trust changes from "heard it" to "verified it yourself". GOAA doesn't ask you to believe — it asks you to falsify.

## Exit and migration guide (free to come and go)

Don't want to use it anymore, or want to switch tools? Three steps:

1. **Copy**: copy the whole `lite/` folder (including `_Memory/`, `identity/`) to the new location;
2. **Open**: set the folder as the workspace in the new computer / new AI assistant;
3. **Talk**: say "hello" — the AI reads your profile and distill, and continues where you left off.

> Your entire memory is these files. **There is nothing beyond them** — no cloud account, no hidden storage, no lock-in.

## FAQ

**Q: Could an AI vendor secretly save my conversations?**
A: GOAA cannot control the behavior of the AI tool you use itself. What GOAA guarantees is: **your memory system lives entirely in your own files** — even if you stop using any AI one day, these files still belong to you and remain readable.

**Q: Will this folder keep growing?**
A: Yes, but that's a good thing — it's your accumulation. Memory files are only a few KB to a few MB; plain text is very light.

---

*GOAA Lite · Ownership · Genericized concise version · 2026-08-29*
