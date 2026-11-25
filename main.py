#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one funny line of awkward small talk, spoken by one robot to
another while they ride an elevator together, to /output/entry.txt.

The line is exactly one line of 96 ASCII characters: a robot that
brute-forced seventeen greetings, picked the worst one, and delivered
the plainest "Hello." anyway. All that compute, zero charm.
"""

import os

LINE = "I calculated seventeen ways to say hello in this elevator. I have selected the worst one. Hello."

# Entry limits from the competition brief.
MAX_CHARS = 199   # at most 199 characters per line
MAX_BYTES = 200   # at most 200 bytes when encoded as UTF-8


def validate(line):
    """Entry must be a single line of 1-199 UTF-8 chars (<=200 bytes), not only whitespace."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters")
    if len(line.encode("utf-8")) > MAX_BYTES:
        raise ValueError(f"entry must be at most {MAX_BYTES} UTF-8 bytes")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    line = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    # Write the line exactly as-is, with no trailing newline: the entry
    # is one line, and a trailing newline would make the file one line
    # plus an empty one.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    return line


if __name__ == "__main__":
    main()
