import re

with open('entree', 'r') as file:
    data = file.read()

#retourne la somme des produits du pattern
def somme(data):
    total = 0
    match = re.compile(r'mul\(\d*,\d*\)').findall(data)
    for i in match:
        produits = re.findall(r'\d+', i)
        total += int(produits[0]) * int(produits[1])
    return total

total = 0
block = ""
is_enable = True
i = 0


while i < len(data):

    if data[i:i+4] == 'do()':
        if is_enable:
            total += somme(block)
        #augmente l'iteration de 4 pour pour sauter 'do()'
        i += 4
        is_enable = True
        block = ""
    elif data[i:i+7] == "don't()":
        if is_enable:
            total += somme(block)
        # augmente l'iteration de 7 pour pour sauter 'don't()'
        i += 7
        is_enable = False
        block = ""
    else:
        block += data[i]
        i += 1
#pour le dernier block
if is_enable:
    total += somme(block)

print(total)