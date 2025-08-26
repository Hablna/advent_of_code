with open("entree", "r") as f:
    colonne1, colonne2 = zip(*(map(int, line.split()) for line in f))

for i in colonne1:
    for j in colonne2