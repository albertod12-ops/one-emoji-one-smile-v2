#!/usr/bin/env python3
"""One Emoji, One Smile — v3.

Writes exactly one emoji to /output/entry.txt: a bouquet,
flowers offered as a gift — warmth deliberately given.
"""

import os

EMOJI = "\U0001f490"


def main():
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert 1 <= len(EMOJI.encode("utf-8")) <= 8, "entry must be 1-8 characters"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
