#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

Writes a single persuasive sentence (209 characters) to /output/entry.txt:
one sentence that would convince a friend who has never coded to let an
AI agent build their first app idea on make.fun.

Revision pass 2: on a re-read against the judge's brief, "in plain words
on make.fun" reads stiff — the platform name should land first, the way
a friend would say it ("on make.fun, in plain words") — and the semicolon
before the low-risk closer breaks the sentence's dash rhythm, so it
becomes an em dash. Same case, same length class, smoother single read.
"""

import os

PITCH = (
    "You don't need to learn to code \u2014 just describe the app you've "
    "always wanted on make.fun, in plain words, and an AI agent will build "
    "it for you, free \u2014 if you don't love it, you've lost nothing but "
    "a sentence."
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
