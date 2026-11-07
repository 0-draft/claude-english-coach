"""Build an ASCII-only copy of rounds.html for publishing.

The artifact viewer may decode the page with a charset other than UTF-8, which
turns Japanese text into mojibake. Escaping every non-ASCII character makes the
page render the same under any ASCII-compatible charset.

Usage: python3 app/build.py app/rounds.html dist/rounds.html
"""

import re
import sys


def js_escape(text: str) -> str:
    out = []
    for ch in text:
        if ord(ch) < 128:
            out.append(ch)
            continue
        units = ch.encode("utf-16-be")
        for i in range(0, len(units), 2):
            out.append("\\u%04x" % int.from_bytes(units[i : i + 2], "big"))
    return "".join(out)


def css_escape(text: str) -> str:
    return "".join(ch if ord(ch) < 128 else "\\%06x" % ord(ch) for ch in text)


def html_escape(text: str) -> str:
    return "".join(ch if ord(ch) < 128 else "&#x%x;" % ord(ch) for ch in text)


BLOCK = re.compile(r"(<script\b[^>]*>)(.*?)(</script>)|(<style\b[^>]*>)(.*?)(</style>)", re.S)


def build(src: str) -> str:
    out, pos = [], 0
    for m in BLOCK.finditer(src):
        out.append(html_escape(src[pos : m.start()]))
        if m.group(1):
            out.append(m.group(1) + js_escape(m.group(2)) + m.group(3))
        else:
            out.append(m.group(4) + css_escape(m.group(5)) + m.group(6))
        pos = m.end()
    out.append(html_escape(src[pos:]))
    result = "".join(out)
    result.encode("ascii")  # fails loudly if anything slipped through
    return result


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        built = build(f.read())
    with open(sys.argv[2], "w", encoding="ascii") as f:
        f.write(built)
