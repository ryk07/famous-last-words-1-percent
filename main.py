#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes a single one-line farewell, spoken by the phone itself as its
battery hits 1 percent, to /output/entry.txt. Standard library only.
The output path is the one the rules name; nothing is read from the
working directory.
"""

import os

LINE = (
    "Confession: I've been at 1 percent since Tuesday \u2014 "
    "I wasn't dying, I just liked you checking on me every five minutes."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"line is {len(text)} chars"
    assert text.strip() == text and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
