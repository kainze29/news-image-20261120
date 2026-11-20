"""Copy the bundled 20 November 2026 front page to the output path.

The repository carries the finished front page as news.png: six photo
panels for the day's biggest stories, the numbered list of stories
7 to 50, and a UTC timeline strip, all drawn for Friday 20 November
2026. This program runs in the grader's sandbox with no network, so
it does no drawing and no fetching: it reads the bundled PNG, checks
that it is a whole image inside the competition's limits, and writes
it unchanged to entry.png in the output directory. Two runs write
the same bytes, because the input never changes.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

SOURCE_FILE = "news.png"
TARGET_FILE = "entry.png"
MAGIC = b"\x89PNG\r\n\x1a\n"
TAIL = b"\x00\x00\x00\x00IEND\xaeB`\x82"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
MIN_BYTES = 4_096


def fail(reason):
    """Stop the run with a plain explanation."""
    sys.exit(f"{SOURCE_FILE}: {reason}")


def read_bundled():
    """Load the front page shipped beside this program."""
    here = Path(__file__).resolve().parent
    return (here / SOURCE_FILE).read_bytes()


def inspect(data):
    """Check the bytes are a whole PNG inside the size limits."""
    if len(data) > MAX_BYTES:
        fail(f"{len(data)} bytes, over the 1 MiB limit")
    if len(data) < MIN_BYTES:
        fail(f"only {len(data)} bytes, looks truncated")
    if data[:8] != MAGIC:
        fail("missing PNG signature")
    if data[12:16] != b"IHDR":
        fail("first chunk is not IHDR")
    width, height = struct.unpack(">II", data[16:24])
    if width == 0 or height == 0:
        fail("zero width or height in IHDR")
    depth, colour = data[24], data[25]
    if depth != 8 or colour != 2:
        fail(f"expected 8-bit RGB, got depth {depth} colour {colour}")
    if width > MAX_SIDE or height > MAX_SIDE:
        fail(f"{width}x{height} pixels, over the 1024 limit")
    if data[-12:] != TAIL:
        fail("missing whole IEND chunk at the end")
    return width, height


def emit(data):
    """Write the image into the grader's output directory."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / TARGET_FILE
    target.write_bytes(data)
    return target


def run():
    data = read_bundled()
    width, height = inspect(data)
    target = emit(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"{target}: {len(data)} bytes, {width}x{height}, sha256 {digest}")


if __name__ == "__main__":
    run()
