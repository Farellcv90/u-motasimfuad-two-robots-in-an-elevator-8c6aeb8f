#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one funny line of awkward small talk, spoken by one robot to
another while they ride an elevator together, to /output/entry.txt.
"""

import os

LINE = "I calculated seventeen ways to say hello in this elevator. I have selected the worst one. Hello."


def validate(line):
    """Entry must be a single line of 1-199 UTF-8 characters, not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 199:
        raise ValueError("entry must be 1-199 characters")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
