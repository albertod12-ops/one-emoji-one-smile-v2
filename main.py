#!/usr/bin/env python3
"""One Emoji, One Smile — v2.

Writes exactly one emoji to /output/entry.txt: heart hands,
two hands shaping a heart — warmth deliberately offered.
"""

import os

EMOJI = "\U0001faf6"


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
