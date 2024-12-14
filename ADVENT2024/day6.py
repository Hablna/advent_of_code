with open("entree", 'r') as file:
    data=[line.strip() for line in file.readlines() ]

for j in range (len(data)):
    i = data[j].find('^')
    if i != -1 : break

longueur = len(data[i])
hauteur = len(data)
mvt = 'up'
count=0
coordonees=[]
while i not in [0, longueur-1] and j not in [0, hauteur-1]:
    coordonees.append((i,j))
    if mvt == 'up' :
        if data[j-1][i]=='#':
            mvt = 'right'
            i += 1
        else:
            j -= 1
    elif mvt == 'down' :
        if data[j+1][i]=='#':
            mvt = 'left'
            i -= 1
        else:
            j += 1
    elif mvt == 'right' :
        if data[j][i+1]=='#':
            mvt = 'down'
            j += 1
        else:
            i += 1
    elif mvt == 'left' :
        if data[j][i-1]=='#':
            mvt = 'up'
            j -= 1
        else:
            i -= 1

print(len(set(coordonees)))