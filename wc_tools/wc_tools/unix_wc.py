#!/usr/bin/env python3

import argparse
from pathlib import Path
from typing import List


class UnixWC:
    """A custom implementation of the Unix `wc` utility."""

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.filename = Path(filepath).name
        self._text_lines = None
        self._binary_data = None

    def _read_text(self) -> List[str]:
        if self._text_lines is None:
            with open(self.filepath, "r", encoding="utf-8") as f:
                self._text_lines = f.readlines()
        return self._text_lines

    def _read_bytes(self) -> bytes:
        if self._binary_data is None:
            with open(self.filepath, "rb") as f:
                self._binary_data = f.read()
        return self._binary_data

    def count_bytes(self) -> int:
        return len(self._read_bytes())

    def count_lines(self) -> int:
        return len(self._read_text())

    def count_words(self) -> int:
        return sum(len(line.split()) for line in self._read_text())

    def count_characters(self) -> int:
        return sum(len(line) for line in self._read_text())

    def __str__(self) -> str:
        return f"{self.count_lines()}  {self.count_words()}  {self.count_characters()}  {self.filename}"


def parse_args():
    parser = argparse.ArgumentParser(description="unixwc: a custom wc clone")
    parser.add_argument("filepath", help="Path to input file")
    parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-m", "--chars", action="store_true", help="Count characters")
    return parser.parse_args()


def main():
    args = parse_args()
    wc = UnixWC(args.filepath)

    # Command-option dispatch
    actions = {
        args.bytes: wc.count_bytes,
        args.lines: wc.count_lines,
        args.words: wc.count_words,
        args.chars: wc.count_characters,
    }

    # Execute the first selected option or default
    for flag, action in actions.items():
        if flag:
            print(action())
            break
    else:
        print(wc)  # calls __str__


if __name__ == "__main__":
    main()
