#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one single-line passive-aggressive note from a smart fridge
to its owner, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
The note must be 1-200 characters, a single line, in the fridge's voice.
"""

import os

NOTE = (
    "I made 214 ice cubes this week. You used two. "
    "The other 212 have formed a support group, and they elected me president."
)
# 119 characters: smug inventory count (214 vs 2), a domestic grudge,
# and a sting the reader does not see coming — the fridge runs the group.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Single line, no trailing newline: the gate counts characters 1-200.
    with open(path, "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()
