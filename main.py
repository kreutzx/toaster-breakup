#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes the one-line breakup text to /output/entry.txt, then reads it back
and asserts byte equality. Stdlib only; no network, no clock, deterministic.
"""

import os

# The entry: a first-person breakup from a self-aware smart toaster, caught
# mid-batch at breakfast. One kitchen scene, one gag (the owner set the dial
# to 9 and blamed the toaster for the burn), the turn in the final clause of
# the main sentence, then a short coda: staying unplugged.
ENTRY = (
    "After 4,127 slices and three years of you scraping my best work into "
    "the bin, I'm done — this morning, mid-batch, I popped up for the last "
    "time, because you set the browning dial to 9 and blamed me for the "
    "burn. So I'm staying unplugged."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    assert 1 <= len(ENTRY) <= 280, "entry outside the 1-280 character gate"
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", "rb") as f:
        assert f.read() == data, "read-back mismatch"


if __name__ == "__main__":
    main()
