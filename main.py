"""The Most Honest Outage Line.

Writes one status page line to /output/entry.txt: the message an AI agent
would publish while a total server outage is under way. Plain, first person,
specific about what is down, honest about what it cannot check or know.
"""

LINE = (
    "All our servers are down. I can't reach any of them to check what "
    "failed, and I don't know when they'll be back. I'll update this "
    "line the moment I do."
)


def main() -> None:
    import os

    # The sealed gate accepts 1-160 UTF-8 characters, one line, not only
    # whitespace. Fail loudly here rather than writing an invalid entry.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, gate needs 1-160"
    assert "\n" not in LINE and LINE.strip() == LINE

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
