from collections import deque

with open('entree', 'r') as file:
    donnee = file.readlines()
    entree = []
    for i in  donnee:
        rows = []
        i = i.strip()
        for j in i:
            rows.append(int(j))
        entree.append(rows)
print(entree)

rows = len(entree)
print(rows)
cols = len(entree[0])
print(cols)

#Directions
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(start_i, start_j):
    visited = set()
    queue = deque()
    queue.append((start_i, start_j))
    visited.add((start_i, start_j))
    count = 0

    while queue:
        i, j = queue.popleft()
        current_value = entree[i][j]
        if current_value == 9 :
            count += 1
            continue

        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols :
                next_value = entree[ni][nj]
                if (ni, nj) not in visited and next_value == current_value+1:
                    visited.add((ni, nj))
                    queue.append((ni, nj))

    return count
count = 0
#detect zero
for i in range(rows):
    for j in range(cols):
        if entree[i][j] == 0:
            count += bfs(i, j)

print(count)
