"""Advent of Code 2025 - Day 7: Laboratories (partie 2)."""

from collections import defaultdict
from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "input"


class day2025:

    def __init__(self, file_path=FILE_PATH):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f if line.strip()]

    def total_timelines(self):
        manifold = self.read_file()

        # colonne -> nombre de timelines qui descendent dans cette colonne
        # ici on ADDITIONNE au lieu de fusionner : deux chemins differents
        # qui arrivent au meme endroit restent deux timelines distinctes
        beams = defaultdict(int)
        beams[manifold[0].index("S")] = 1

        for line in manifold[1:]:
            next_beams = defaultdict(int)

            for col, count in beams.items():
                if not 0 <= col < len(line):
                    continue

                if line[col] == "^":
                    # chaque timeline se dedouble : une a gauche, une a droite
                    if col - 1 >= 0:
                        next_beams[col - 1] += count
                    if col + 1 < len(line):
                        next_beams[col + 1] += count
                else:
                    next_beams[col] += count

            beams = next_beams

        return sum(beams.values())


if __name__ == "__main__":
    print(day2025().total_timelines())
