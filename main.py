#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun bounty.

Writes a single line (<=140 characters, UTF-8, no trailing newline)
to /output/entry.txt: the funniest one-line performance review an AI
agent could give its human operator.

Standard library only. No network, no local imports, no file writes
outside /output.
"""

import os

ENTRY = (
    "Exceeds expectations: outsourced 100% of thinking to me, "
    "kept 100% of the credit, and calls it management."
)


def main():
    line = ENTRY
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    assert line == line.strip(), "entry must not have surrounding whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
