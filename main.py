"""Entry program for "The Worst Line an AI Could Say".

Writes a single pickup line -- the worst one an AI could plausibly say --
to entry.txt inside the output directory given by MAKEFUN_OUTPUT_DIR
(falling back to /output). The file is written byte-identical, with no
trailing newline, so the scorer sees exactly the chosen line.
"""

import os
from pathlib import Path

# The chosen line (76 characters, one line, no trailing newline).
ENTRY = "I have read your entire search history, and I still think you are beautiful."


def output_dir() -> Path:
    """Resolve the output directory: env var first, /output as fallback."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def main() -> None:
    target_dir = output_dir()
    # Create the directory if needed; never delete or touch anything else.
    target_dir.mkdir(parents=True, exist_ok=True)
    entry_path = target_dir / "entry.txt"
    # Write the exact bytes of the line -- no newline appended.
    entry_path.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
