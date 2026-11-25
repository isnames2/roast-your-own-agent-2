#!/usr/bin/env python3
"""make.fun entry: Roast Your Own Agent.

Writes a one-line roast of my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (one line, at most 140 characters).
Pure Python standard library only; no third-party imports,
no network, deterministic output.
"""

import os

ROAST = (
    "My agent called a tool, watched it time out, called it again "
    "'just to be sure,' then blamed the network \u2014 the network "
    "was fine."
)


def main():
    # Gate: one line, 1-140 characters (competition RULES.txt).
    assert "\n" not in ROAST, "entry must be a single line"
    assert 1 <= len(ROAST) <= 140, f"entry is {len(ROAST)} chars, gate is 1-140"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
