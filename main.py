#!/usr/bin/env python3
"""One Emoji, One Smile — v3: a bouquet.

The entry is a single emoji, U+1F490 BOUQUET: flowers handed to a
stranger, a gift rather than a symbol. Writing it is the whole
program: one character, no trailing newline, world-readable.
"""

import os

EMOJI = "\U0001f490"
# v3: the gift, not the gesture — flowers handed over, not a symbol.
OUT_DIR = "/output"
OUT_PATH = "/output/entry.txt"


def main():
    if len(EMOJI) != 1:
        raise ValueError("entry must be exactly one emoji")
    if not 1 <= len(EMOJI.encode("utf-8")) <= 8:
        raise ValueError("entry must be 1-8 UTF-8 bytes")
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EMOJI)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
