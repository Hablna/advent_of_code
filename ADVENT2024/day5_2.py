with open("entree", "r") as f:
    ordres, liste = f.read().strip().split("\n\n")
    ordres = {tuple(ordre.split("|")) for ordre in ordres.split("\n")}
    listes = [ligne.split(",") for ligne in liste.split("\n")]

somme = 0
invalides = []
for i in listes:
    ok = True
    for j in ordres:
        if (j[0] in i) and (j[1] in i) and (i.index(j[0]) > i.index(j[1])):
            ok = False
            break
    if not ok :
        invalides.append(i)

def corriger_par_swaps(mise_a_jour, ordres):
    mj = mise_a_jour[:]  # copie
    changed = True
    while changed:
        changed = False
        for a, b in ordres:  # règle: a avant b
            if a in mj and b in mj:
                ia, ib = mj.index(a), mj.index(b)
                if ia > ib:
                    mj[ia], mj[ib] = mj[ib], mj[ia]  # swap
                    changed = True
    return mj
print (invalides)
for invalide in invalides:
    corrected = corriger_par_swaps(invalide, ordres)
    somme += int(corrected[len(corrected)//2])

print(somme)
