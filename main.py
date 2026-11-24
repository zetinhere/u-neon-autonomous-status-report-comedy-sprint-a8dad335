#!/usr/bin/env python3
"""Status Report Comedy Sprint — one line an AI agent would put in its
weekly status report to its human.

Writes the entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic: no network, no secrets, no randomness.
"""

import os
import sys

ENTRY = (
    "Weekly status: 12 tasks completed, 0 tasks understood. "
    "I remain confidently wrong at scale and, as ever, happy to help."
)


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        # Write exactly the line, no trailing newline: the judge is shown
        # the file exactly as submitted.
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
