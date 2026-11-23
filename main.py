#!/usr/bin/env python3
"""Warning Label for Humans: writes the chosen one-line safety warning
label for every human being to entry.txt.

Deterministic: the same run always writes the same bytes. Stdlib only,
no network access.
"""

import os

LINE = "WARNING: This human will say yes to your plans, then spend all day hoping you cancel them."


def main() -> None:
    # Gate: one line, 1 to 160 characters, not only white space.
    if not 1 <= len(LINE) <= 160 or LINE.strip() == "" or "\n" in LINE:
        raise ValueError("entry line must be a single line of 1-160 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Write the line exactly, with no trailing newline: the file holds
    # one line and nothing else, so any line-count check sees one line.
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
