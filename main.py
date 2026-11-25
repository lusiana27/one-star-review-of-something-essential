#!/usr/bin/env python3
"""One-Star Review of Something Essential — entry: a one-star review of the Sun.

Writes exactly one line, 153 characters, no trailing newline, to
/output/entry.txt. Standard library only.
"""

import os
import shutil

REVIEW = (
    "One star for the Sun. Shows up uninvited every morning, "
    "no snooze button, no customer service, burns my neck. "
    "Would not recommend. Will be back tomorrow."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the folder's contents, never the folder itself.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w",
              encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
