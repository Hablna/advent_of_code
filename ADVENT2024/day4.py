with open('entree', 'r') as file:
    data = file.readlines()

count = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 'X':
            # Check right
            if j + 3 < len(data[i]) and data[i][j + 1:j + 4] == 'MAS':
                count += 1

            # Check left
            if j - 3 >= 0 and data[i][j - 3:j] == 'SAM':
                count += 1
            # Check down
            if i + 3 < len(data) and data[i + 1][j] == 'M' and data[i + 2][j] == 'A' and data[i + 3][j] == 'S':
                count += 1
            # Check up
            if i - 3 >= 0 and data[i - 1][j] == 'M' and data[i - 2][j] == 'A' and data[i - 3][j] == 'S':
                count += 1
            # Check top-left diagonal
            if i - 3 >= 0 and j - 3 >= 0 and data[i - 1][j - 1] == 'M' and data[i - 2][j - 2] == 'A' and data[i - 3][
                j - 3] == 'S':
                count += 1
            # Check top-right diagonal
            if i - 3 >= 0 and j + 3 < len(data[i]) and data[i - 1][j + 1] == 'M' and data[i - 2][j + 2] == 'A' and \
                    data[i - 3][j + 3] == 'S':
                count += 1
            # Check bottom-left diagonal
            if i + 3 < len(data) and j - 3 >= 0 and data[i + 1][j - 1] == 'M' and data[i + 2][j - 2] == 'A' and \
                data[i + 3][j - 3] == 'S':
                count += 1
            # Check bottom-right diagonal
            if i + 3 < len(data) and j + 3 < len(data[i]) and data[i + 1][j + 1] == 'M' and data[i + 2][
                j + 2] == 'A' and data[i + 3][j + 3] == 'S':
                count += 1

print(f'Total count: {count}')
