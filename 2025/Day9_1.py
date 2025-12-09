import itertools

input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

#with open("input.txt") as f:
#   input = f.read()

if __name__ == "__main__":
    tiles = []
    for line in input.splitlines():
        x, y = line.split(',')
        tiles.append((int(x), int(y)))

    areas = []

    for tile1, tile2 in itertools.combinations(tiles, 2):
        area = (abs(tile2[0] - tile1[0]) + 1) * (abs(tile2[1] - tile1[1]) + 1)
        areas.append(area)

    print(max(areas))