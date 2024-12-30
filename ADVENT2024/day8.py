#Cette fonction me retourne une liste des coordonnées des occurences des lettres ou nombres
def get_coordonnees(puzzle):
    coordonnes = {}
    for y, line in enumerate(puzzle):
        for x, char in enumerate(line):
            if char.isalnum():
                #setdefault verifie si la clé char n'existe pas déjà dans le dictionnaire, sinon ça la crée
                coordonnes.setdefault(char, []).append((x, y))
    return coordonnes

def calcul_antinoeud(coordonnees, longueur, hauteur):
    antinoeuds = set()
    for lettre, liste_tuples in coordonnees.items():

        for i in range(len(liste_tuples)):
            for j in range(i + 1, len(liste_tuples)):
                # je calcul les coordinates des deux antinoeuds
                diffX = liste_tuples[j][0] - liste_tuples[i][0]
                diffY = liste_tuples[j][1] - liste_tuples[i][1]

                antinoeud1X = liste_tuples[i][0] - diffX
                antinoeud1Y = liste_tuples[i][1] - diffY
                antinoeud2X = liste_tuples[j][0] + diffX
                antinoeud2Y = liste_tuples[j][1] + diffY

                if 0 <= antinoeud1X <= longueur and 0 <= antinoeud1Y <= hauteur:
                    # .add() ajoute l'élement s'il n'existe pas déjà
                    antinoeuds.add((antinoeud1X, antinoeud1Y))

                if 0 <= antinoeud2X <= longueur and 0 <= antinoeud2Y <= hauteur:
                    antinoeuds.add((antinoeud2X, antinoeud2Y))
    return antinoeuds

# Un peu basique 😅
with open("entree", 'r') as file:
    puzzle = [line.strip() for line in file.readlines()]

longueur = len(puzzle[1])-1
hauteur = len(puzzle)-1

coordonnees = get_coordonnees(puzzle)
antinoeuds = calcul_antinoeud(coordonnees, longueur, hauteur)
print(len(antinoeuds))