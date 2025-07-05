from collections import deque

entree = [
    ['.', '.', '.', 0, '.', '.', '.'],
    ['.', '.', '.', 1, '.', '.', '.'],
    ['.', '.', '.', 2, '.', '.', '.'],
    [6,5,4,3,4,5,6],
    ['7', '.', '.', '.', '.', '.', '7'],
    ['8', '.', '.', '.', '.', '.', '8'],
    ['9', '.', '.', '.', '.', '.', '9'],
]

rows = len(entree)
cols = len(entree[0])
#Directions
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(start_i, start_j):
    visited = set()
    queue = deque()
    queue.append((start_i, start_j))
    visited.add((start_i, start_j))
    found_nine = False

    while queue:
        i, j = queue.popleft()
        current_value = entree[i][j]
        if current_value == 9 :
            found_nine = True
            continue

        for di, dj in directions:
            ni, nj = i+di, j+dj
            if 0 <= ni < rows and 0 <= nj < cols :
                next_value = entree[ni][nj]
                if (ni, nj) not in visited and next_value == current_value+1:
                    visited.add((ni, nj))
                    queue.append((ni, nj))

    return found_nine

count = 0
for i in range(rows):
    for j in range(cols):
        if entree[i][j] == 0:
            if bfs(i, j):
                count+=1

print(count)
