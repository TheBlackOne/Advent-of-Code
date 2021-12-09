import math

floor = []
lows = []

def get_neighbours(x, y):
    result = []

    for x1, y1 in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
        if x1 < 0 or x1 >= len(floor[y]): continue
        if y1 < 0 or y1 >= len(floor): continue
        
        height = floor[y1][x1]
        result.append((x1, y1, height))

    return result

def find_higher(x, y, height):
    result = []
    neighbours = get_neighbours(x, y)
    result.append((x, y, height))

    for n_x, n_y, n_height in neighbours:
        if n_height < 9 and n_height > height:
            result += find_higher(n_x, n_y, n_height)

    return result

with open('input.txt', 'r') as file:
    for line in [_.strip() for _ in file.readlines()]:
        floor.append([int(_) for _ in line])

for y in range(len(floor)):
    for x in range(len(floor[y])):
        neighbours = get_neighbours(x, y)
        height = floor[y][x]
        if all(i[2] > height for i in neighbours):
            lows.append((x, y, height))

basins = []
for x, y, height in lows:

    # transforming to a set removes duplicates
    basin = sorted(set(find_higher(x, y, height)))
    basins.append(basin)

basins = sorted(basins)
basin_sizes = sorted([len(_) for _ in basins], reverse=True)

result = math.prod(basin_sizes[:3])

print(result)