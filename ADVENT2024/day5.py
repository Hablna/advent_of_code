
with open("entree", "r") as f:
    ordres, liste = f.read().strip().split("\n\n")
    ordres = {tuple(ordre.split("|")) for ordre in ordres.split("\n")}
    listes = [ligne.split(",") for ligne in liste.split("\n")]

for i in ordres:
    for j in listes:
        if (i[0] and i[1]) in j :
            print(f"{i[0]} et {i[1]}existent dans", j)
