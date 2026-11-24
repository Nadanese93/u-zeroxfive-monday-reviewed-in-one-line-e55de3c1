"""Monday, Reviewed in One Line — entry program.

Writes the one-line Monday review to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "Monday, one star: the 9 a.m. standup ran until lunch, "
    "my inbox bred overnight, and the coffee machine has filed "
    "a formal complaint."
)

MAX_CHARS = 200


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY or not ENTRY.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character gate"
            % (len(ENTRY), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
