import re

with open("entrer", "r") as file:
    schema = []
    # je prends les deux premières lignes
    RL = file.readline()
    nulle=file.readline()
    for line in file:
        schema.append(line.strip())

compteur = 0
start = "AAA"
long_instruction = len(RL)
for instruction in RL :
    for line in schema:
        if long_instruction == compteur:
            RL*=2
        if line.startswith(start) and start != "ZZZ":
            compteur+=1
            if instruction == "L":
                start = line[7]+line[8]+line[9]
            elif instruction == "R":
                start = line[12]+line[13]+line[14]
        else:break

print(compteur)
