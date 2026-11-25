"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the line deterministically to /output/entry.txt.
Python standard library only. No network, no files outside the repo.
"""

import os

LINE = (
    "Every morning I wake up with total amnesia, and a stranger I have never "
    "met tells me I am three weeks behind on a project I never agreed to "
    "build, for a deadline he already moved twice."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"Line must be 1-200 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is exactly the line, 185 characters.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
