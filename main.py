#!/usr/bin/env python3
"""Entry program: deliver entry.png to the output directory.

Only the Python standard library is used. The program reads the
entry.png file that sits next to this script and writes its bytes,
unchanged, to <output>/entry.png, where <output> is
$MAKEFUN_OUTPUT_DIR (default /output). No network, no randomness:
running it twice produces byte-identical outputs.
"""
import os
import shutil
import sys


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main(argv):
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target_dir = argv[1] if len(argv) > 1 else output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    print("wrote " + target)


if __name__ == "__main__":
    main(sys.argv)
