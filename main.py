"""Tell a Whole Story in 32 Characters — a make.fun entry.

Prints exactly one Wi-Fi network name, 32 characters or fewer, that
lands a joke and implies a whole story to anyone scrolling the list.
"""

LINE = "WeHearEverythingUnit4B"


def build_line() -> str:
    line = LINE
    assert len(line) <= 32, f"line too long: {len(line)} chars"
    assert "\n" not in line
    return line


if __name__ == "__main__":
    print(build_line())
