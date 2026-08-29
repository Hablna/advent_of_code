"""Advent of Code 2025 - Day 8: Playground (partie 1)."""

from itertools import combinations
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "input"


class day2025:

    def __init__(self, file_path=FILE_PATH, connections=1000):
        self.file_path = file_path
        self.connections = connections

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

    def three_largest_circuits(self):
        boxes = self.read_file()

        # toutes les paires triees par distance (le carre suffit pour comparer,
        # et evite les erreurs d'arrondi des flottants)
        pairs = []
        for i, j in combinations(range(len(boxes)), 2):
            ax, ay, az = boxes[i]
            bx, by, bz = boxes[j]
            dist = (ax - bx) ** 2 + (ay - by) ** 2 + (az - bz) ** 2
            pairs.append((dist, i, j))
        pairs.sort()

        parent = list(range(len(boxes)))
        size = [1] * len(boxes)

        # on traite les N paires les plus courtes ; une paire deja reliee
        # compte quand meme comme une connexion, mais ne fusionne rien
        for _, i, j in pairs[:self.connections]:
            ri, rj = self.find(parent, i), self.find(parent, j)
            if ri == rj:
                continue
            if size[ri] < size[rj]:
                ri, rj = rj, ri
            parent[rj] = ri
            size[ri] += size[rj]

        circuits = sorted(
            (size[r] for r in range(len(boxes)) if self.find(parent, r) == r),
            reverse=True,
        )

        return circuits[0] * circuits[1] * circuits[2]


if __name__ == "__main__":
    print(day2025().three_largest_circuits())
