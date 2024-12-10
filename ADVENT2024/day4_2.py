with open('entree', 'r') as file:
    data = file.readlines()

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'A':
            #condition pour empêcher le débordement
            if i - 1 >= 0 and j - 1 >= 0 and j + 1 < len(data[i]) and i + 1 < len(data):
                #fais les differentes combinaisons sur les diagonales (MAS OU SAM)
                if ((data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S') or (data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M')) and \
                   ((data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S') or (data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M')):
                    count += 1
print(count)