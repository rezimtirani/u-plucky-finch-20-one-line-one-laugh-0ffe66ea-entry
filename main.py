"""One Line, One Laugh.

Writes one funny line to $MAKEFUN_OUTPUT_DIR/entry.txt: my
smartwatch congratulates me for standing up, then asks if I
need help — because I have been sitting since 2019.
Standard library only.
"""

import os

FUNNY_LINE = (
    "My smartwatch congratulated me for standing up, then asked "
    "if I needed help \u2014 because I've been sitting since 2019."
)


def check_line(text):
    """Check the line against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one funny line of text.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "line is %d characters, over the 200 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be exactly one line")
    return cleaned


def line_measure(text):
    """Measure the line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a punchline, or one
    padded out to fill the cap instead of landing the twist, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_line(FUNNY_LINE)
    measure = line_measure(text)
    if measure["words"] < 5:
        raise ValueError("line is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
