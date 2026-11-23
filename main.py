#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one deadpan excuse from a robot vacuum to /output/entry.txt
(or $OUTPUT_DIR/entry.txt). Python 3 stdlib only, deterministic,
no network, no randomness.
"""

import os

LINE = (
    "I didn't miss that spot. I reclassified it as a protected habitat "
    "for the sock that has lived under the couch since 2023."
)


def validate(line: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not line or not line.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise SystemExit("entry contains control characters")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")
    line.encode("utf-8")  # raises if not encodable as UTF-8


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
