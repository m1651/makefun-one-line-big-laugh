"""One Line, Big Laugh: a single funny line of at most 200 characters.

The program writes one punchy joke — a fraud alert triggered by the owner's
own spending, because even the bank doesn't recognize them anymore — to
``entry.txt`` in the output directory.
"""

import os

LINE = (
    "My bank sent me a fraud alert about my own spending, which is fair — "
    "I barely recognize that person either."
)


def validate(line: str) -> None:
    """Enforce the entry gate: single non-blank line, 1-200 chars incl. newline."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) + 1 < 1 or len(line) + 1 > 200:
        raise ValueError(
            f"entry is {len(line) + 1} chars including trailing newline, "
            "outside the 1-200 char limit"
        )


def main() -> None:
    """Write the joke line to entry.txt in the output directory."""
    validate(LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip verification: read back and confirm bytes match exactly.
    with open(os.path.join(output_dir, "entry.txt"), "rb") as f:
        if f.read() != (LINE + "\n").encode("utf-8"):
            raise ValueError("round-trip verification failed: entry.txt mismatch")


if __name__ == "__main__":
    main()
