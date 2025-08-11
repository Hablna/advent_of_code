import re
def solve_machine(xa, ya, xb, yb, tx, ty):
    """
    Renvoie le coût minimal (3*ka + kb) si (ka, kb) entiers >=0 existent,
    sinon 0 (comme dans l'énoncé). Si max_presses=100, applique la contrainte Part 1.
    """
    det = xa * yb - xb * ya
    if det == 0:
        # Vecteurs A et B colinéaires : vérifier si la cible est atteignable, sinon 0.
        # Dans AoC, ça arrive rarement; on peut retourner 0 par défaut.
        return 0

    #Pour la parie 2, transformer en str pour avoir le lenght
    tx = int("1"+"0"*(13-len(str(tx)))+str(tx))
    ty = int("1"+"0"*(13-len(str(ty)))+str(ty))

    ka_num = tx * yb - xb * ty
    kb_num = xa * ty - tx * ya

    # Vérifie divisibilité exacte (solutions entières)
    if ka_num % det != 0 or kb_num % det != 0:
        return 0

    ka = ka_num // det
    kb = kb_num // det

    # Non-négativité
    if ka < 0 or kb < 0:
        return 0

    return 3 * ka + kb

with open('entree', 'r') as f:
    f = f.read().strip().split('\n\n')
solution = 0
for block in f:
    numbers = re.findall(r'-?\d+', block)
    numbers = [int(n) for n in numbers]
    solution = solution +solve_machine(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5])
print(solution)