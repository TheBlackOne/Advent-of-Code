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
        for coord1, coord2 in itertools.permutations(antenna_coords, 2):
            # (dx, dy)
            d = tuple(e2 - e1 for e1, e2 in zip(coord1, coord2))
            antinode = coord1

            while True:
                antinode = tuple(map(sum, zip(antinode, d)))

                if any(a not in lim for a, lim in zip(antinode, limits)):
                    break

                antinode_coords.add(antinode)

    print(len(antinode_coords))
