with open("entree", "r") as f:
    ordres, liste = f.read().strip().split("\n\n")
    ordres = {tuple(ordre.split("|")) for ordre in ordres.split("\n")}
    listes = [ligne.split(",") for ligne in liste.split("\n")]

somme = 0
for i in listes:
    ok = True
    for j in ordres:
        if (j[0] in i) and (j[1] in i) and (i.index(j[0]) > i.index(j[1])):
            ok = False
            break
    if ok :
        somme += int(i[len(i)//2])

print(somme)