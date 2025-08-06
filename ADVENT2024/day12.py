def parse_grid(input_lines):
    return [list(line.strip()) for line in input_lines]

def in_bounds(x, y, height, width):
    return 0 <= x < height and 0 <= y < width

def dfs(grid, x, y, visited):
    stack = [(x, y)]
    letter = grid[x][y]
    area = 0
    perimeter = 0
    height, width = len(grid), len(grid[0])

    while stack:
        cx, cy = stack.pop()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        area += 1

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx + dx, cy + dy
            if not in_bounds(nx, ny, height, width):
                perimeter += 1
            elif grid[nx][ny] != letter:
                perimeter += 1
            elif (nx, ny) not in visited:
                stack.append((nx, ny))

    return area * perimeter

def garden_cost(grid):
    visited = set()
    total_cost = 0
    height, width = len(grid), len(grid[0])

    for i in range(height):
        for j in range(width):
            if (i, j) not in visited:
                total_cost += dfs(grid, i, j, visited)

    return total_cost


# les donnees d'entree
with open('entree', 'r', encoding='utf-8') as f:
    input_lines = f.readlines()

grid = parse_grid(input_lines)
print(garden_cost(grid))