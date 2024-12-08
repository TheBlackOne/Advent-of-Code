import itertools
from collections import defaultdict

input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

# with open("input.txt") as f:
#    input = f.read()


if __name__ == "__main__":
    input = input.splitlines()
    max_x = len(input[0])
    max_y = len(input)
    limits = [range(max_x), range(max_y)]

    antennas = defaultdict(list)
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c != ".":
                antennas[c].append((x, y))

    antinode_coords = set()

    for antenna_coords in antennas.values():
        for c1, c2 in itertools.permutations(antenna_coords, 2):
            # print(f"{c1} {c2}")

            # (dx, dy)
            d = tuple(v2 - v1 for v1, v2 in zip(c1, c2))

            antinode = tuple(map(sum, zip(c2, d)))
            if all(a in lim for a, lim in zip(antinode, limits)):
                antinode_coords.add(antinode)

    print(len(antinode_coords))
