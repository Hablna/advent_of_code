import re
from collections import Counter

WIDTH, HEIGHT = 101, 103

def pos_after_t(x, y, vx, vy, t, w=WIDTH, h=HEIGHT):
    # Avance directement de t secondes sur un tore
    return (x + vx * t) % w, (y + vy * t) % h

if __name__ == "__main__":
    robots = []  # liste de tuples (x, y, vx, vy)
    with open("entree", "r") as f:
        for line in f:
            # format attendu : p=xx,yy v=dx,dy (mais le regex attrape juste les nombres)
            x, y, vx, vy = map(int, re.findall(r"-?\d+", line))
            robots.append((x, y, vx, vy))

    # --- Part 1 : t = 100 secondes ---
    t = 100
    occ = Counter()
    for x, y, vx, vy in robots:
        nx, ny = pos_after_t(x, y, vx, vy, t)
        occ[(nx, ny)] += 1

    q1 = q2 = q3 = q4 = 0
    mx, my = WIDTH // 2, HEIGHT // 2  # 50, 51

    for (x, y), count in occ.items():
        if x < mx and y < my:
            q1 += count
        elif x > mx and y < my:
            q2 += count
        elif x < mx and y > my:
            q3 += count
        elif x > mx and y > my:
            q4 += count
        # si x == mx ou y == my, ignoré (lignes médianes)

    print(q1 * q2 * q3 * q4)
