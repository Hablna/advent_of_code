with open("entree", 'r') as file:
    colonne1, colonne2 = zip(*(map(int, line.split()) for line in file))

colonne1, colonne2 = sorted(colonne1), sorted(colonne2)

total = sum(abs(c1 - c2) for c1, c2 in zip(colonne1, colonne2))
print(total)