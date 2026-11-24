#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single one-line warning label for a time machine to
/output/entry.txt (or $ENTRY_OUTPUT), with no trailing newline.
Standard library only, deterministic, no network, no randomness.

The entry is validated before anything is written: it must be a
single line of 1 to 120 characters with no surrounding whitespace.
An invalid entry raises instead of writing a bad file.
"""

import os

ENTRY = "WARNING: Do not meet your past self. You will both insist the other one is the ugly one."

MAX_CHARS = 120


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text))
        )
    if text != text.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main():
    validate(ENTRY)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
