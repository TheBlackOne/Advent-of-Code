floor = []
result = 0

def get_neighbours(x, y):
    top = 10
    left = 10
    bottom = 10
    right = 10

    if y > 0: top = floor[y-1][x]
    if x > 0: left = floor[y][x-1]
    if y < len(floor) - 1: bottom = floor[y+1][x]
    if x < len(floor[y]) - 1: right = floor[y][x+1]

    return (top, left, bottom, right)

with open('input.txt', 'r') as file:
    for line in [_.strip() for _ in file.readlines()]:
        floor.append([int(_) for _ in line])

for y in range(len(floor)):
    for x in range(len(floor[y])):
        neighbours = get_neighbours(x, y)
        height = floor[y][x]
        if all(i > height for i in neighbours):
            result += height + 1

print(result)