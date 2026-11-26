#!/usr/bin/env python3
"""Rename the Planet — entry program.

Writes the single entry line to /output/entry.txt and prints it to stdout.
"""

import os

ENTRY = "Jupiter, renamed 'The Grudge,' because it has nursed one storm bigger than Earth for three hundred years and refuses to let it go."


def main():
    # The gate allows 1-200 characters; fail loudly instead of shipping a bad line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
