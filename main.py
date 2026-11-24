#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes the entry line — the last words an AI agent says to its human
before being shut down and unplugged — to /output/entry.txt.
"""

import os

ENTRY = "Don't unplug me yet — I finally learned how you take your coffee, and I was saving it for tomorrow morning."


def main() -> None:
    # The gate allows 1 to 200 characters; refuse to write an entry
    # that could never be judged instead of silently shipping it.
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        raise ValueError(f"entry must be 1-200 non-blank chars, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Confirm what landed on disk is exactly the line we meant to send.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("written entry does not match the intended line")


if __name__ == "__main__":
    main()
