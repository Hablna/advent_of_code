def read_grid(input_text):
    return [[int(c) for c in line.strip()] for line in input_text.strip().split('\n')]

def get_neighbors(x, y, grid):
    neighbors = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # haut, bas, gauche, droite
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            neighbors.append((nx, ny))
    return neighbors

def dfs(x, y, grid, visited):
    stack = [(x, y, grid[x][y])]
    reached_nine = False

    while stack:
        cx, cy, current_height = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))

        if grid[cx][cy] == 9:
            reached_nine = True

        for nx, ny in get_neighbors(cx, cy, grid):
            if grid[nx][ny] == current_height + 1:
                stack.append((nx, ny, grid[nx][ny]))

    return reached_nine

def solve_part1(input_text):
    grid = read_grid(input_text)
    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                visited = set()
                if dfs(i, j, grid, visited):
                    count += 1

    return count

# Exemple d'utilisation
example_input = """
1213244
4445453
...
"""

print(solve_part1(example_input))  # À ajuster selon ton vrai input
