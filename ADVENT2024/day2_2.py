import re
with open("entree", 'r') as file:
    data=file.readlines()

# fonction pour verifier si une liste est ordonnée
def is_ordonne(report):
    ordre = report == sorted(report) or report == sorted(report, reverse=True)
    return ordre

# fonction pour verifier si la difference entre les elements consécutis
# de la liste est entre 1 et 3
def min_max(report):
    difference=[abs(report[i] - report[i+1]) for i in range(len(report)-1)]
    #print(difference)
    return max(difference)<=3 and min(difference)>=1

valide = 0
for i in range(len(data)):
    report=re.split(r' ', data[i].strip())
    report = [int(x) for x in report]
    if is_ordonne(report) and min_max(report):
        valide+=1
    else :
        for index in range(len(report)):
            new_report = report[:index] + report[index+1:]
            if is_ordonne(new_report) and min_max(new_report):
                valide += 1
                print(new_report)
                break
print(valide)