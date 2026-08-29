"""Advent of Code 2025 - Day 8: Playground (partie 2)."""

from itertools import combinations
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "input"


class day2025:

    def __init__(self, file_path=FILE_PATH):
        self.file_path = file_path

    def read_file(self):
        boxes = []
        with open(self.file_path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    x, y, z = line.strip().split(",")
                    boxes.append((int(x), int(y), int(z)))
        return boxes

    def find(self, parent, i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]  # compression de chemin
            i = parent[i]
        return i

    def last_connection(self):
        boxes = self.read_file()

        pairs = []
        for i, j in combinations(range(len(boxes)), 2):
            ax, ay, az = boxes[i]
            bx, by, bz = boxes[j]
            dist = (ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2
            pairs.append((dist, i, j))
        pairs.sort()

        parent = list(range(len(boxes)))
        size = [1] * len(boxes)
        circuits = len(boxes)

        for _, i, j in pairs:
            ri, rj = self.find(parent, i), self.find(parent, j)
            if ri == rj:
                continue  # deja dans le meme circuit : on ne compte pas

            if size[ri] < size[rj]:
                ri, rj = rj, ri
            parent[rj] = ri
            size[ri] += size[rj]
            circuits -= 1

            # cette connexion vient de reunir tout le monde
            if circuits == 1:
                return boxes[i][0] * boxes[j][0]

        return None


if __name__ == "__main__":
    print(day2025().last_connection())
