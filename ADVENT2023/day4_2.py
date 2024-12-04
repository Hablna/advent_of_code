import re

with open('entrer','r') as file:
    sommes=0
    line_count = 0
    matchs = []
    valeurs=[]
    for line in file:
        match =0
        somme = 0
        line = line.strip()
        parts = re.split(r"[:|]",line)
        part0 = re.split(r" ", parts[0].strip())
        part1 = re.split(r" ", parts[1].strip())
        part2 = re.split(r" ", parts[2].strip())

        #filtrage des cases vides
        part0 = [i for i in part0 if i != '']
        part1 = [i for i in part1 if i != '']
        part2 = [i for i in part2 if i != '']

        valeurs.append(1)

        for i in part1:
            for j in part2 :
                if i == j :
                    match+= 1
        matchs.append( match )
    print(valeurs)
    for w in range(0,len(matchs)):
        for x in range(valeurs[w+1],valeurs[w]+matchs[w]):
            valeurs[x] += matchs[w]
    print(valeurs)