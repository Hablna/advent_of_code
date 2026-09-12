import re

width = 101
height = 103

def update_position(p, steps=100):
    x = int(p[0])
    y = int(p[1])
    vx = int(p[2])
    vy = int(p[3])

    for i in range(steps):
        x = (x + vx) % width
        y = (y + vy) % height
    return x, y

def get_position_at_time(p, t):
    """Get robot position at time t"""
    x = int(p[0])
    y = int(p[1])
    vx = int(p[2])
    vy = int(p[3])
    
    final_x = (x + vx * t) % width
    final_y = (y + vy * t) % height
    return final_x, final_y

def has_large_cluster(positions):
    """Check if robots form a large cluster (potential Christmas tree)"""
    if not positions:
        return False
    
    position_set = set(positions)
    visited = set()
    
    def get_cluster_size(start_x, start_y):
        if (start_x, start_y) in visited or (start_x, start_y) not in position_set:
            return 0
        
        visited.add((start_x, start_y))
        size = 1
        
        # Check 4 directions for connectivity (more restrictive than 8)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            size += get_cluster_size(start_x + dx, start_y + dy)
        
        return size
    
    # Find the largest cluster
    max_cluster_size = 0
    for pos in positions:
        if pos not in visited:
            cluster_size = get_cluster_size(pos[0], pos[1])
            max_cluster_size = max(max_cluster_size, cluster_size)
    
    # Christmas tree likely has a cluster of at least 20% of robots
    return max_cluster_size >= len(positions) * 0.2

def visualize_pattern(robots, t):
    """Visualize the robot pattern at time t"""
    positions = set()
    for robot in robots:
        pos = get_position_at_time(robot, t)
        positions.add(pos)
    
    print(f"\nPattern at time {t}:")
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) in positions:
                line += "#"
            else:
                line += "."
        print(line)

def find_christmas_tree(robots):
    """Find when robots form a Christmas tree pattern"""
    # Check first 10000 seconds (robots will cycle eventually)
    for t in range(10000):
        positions = []
        for robot in robots:
            pos = get_position_at_time(robot, t)
            positions.append(pos)
        
        # Check if this configuration has a large cluster
        if has_large_cluster(positions):
            return t
    
    return -1  # Not found

if __name__ == "__main__":
    robots = []
    with open('entree', 'r') as f:
        f = f.read().strip().split('\n')
        for line in f:
            p = re.findall(r'-?\d+', line)
            robots.append(p)
    
    # Part 1: Safety factor after 100 seconds
    positions = []
    occurrences = {}
    for robot in robots:
        coord = update_position(robot, 100)
        if coord not in occurrences:
            occurrences[coord] = 1
            positions.append(coord)
        else:
            occurrences[coord] += 1

    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    for coord, count in occurrences.items():
        x,y = coord
        if x < width//2 and y < height//2:
            total1 += count
        elif x > width//2 and y < height//2:
            total2 += count
        elif x < width//2 and y > height//2:
            total3 += count
        elif x > width//2 and y > height//2:
            total4 += count

    print("Part 1:", total1 * total2 * total3 * total4)
    
    # Part 2: Find Christmas tree pattern
    tree_time = find_christmas_tree(robots)
    print("Part 2:", tree_time)
    
    # Optionally visualize the pattern (commented out to avoid cluttering output)
    # if tree_time != -1:
    #     visualize_pattern(robots, tree_time)
