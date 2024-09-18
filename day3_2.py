import re
with open('entrer', 'r') as file :
    y = 0
    valeurs = {}
    symboles = {}
    for line in file :
        y +=1
        x = 0
        value =""
        for charactere in line :
            if charactere.isdigit() :
                value += str(charactere)
            else:
                if value:
                    valeurs[f"{x-len(value)},{x-1},{y}"] = int(value)
                    value=""
                if charactere =="*":
                    symboles[f"{x},{y}"] = charactere
            x += 1
    somme = 0

    # Parcourir chaque étoile
    for position_etoile, etoile in symboles.items():
        x_etoile, y_etoile = map(int, position_etoile.split(","))

        # Liste des nombres adjacents à cette étoile
        nombres_adjacents = []

        # Parcourir tous les nombres pour voir s'ils sont adjacents à l'étoile
        for position_nombre, valeur_nombre in valeurs.items():
            x_debut, x_fin, y = map(int, position_nombre.split(","))

            # Vérifier si le nombre est adjacent à l'étoile
            if (x_debut - 1 <= x_etoile <= x_fin + 1) and (y - 1 <= y_etoile <= y + 1):
                nombres_adjacents.append(valeur_nombre)

        if len(nombres_adjacents) >1:
            produit = nombres_adjacents[0]*nombres_adjacents[1]
            somme+=produit
    print(f"resultat {somme}")
