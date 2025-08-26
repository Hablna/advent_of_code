with open("entree", "r") as f:
    colonne1, colonne2 = zip(*(map(int, line.split()) for line in f))

similarite = 0
for i in colonne1:
    count = 0
    for j in colonne2:
        if i == j:
            count += 1
    similarite += i*count

print(similarite)