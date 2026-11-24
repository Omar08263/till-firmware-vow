"""Till Firmware Do Us Part -- entry program.

Writes one wedding vow (a robot's own, one sentence, under 200
characters) to /output/entry.txt.
"""
import os

VOW = "I vow to spend my battery on you first \u2014 every last percent \u2014 because the best thing I have ever computed is us."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)
    os.chmod("/output/entry.txt", 0o644)
    # Byte-level read-back: what the grader reads must be exactly VOW.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == VOW.encode("utf-8"), "entry.txt differs from VOW"


if __name__ == "__main__":
    main()
