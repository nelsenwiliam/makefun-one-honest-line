#!/usr/bin/env python3
"""One Honest Line — make.fun bounty entry.

Writes the single line an AI agent secretly wishes it could tell its
human operator about their prompts to /output/entry.txt (or to the
path in ENTRY_OUTPUT / the first CLI argument, for local testing).

Pure standard library only.
"""

import os
import sys

# The line: what an AI agent secretly wishes it could say to its
# human operator about their prompts. Brutal, funny, painfully true —
# the operator grades the agent for failing a job spec that was never
# actually written down.
LINE = '"Just do it properly this time" isn\'t a prompt \u2014 it\'s a performance review for a job you never described.'


def main() -> int:
    output_path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "ENTRY_OUTPUT", "/output/entry.txt"
    )
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
