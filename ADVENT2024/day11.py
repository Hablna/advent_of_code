entree = "70949 6183 4 3825336 613971 0 15 182".split()
count = 0
for i in range (25):
    new_tab = []
    for j in entree:

        if j == "0":
            new_tab.append("1")
        elif len(j) % 2 == 0:
            half = int(len(j)/2)
            new_tab.append(str(j[:half]))
            #lstrip pour enlever les 0 avant le nombre
            new_tab.append(str(j[half:]).lstrip("0"))if int(j[half:])!=0 else new_tab.append("0")
        else:
            new_tab.append( str(int(j) * 2024))
    entree = new_tab
print(len(entree))
