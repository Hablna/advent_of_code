import re

p = [2, 4, 2, -3]
width = 101
height = 103
def update_position(p):
    x = int(p[0])
    y = int(p[1])
    vx = int(p[2])
    vy = int(p[3])

    for i in range(100):
        x = (x + vx) % width
        y = (y + vy) % height
    return x, y

if __name__ == "__main__":
    positions = []
    occurrences = {}
    with open('entree', 'r') as f:
        f = f.read().strip().split('\n')
        for line in f:
            p = re.findall(r'-?\d+', line)
            print(p)
            coord = update_position(p)
            if coord not in positions:
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

    print(total1 * total2 * total3 * total4)
