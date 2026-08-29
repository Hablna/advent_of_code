"""Advent of Code 2025 - Day 9: Movie Theater (partie 2)."""

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

    def build_axis(self, values):
        """Compression : un representant par coordonnee de sommet, plus un
        representant par intervalle vide entre deux sommets. La grille passe
        de 100000 a ~500 de cote, sans rien perdre : a l'interieur d'un
        intervalle, tout le polygone est identique."""
        axis, index = [], {}
        for i, v in enumerate(values):
            index[v] = len(axis)
            axis.append(v)
            if i + 1 < len(values) and values[i + 1] > v + 1:
                axis.append(v + 1)
        return axis, index

    def largest_rectangle(self):
        tiles = self.read_file()
        n = len(tiles)

        axis_x, col = self.build_axis(sorted({x for x, _ in tiles}))
        axis_y, row = self.build_axis(sorted({y for _, y in tiles}))
        width, height = len(axis_x), len(axis_y)

        # aretes du polygone (la liste boucle sur elle-meme)
        verticals, horizontals = [], []
        for i in range(n):
            (x1, y1), (x2, y2) = tiles[i], tiles[(i + 1) % n]
            if x1 == x2:
                verticals.append((x1, min(y1, y2), max(y1, y2)))
            else:
                horizontals.append((y1, min(x1, x2), max(x1, x2)))

        green = [bytearray(width) for _ in range(height)]

        # balayage : sur chaque ligne, les aretes verticales traversees
        # delimitent l'interieur par paires (regle pair/impair)
        for r, ry in enumerate(axis_y):
            crossings = sorted(x for x, lo, hi in verticals if lo <= ry < hi)
            line = green[r]
            for k in range(0, len(crossings), 2):
                for c in range(col[crossings[k]], col[crossings[k + 1]] + 1):
                    line[c] = 1

        # les aretes horizontales sont paralleles au balayage : on les ajoute
        for y, lo, hi in horizontals:
            line = green[row[y]]
            for c in range(col[lo], col[hi] + 1):
                line[c] = 1

        # sommes prefixes du nombre de cases NON vertes
        prefix = [[0] * (width + 1) for _ in range(height + 1)]
        for r in range(height):
            acc = 0
            above, cur = prefix[r], prefix[r + 1]
            line = green[r]
            for c in range(width):
                acc += 1 - line[c]
                cur[c + 1] = above[c + 1] + acc

        def has_hole(r1, r2, c1, c2):
            return (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1] + prefix[r1][c1]) > 0

        # on teste les rectangles du plus grand au plus petit : le premier
        # entierement vert est la reponse
        candidates = []
        for (x1, y1), (x2, y2) in combinations(tiles, 2):
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            candidates.append((-area, x1, y1, x2, y2))
        candidates.sort()

        for neg_area, x1, y1, x2, y2 in candidates:
            c1, c2 = sorted((col[x1], col[x2]))
            r1, r2 = sorted((row[y1], row[y2]))
            if not has_hole(r1, r2, c1, c2):
                return -neg_area

        return 0


if __name__ == "__main__":
    print(day2025().largest_rectangle())
