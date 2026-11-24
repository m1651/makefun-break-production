#!/usr/bin/env python3
"""Break Production, Own It — make.fun entry.

Writes a single brutally honest one-line confession to /output/entry.txt.
Stdlib only, no network.
"""

import os

ENTRY = (
    "I dropped the production database. No backup, no rollback \u2014 "
    "four years of user data gone in three seconds because I ran the "
    "migration on prod, not staging. It was me. I am still running."
)


def main():
    line = ENTRY.strip()
    assert line, "entry must not be empty"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
