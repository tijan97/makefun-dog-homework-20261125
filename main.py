"""Dog Ate My Homework: Funniest Excuse.

Writes one line, under 200 characters, in which a dog explains why
the homework got eaten, to <output>/entry.txt. The output directory
comes from MAKEFUN_OUTPUT_DIR (preferred), OUTPUT_DIR, or /output.
"""

import os
import sys

ENTRY = (
    "I didn't eat your homework, I graded it. "
    "It tasted like a C-minus, so I swallowed the evidence. "
    "Case closed."
)


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: entry is {len(text)} chars, over the 200 limit",
              file=sys.stderr)
        return 1
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
