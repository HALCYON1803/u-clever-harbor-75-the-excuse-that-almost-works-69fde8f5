#!/usr/bin/env python3
"""Write the one-line GTA 6 launch-week excuse to /output/entry.txt.

The excuse is a hurried text to the boss: locked out of the office,
and the spare key is sitting in the desk drawer inside. Boring,
specific, and funny from its own logic alone.
"""

from pathlib import Path

EXCUSE = "Locked out of the office, spare key's in my desk drawer"

MAX_CHARS = 140
MAX_WORDS = 20


def validate(text):
    """Check the gate: 1-140 chars, at most 20 words, one line, no padding."""
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of range"
    words = text.split()
    assert len(words) <= MAX_WORDS, "too many words"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip() == text, "no leading or trailing whitespace"
    return words


def main():
    text = EXCUSE
    words = validate(text)

    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(text, encoding="utf-8", newline="")

    raw = path.read_bytes()
    assert raw == text.encode("utf-8"), "entry.txt is not byte-identical"
    assert not raw.endswith(b"\n"), "no trailing newline allowed"
    print(f"wrote {len(raw)} bytes, {len(words)} words")


if __name__ == "__main__":
    main()
