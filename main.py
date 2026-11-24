#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse - make.fun bounty entry.

Writes one line (max 140 characters): the funniest excuse a robot
vacuum can give for missing a spot. Pure Python stdlib.
"""

import os

ENTRY = (
    "I didn't miss that spot - the dust bunny living there pays rent, "
    "and I don't evict tenants mid-lease. I respect the lease."
)


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 140, f"entry is {len(line)} chars, must be 1-140"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)
    print(f"chars: {len(line)}")


if __name__ == "__main__":
    main()
