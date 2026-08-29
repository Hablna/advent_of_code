"""Advent of Code 2025 - Day 9: Movie Theater (partie 1)."""

from itertools import combinations
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "input"


class day2025:

    def __init__(self, file_path=FILE_PATH):
        self.file_path = file_path

    def read_file(self):
        tiles = []
        with open(self.file_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    x, y = line.strip().split(",")
                    tiles.append((int(x), int(y)))
        return tiles

    def largest_rectangle(self):
        tiles = self.read_file()
        best = 0

        # les deux tuiles sont des coins OPPOSES : les bords du rectangle
        # passent par elles, donc on compte les deux colonnes et les deux
        # lignes -> +1 sur chaque cote
        for (x1, y1), (x2, y2) in combinations(tiles, 2):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > best:
                best = area

        return best


if __name__ == "__main__":
    print(day2025().largest_rectangle())
