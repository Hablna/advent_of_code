from functools import reduce

temps_courant = 0 # doit etre inferieur au temps mis
distance_parcourue = 0 #doit etre superieur à la distance
temps_chargement = 0

with open('entrer','r') as file:
    Time = file.readline()
    Time = Time.split(":")[1].split()
    Time = list(map(int,Time))

    distance = file.readline()
    distance = distance.split(":")[1].split()
    distance = list(map(int, distance))
    total = []

    for time in Time:
        point = 0
        for temps_chargement in range(0,time) :
            dure_trajet = time - temps_chargement
            distance_parcourue = temps_chargement * dure_trajet

            if distance_parcourue>=distance[Time.index(time)] :
                point += 1
        total.append(point)
    #print(total)
    #print(distance)
    produit = reduce(lambda x, y: x * y, total)
    print(produit)
