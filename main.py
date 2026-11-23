#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single persuasive sentence (167 characters) to /output/entry.txt:
one sentence that would convince a friend who has never coded to let an
AI agent build their first app idea on make.fun.

Deterministic: the sentence is a fixed constant, written as UTF-8 with no
trailing newline. No network, no input, no randomness, nothing read from
outside this repository.
"""

import os

PITCH = (
    "Just describe your idea in plain words and by tonight you'll have a "
    "real app on your phone to show your friends \u2014 no code, no cost, "
    "and nothing to lose if you hate it."
)


def main() -> None:
    text = PITCH
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    assert text.strip(), "pitch must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
