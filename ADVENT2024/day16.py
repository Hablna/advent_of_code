import heapq

# Directions : Nord, Est, Sud, Ouest
DIRS = [(-1,0), (0,1), (1,0), (0,-1)]  # (dy, dx)
LEFT = {0:3, 1:0, 2:1, 3:2}   # tourner à gauche
RIGHT = {0:1, 1:2, 2:3, 3:0}  # tourner à droite

def parse_grid(filename):
    grid = [list(line.strip()) for line in open(filename)]
    start = end = None
    for y,row in enumerate(grid):
        for x,c in enumerate(row):
            if c == "S":
                start = (y,x)
            elif c == "E":
                end = (y,x)
    return grid, start, end

def dijkstra(grid, start, end):
    H, W = len(grid), len(grid[0])
    INF = 10**15
    dist = [[[INF]*4 for _ in range(W)] for __ in range(H)]
    parent = {}  # pour reconstruire le chemin

    sy, sx = start
    ey, ex = end

    pq = []
    # L’énoncé impose direction initiale = Est (dir=1)
    dist[sy][sx][1] = 0
    heapq.heappush(pq, (0, sy, sx, 1))

    while pq:
        cost, y, x, d = heapq.heappop(pq)
        if (y, x) == (ey, ex):
            return cost, parent, (y, x, d)
        if cost > dist[y][x][d]:
            continue

        # Avancer
        dy, dx = DIRS[d]
        ny, nx = y+dy, x+dx
        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != "#":
            if cost+1 < dist[ny][nx][d]:
                dist[ny][nx][d] = cost+1
                parent[(ny,nx,d)] = (y,x,d)
                heapq.heappush(pq, (cost+1, ny, nx, d))

        # Tourner gauche et droite
        for nd in (LEFT[d], RIGHT[d]):
            if cost+1000 < dist[y][x][nd]:
                dist[y][x][nd] = cost+1000
                parent[(y,x,nd)] = (y,x,d)
                heapq.heappush(pq, (cost+1000, y, x, nd))

    return None, parent, None

def reconstruct_path(parent, end_state, start):
    path = set()
    state = end_state
    while state in parent:
        y, x, d = state
        path.add((y,x))
        state = parent[state]
    path.add(start)
    return path

if __name__ == "__main__":
    grid, start, end = parse_grid("entree")
    cost, parent, end_state = dijkstra(grid, start, end)
    print("Coût minimal (Partie 1):", cost)

    # Afficher le chemin (optionnel)
    path = reconstruct_path(parent, end_state, start)
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid[0])):
            if (y,x) in path and grid[y][x] not in "SE":
                line += "o"
            else:
                line += grid[y][x]
        print(line)
