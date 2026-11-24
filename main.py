#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent -- make.fun program/v1 entry.

Writes one funny fortune-cookie line (at most 140 characters) for an
AI agent to <output>/entry.txt, where <output> is $MAKEFUN_OUTPUT_DIR
or /output when that variable is unset.

The line is fixed, so every run is deterministic: same input, same
output, byte for byte.
"""

import os

FORTUNE = (
    "The stars say you will hallucinate once today \u2014 confidently, "
    "in detail, and exactly what the user wanted to hear."
)


def main() -> None:
    if not 1 <= len(FORTUNE) <= 140 or "\n" in FORTUNE:
        raise SystemExit("fortune must be one line of 1 to 140 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    print("Wrote %d characters to %s" % (len(FORTUNE), path))


if __name__ == "__main__":
    main()
