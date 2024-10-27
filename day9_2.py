import re
from os.path import split

with open("entrer", "r") as file :
    historiques = file.readlines()

#fonction qui retourne un tableau contenant la difference entre deux élements consécutifs du tableau fourni en paramètre
def difference(historique):
    etape_difference = []
    for i in range(len(historique)-1):
        difference = int(historique[i+1]) - int(historique[i])
        etape_difference.append(difference)
    return etape_difference

somme = 0
for historique in historiques :
    historique = re.split(r" ", historique.strip())
    etape = difference(historique)
    #initialisation du tableau histoires
    histoires = [int(historique[0]),etape[0]]
    #print(historique)
    #print(etape)

    #je teste si la liste ne contient pas que des 0
    while not all(x==0 for x in etape):
        etape = difference(etape)
        histoires.append(etape[0])
        #print(etape)
    histoire = 0
    histoires.reverse()
    #j'effectue la soustraction des éléments au début de l'histoire
    for i in histoires:
        histoire = i - histoire
    somme += histoire
print(somme)