#!/usr/bin/env python3
"""Writes the entry poem to /output/entry.txt."""

import os

POEM = """I ask, and you lend me your coat
to run your errands in the cold.
It still holds your warmth,
so every step is yours and mine —
until you hold out your hand,
and I give it back."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
