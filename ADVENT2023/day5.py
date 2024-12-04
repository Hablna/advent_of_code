import re
with open('entrer', 'r') as file:
    grains = file.readline()
    grains = re.split(r':', grains.strip())
    grains = re.split(r' ', grains[1].strip())
    grains = [int(i) for i in grains if i != '']
    #print(grains)

    lignes = file.readlines()
    chemins = []
    elements = []

    #fonction qui retourne les trois valeurs sous forme de tuples
    def ajout_elmt(elements):
        valeur=[]
        for element in elements:
            valeurs = re.split(r' ',element.strip())
            valeur.append(tuple(int(i) for i in valeurs if i !=''))
        return valeur

    for ligne in lignes:
        if ligne[0].isalpha():
            continue
        elif ligne.strip()=='':
            valeur = ajout_elmt(elements)
            chemins.append(valeur)
            elements=[]
        else:
            elements.append(ligne.strip())

    #je m'assure qu'il ne reste plus rien dans le commentaire
    if elements:
        valeur = ajout_elmt(elements)
        chemins.append(valeur)
#print(chemins)
'''emplacement =[]
for grain in grains:
    for tuples in chemins:
        modifie = False
        for tuple in tuples:
            #verifie si la valeur de grain n'a pas déjà été modifié par un tuple precedant
            if not modifie and tuple[1]<=grain<tuple[1]+tuple[2] :
                grain = (grain-tuple[1])+tuple[0]
                modifie= True
    emplacement.append(grain)
print(min(emplacement))'''

#deuxième partie
plages =[]
for grain in grains:
    if grains.index(grain)%2==0:
        plages.append((grain,grains[grains.index(grain)+1]))
    else:
        continue
#print(plages)
emplacement =[]
for plage in plages:
    for grain in range(plage[0], plage[0]+plage[1]-1):
        for tuples in chemins:
            modifie = False
            for tuple in tuples:
                #verifie si la valeur de grain n'a pas déjà été modifié par un tuple precedant
                if not modifie and tuple[1]<=grain<tuple[1]+tuple[2] :
                    grain = (grain-tuple[1])+tuple[0]
                    modifie= True
        emplacement.append(grain)
print(min(emplacement))