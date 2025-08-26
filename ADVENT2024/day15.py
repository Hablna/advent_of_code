import re

with open("entree", "r") as f:
    cards, movement = f.read().strip().split("\n\n")
    grid = [list(line) for line in cards.split("\n")]

def move(direction, pos, grid):
    y, x = pos
    d = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}
    dy, dx = d[direction]
    ny, nx = y + dy, x + dx

    # Mur -> pas de mouvement
    if grid[ny][nx] == "#":
        return pos

    # Vide -> avance le robot
    if grid[ny][nx] == ".":
        grid[y][x] = "."
        grid[ny][nx] = "@"
        return (ny, nx)

    # Boîte -> scanner la chaîne de 'O' puis pousser si possible
    if grid[ny][nx] == "O":
        ty, tx = ny, nx
        # Avancer jusqu'à trouver autre chose que 'O'
        while grid[ty][tx] == "O":
            ty += dy
            tx += dx
        # Si c'est un mur, on annule
        if grid[ty][tx] == "#":
            return pos

        grid[ty][tx] = "O"  # on place un O tout à la fin
        grid[ny][nx] = "@"  # le robot se déplace dans la première boîte
        grid[y][x] = "."
        return (ny, nx)

    # Autre symbole inattendu
    return pos

# Trouver la position de départ du robot
start = None
for j in range(len(grid)):
    for i in range(len(grid[0])):
        if grid[j][i] == "@":
            start = (j, i)
            break
    if start is not None:
        break

# Appliquer tous les mouvements (ignorer les sauts de ligne)
pos = start
for ch in movement:
    if ch in "><^v":
        pos = move(ch, pos, grid)

# Calcul du score GPS (Partie 1) : somme des 100*y + x pour chaque 'O'
score = 0
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c == "O":
            score += 100 * y + x

print(score)
