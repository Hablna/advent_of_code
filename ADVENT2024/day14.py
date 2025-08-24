import re

p = [2, 4, 2, -3]

def update_position(p):
    x = int(p[0])
    y = int(p[1])
    vx = int(p[2])
    vy = int(p[3])

    width = 11
    height = 7

    for i in range(100):
        if x + vx > width:
            x = (x + vx) - width
        elif x + vx < 0:
            x = width + (x + vx)
        else:
            x = x + vx

        if y + vy > height:
            y = (y + vy) - height
        elif y + vy < 0:
            y = height + (y + vy)
        else:
            y = y + vy
    return (x, y)

if __name__ == "__main__":
    positions = []
    occurrences = {}
    with open('entree', 'r') as f:
        f = f.read().strip().split('\n')
        for line in f:
            p = re.findall(r'-?\d+', line)
            coord = update_position(p)
            if coord not in occurrences:
                occurrences[coord] = 1
                positions.append(coord)
            else:
                occurrences[coord] += 1

    print(p)
    print("Positions:", positions)
    print("Occurrences:", occurrences)
