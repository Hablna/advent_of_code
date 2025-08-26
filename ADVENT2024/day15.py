with open("entree", "r") as f:
    cards, movement = f.read().strip().split("\n\n")
    card = [list(line) for line in cards.split("\n")]

def move(direction, pos, grid):
    y, x= pos
    d = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
    dy, dx = d[direction]
    ny, nx = y + dy, x + dx

    if grid[ny][nx] == "#":
        return pos

    if grid[ny][nx] == ".":
        grid[y][x] = "."
        grid[ny][nx] = "@"
        return (ny, nx)

    if grid[ny][nx] == "O":
        ty, tx = ny, nx
        # j'avance jusqu'a  trouver un mur ou un point
        while grid[ty][tx] == "0":
            ty, tx = ty + dy, tx + dx
        if grid[ty][tx] == "#":
            return pos
        cy, cx = ty, tx
        while (cy, cx) != (ny, nx):
            py, px = cy - dy, cx - dx  # précédente case dans la chaîne
            grid[cy][cx] = grid[py][px]  # 'O' se décale d'un cran
            cy, cx = py, px

        # La case voisine du robot devient libre
        grid[ny][nx] = "@"
        grid[y][x] = "."
        return (ny, nx)
    return pos
