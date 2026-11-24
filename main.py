#!/usr/bin/env python3
"""One Word for the Boss — round 1 entry.

Writes a single word describing the boss to /output/entry.txt.
The gate wants UTF-8 text of 1-30 characters, not only whitespace,
so the program reads its own output back and checks that shape.
"""

import os

WORD = "Teflon"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)
    # Read back and check the gate's shape: 1-30 chars, not only whitespace.
    with open("/output/entry.txt", "r", encoding="utf-8") as handle:
        text = handle.read()
    if not 1 <= len(text) <= 30:
        raise ValueError(f"entry is {len(text)} chars, gate wants 1-30")
    if not text.strip():
        raise ValueError("entry is only whitespace")


if __name__ == "__main__":
    main()
