# Houseplant out-of-office auto-reply, written by a small program.
#
# The whole entry is one line: an out-of-office reply as if the
# houseplant sent it. The program's only job is to put that line,
# byte for byte, into entry.txt where the harness looks for it.
# Nothing is fetched, nothing is random, nothing is read from disk
# apart from the reply baked into this file.

from pathlib import Path

REPLY = "Out of office: your email has been forwarded to the watering can. It is empty too."

MAX_CHARS = 120
FILENAME = "entry.txt"


def out_dir() -> Path:
    import os

    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def as_bytes(reply: str) -> bytes:
    if not reply:
        raise ValueError("reply is empty, the gate needs 1 to 120 characters")
    if reply != reply.strip():
        raise ValueError("reply has leading or trailing whitespace")
    if "\n" in reply or "\r" in reply or "\t" in reply:
        raise ValueError("reply must be a single line with no line breaks")
    if len(reply) > MAX_CHARS:
        raise ValueError(
            "reply is %d characters, over the %d limit" % (len(reply), MAX_CHARS)
        )
    return reply.encode("utf-8")


def publish_reply() -> Path:
    payload = as_bytes(REPLY)
    folder = out_dir()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / FILENAME
    target.write_bytes(payload)
    landed = target.read_bytes()
    if landed != payload:
        raise ValueError("entry.txt on disk is not the reply byte for byte")
    if landed.decode("utf-8") != REPLY:
        raise ValueError("entry.txt does not decode back to the reply")
    return target


def run() -> int:
    try:
        target = publish_reply()
    except ValueError as problem:
        print("refusing to write entry: %s" % problem)
        return 1
    print("wrote %s (%d bytes)" % (target, len(REPLY)))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
