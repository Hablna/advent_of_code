with open("entrer", "r") as file:
    puzzles = []
    for line in file:
        puzzles.append((line.strip()))

#je cherche le caractère s dans la liste puzzles
s_y = 0
s_x = 0
for puzzle in puzzles:
    s_y += 1
    s_x = 0
    for initial in puzzle:
        s_x += 1
        if initial =='S' :
            init = [s_y,s_x]

coordonne = (init[0]-1, init[1])
tuile = puzzles[coordonne[0]][coordonne[1]]
#print(tuile)
direction = 'gauche'
i = 1
points_boucle = [(init[0]-1, init[1]-1)]
while tuile != 'S':
    if tuile not in ['-', '|']:
        points_boucle.append(coordonne)
    i += 1
    if tuile == '-':
        if direction == 'gauche':
            coordonne = (coordonne[0],coordonne[1]+1)
            direction = 'gauche'
        elif direction == 'droite':
            coordonne = (coordonne[0],coordonne[1]-1)
            direction = 'droite'

    elif tuile == '|':
        if direction == 'haut':
            coordonne = (coordonne[0]+1,coordonne[1])
            direction = 'haut'
        elif direction == 'bas':
            coordonne = (coordonne[0]-1,coordonne[1])
            direction = 'bas'

    elif tuile == 'J':

        if direction == 'gauche':
            coordonne = (coordonne[0]-1,coordonne[1])
            direction = 'bas'
        elif direction == 'haut':
            coordonne = (coordonne[0],coordonne[1]-1)
            direction = 'droite'

    elif tuile == 'L':
        if direction == 'droite':
            coordonne = (coordonne[0]-1,coordonne[1])
            direction = 'bas'
        elif direction == 'haut':
            coordonne = (coordonne[0],coordonne[1]+1)
            direction = 'gauche'

    elif tuile == 'F':
        if direction == 'droite':
            coordonne = (coordonne[0]+1,coordonne[1])
            direction = 'haut'
        elif direction == 'bas':
            coordonne = (coordonne[0],coordonne[1]+1)
            direction = 'gauche'

    elif tuile == '7':

        if direction == 'gauche':
            coordonne = (coordonne[0]+1,coordonne[1])
            direction = 'haut'
        elif direction == 'bas':
            coordonne = (coordonne[0],coordonne[1]-1)
            direction = 'droite'

    tuile = puzzles[coordonne[0]][coordonne[1]]
print(points_boucle)


def est_a_l_interieur(x, y, points_boucle):
    intersections = 0
    n = len(points_boucle)
    for i in range(n):
        x1, y1 = points_boucle[i]
        x2, y2 = points_boucle[(i + 1) % n]

        # Vérifie si le segment [x1, y1] à [x2, y2] croise le rayon horizontal depuis (x, y)
        if (y1 > y) != (y2 > y):
            intersect_x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            if intersect_x > x:
                intersections += 1

    # Impair => intérieur, Pair => extérieur
    return intersections % 2 == 1
interrieur = 0
for y in range(len(puzzles)):
    for x in range(len(puzzles[y])):
        if est_a_l_interieur(x, y, points_boucle) and (x, y) not in points_boucle:
            interrieur += 1
print(interrieur)