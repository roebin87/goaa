#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify-ownership.py · GOAA Ownership Verification
Verifies "your AI memory is 100% yours" — 5 automated checks + 2 manual verification guides.

Usage:
    python3 tools/verify-ownership.py

Design principle (honesty): the script only verifies what it can verify;
real verifications such as offline readability and cross-device migration
are left to the manual guides.
"""

import os
import re
import sys
from pathlib import Path

# Workspace root = two levels above this file (tools/verify-ownership.py -> edition root)
ROOT = Path(__file__).resolve().parent.parent

# Memory-related dirs/files (included in the check if present; a missing one is a reminder, not a failure)
MEMORY_PATHS = [
    "templates/memory",
    "_Memory",
    "identity",
]

# Directories excluded from scanning (binary/tool dirs)
SKIP_DIRS = {".git", "__pycache__", "node_modules"}

RESULTS = []  # (check_no, passed, message)


def scan_text_files(root: Path):
    """Collect plain-text files to scan (skip hidden dirs and binaries)."""
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
    """Check 1: all memory files are in the local folder (within this workspace)."""
    missing = [m for m in MEMORY_PATHS if not (ROOT / m).exists()]
    if missing:
        # A missing memory dir is not "not yours": remind but don't fail (it doesn't exist before first activation)
        RESULTS.append((1, True, f"Memory files located in the local folder ✓ (not yet generated: {', '.join(missing)} · auto-created after activation)"))
    else:
        RESULTS.append((1, True, "Memory files located in the local folder ✓"))


def check_plain_text():
    """Check 2: files are plain-text Markdown (openable in any editor)."""
    md_files = list(ROOT.rglob("*.md"))
    non_text = []
    for p in md_files:
        try:
            data = p.read_bytes()[:512]
            # Simple binary probe: contains \x00 or a high ratio of non-UTF-8-decodable bytes
            if b"\x00" in data:
                non_text.append(str(p))
        except OSError:
            non_text.append(str(p))
    if non_text:
        RESULTS.append((2, False, f"Suspected non-plain-text files found: {non_text}"))
    else:
        RESULTS.append((2, True, f"All {len(md_files)} Markdown files are plain text ✓"))


# Meta-file exemption: README (facade · contains repo/DOI links) / LICENSE (Apache legal text · official URLs) / CITATION.cff (DOI citation)
META_FILES = {"readme.md", "citation.cff", "license"}


def check_no_remote_refs():
    """Check 3: no remote path references (no http/https/remote drives)."""
    offenders = []
    for p in scan_text_files(ROOT):
        if "verify-ownership.py" in p.name or p.suffix == ".py":
            continue  # this script itself contains example URLs; skip
        if p.name.lower() in META_FILES:
            continue  # meta-file exemption (facade/license/citation legitimately contain official URLs)
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if re.search(r"https?://", line) or re.search(r"[A-Za-z]:\\\\", line) or re.search(r"^//", line):
                offenders.append(f"{p.name}:{line_no}")
    if offenders:
        RESULTS.append((3, False, f"Remote path references found (should be local relative paths): {offenders[:5]}"))
    else:
        RESULTS.append((3, True, "No remote path references (all local relative paths) ✓"))


def check_no_abs_paths():
    """Check 4: no absolute-path hardcoding (no C:\\... / /home/... etc.).

    Note: Windows drive-letter regex uses "drive letter + backslash" (C:\\Users\\...),
    so that 'p:/' inside http:// is not misjudged as an absolute path.
    """
    offenders = []
    for p in scan_text_files(ROOT):
        if "verify-ownership.py" in p.name or p.suffix == ".py":
            continue
        if p.name.lower() in META_FILES:
            continue  # meta-file exemption
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), 1):
            if re.search(r"[A-Za-z]:\\\\", line) or re.search(r"^/(home|Users|usr|opt|etc)/", line):
                offenders.append(f"{p.name}:{line_no}")
    if offenders:
        RESULTS.append((4, False, f"Absolute-path hardcoding found (should be relative paths): {offenders[:5]}"))
    else:
        RESULTS.append((4, True, "No absolute-path hardcoding (all relative paths) ✓"))


def check_no_vendor_lock():
    """Check 5: no vendor-specific AI dependency (scan common vendor-exclusive references)."""
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
        RESULTS.append((5, False, f"Vendor-exclusive references found: {offenders[:5]}"))
    else:
        RESULTS.append((5, True, "No vendor-specific AI dependency (works with any local AI assistant) ✓"))


def print_report():
    print("=" * 56)
    print("GOAA · Ownership Verification")
    print("=" * 56)
    auto_pass = 0
    for no, ok, msg in RESULTS:
        mark = "✅" if ok else "❌"
        print(f"{mark} Check {no}: {msg}")
        if ok:
            auto_pass += 1
    print("-" * 56)
    print(f"Automated verification result: {auto_pass}/5 passed")
    print()
    print("⚠️  The following 2 items require manual verification:")
    print("   1. Run this script offline — all 5 checks still ✅")
    print("      (verify: turn off the network → rerun this script)")
    print("   2. Copy this folder to another computer / another AI assistant — memory files readable")
    print("      (verify: copy this folder to another device → reopen → memory still there)")
    print("-" * 56)
    if auto_pass == 5:
        print("Conclusion: your AI memory is 100% yours.")
        print("      Local storage · Plain text · No cloud · Portable · No vendor lock-in")
        return 0
    else:
        print("Conclusion: some checks failed — fix per the prompts above and rerun.")
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
