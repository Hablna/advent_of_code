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
print(coordonne)
tuile = puzzles[coordonne[0]][coordonne[1]]
direction = 'gauche'
i = 1
while tuile != 'S':
    print(tuile)
    i += 1
    if tuile == '-':
        print(coordonne)
        if direction == 'gauche':
            coordonne = (coordonne[0],coordonne[1]+1)
            direction = 'gauche'
        elif direction == 'droite':
            coordonne = (coordonne[0],coordonne[1]-1)
            direction = 'droite'

    elif tuile == '|':
        print(coordonne)
        if direction == 'haut':
            coordonne = (coordonne[0]+1,coordonne[1])
            direction = 'haut'
        elif direction == 'bas':
            coordonne = (coordonne[0]-1,coordonne[1])
            direction = 'bas'

    elif tuile == 'J':

        if direction == 'gauche':
            coordonne = (coordonne[0]-1,coordonne[1])
            print(tuile)
            direction = 'bas'
        elif direction == 'haut':
            coordonne = (coordonne[0],coordonne[1]-1)
            direction = 'droite'

    elif tuile == 'L':
        print(coordonne)
        if direction == 'droite':
            coordonne = (coordonne[0]-1,coordonne[1])
            direction = 'bas'
        elif direction == 'haut':
            coordonne = (coordonne[0],coordonne[1]+1)
            direction = 'gauche'

    elif tuile == 'F':
        print(coordonne)
        if direction == 'droite':
            coordonne = (coordonne[0]+1,coordonne[1])
            direction = 'haut'
        elif direction == 'bas':
            coordonne = (coordonne[0],coordonne[1]+1)
            direction = 'gauche'

    elif tuile == '7':
        print(coordonne)

        if direction == 'gauche':
            coordonne = (coordonne[0]+1,coordonne[1])
            direction = 'haut'
        elif direction == 'bas':
            coordonne = (coordonne[0],coordonne[1]-1)
            direction = 'droite'
    tuile = puzzles[coordonne[0]][coordonne[1]]
print(int(i/2))
