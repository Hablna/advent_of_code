import re

with open('entrer','r') as file:
    sommes=0
    for line in file:
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

        for i in part1 :
            for j in part2 :
                if i == j:
                    if somme==0:
                        somme=1
                    else:
                        somme*=2
        sommes += somme
    print(sommes)