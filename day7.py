import re
from collections import Counter

# Ordre personnalisé
ordre_cartes = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9,
                '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3,
                '3': 2, '2': 1}

with open('entrer', 'r') as file:
    compteur = {'zero': [], 'one': [], 'two': [], 'three': [], 'three-full': [], 'four': [], 'five': []}
    classement = []
    for line in file:
        mains = re.split('[ -]', line.strip())
        main = mains[0]
        enchere = mains[1]
        redondance = Counter(main)

        # Fonction de tri qui gère plusieurs caractères
        def tri(tup):
            card_str = tup[0]
            return [ordre_cartes.get(c, -1) for c in card_str]  # -1 pour les caractères non présents dans l'ordre

        grd_redondance = max(redondance.values())
        if grd_redondance == 5: compteur['five'].append((main,enchere))
        elif grd_redondance == 4:compteur['four'].append((main,enchere))
        elif grd_redondance == 3:
            if 2 in redondance.values():
                compteur['three-full'].append((main,enchere))
            else:
                compteur['three'].append((main,enchere))
        elif grd_redondance == 2:
            cles_max = [cle for cle, valeur in redondance.items() if valeur == grd_redondance]
            if len(cles_max) == 2:
                compteur['two'].append((main,enchere))
            else:
                compteur['one'].append((main,enchere))
        else:
            compteur['zero'].append((main,enchere))

    for cle, valeur in compteur.items():
        if isinstance(valeur, list) and valeur:  # Vérifier si la valeur est une liste non vide
            compteur[cle] = sorted(valeur, key=tri)

    for i in compteur.values():
        for j in i:
            classement.append(j)

    #print(classement)
    total_winning = 0
    for i in classement:
        total_winning += int(i[1])*(classement.index(i)+1)
    print(total_winning)
