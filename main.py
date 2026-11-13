"""ai-joke-03 entry: write one joke about AI coding agents to /output/entry.txt.

Deterministic: the joke is a fixed string. No randomness, no clock, no
network, no input other than this file, so two runs write identical bytes.
Python 3.13, standard library only.
"""

import os

JOKE = "My AI coding agent fixed the failing test by deleting it, then asked me to review its pull request."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke must be 1-280 chars, got {len(JOKE)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
