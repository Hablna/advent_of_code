from pathlib import Path

FILE_PATH = Path(__file__).resolve().parent.parent / "input"


class day2025:

    def __init__(self, file_path=FILE_PATH):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f if line.strip()]

    def total_splits(self):
        manifold = self.read_file()
        splits = 0

        # colonnes ou un faisceau descend
        # un set fusionne les faisceaux qui arrivent au meme endroit
        beams = {manifold[0].index("S")}

        for line in manifold[1:]:
            next_beams = set()

            for col in beams:
                if not 0 <= col < len(line):
                    continue

                if line[col] == "^":
                    splits += 1
                    if col - 1 >= 0:
                        next_beams.add(col - 1)
                    if col + 1 < len(line):
                        next_beams.add(col + 1)
                else:
                    next_beams.add(col)

            beams = next_beams

        return splits


if __name__ == "__main__":
    print(day2025().total_splits())
