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
                if not charactere.isdigit() and (charactere not in [".", "\n"]):
                    symboles[f"{x},{y}"] = charactere
            x += 1
    #print(valeurs)
    #print(symboles)

    somme = 0
    for position_nombre, valeur in valeurs.items() :
        x_debut,x_fin,y = map(int,position_nombre.split(','))

        for position_symbol, symbol in symboles.items() :
            x_symbol,y_symbol = map(int, position_symbol.split(','))
            if (x_debut-1<=x_symbol<=x_fin+1) & (y-1<=y_symbol<=y+1) :
                somme+=valeur
    print(somme)
