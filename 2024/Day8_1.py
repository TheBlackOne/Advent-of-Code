import itertools

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
    antennas = {}

    input = input.splitlines()
    max_x = len(input[0])
    max_y = len(input)

    lim_x = range(max_x)
    lim_y = range(max_y)

    for y, line in enumerate(input):
        x = 0
        for x, c in enumerate(line):
            if c != ".":
                if c not in antennas.keys():
                    antennas[c] = []
                antennas[c].append((x, y))

    antinode_coords = set()

    for antenna_coords in antennas.values():
        for c1, c2 in itertools.permutations(antenna_coords, 2):
            # print(f"{c1} {c2}")

            # (dx, dy)
            d = tuple(v2 - v1 for v1, v2 in zip(c1, c2))

            antinode = tuple(map(sum, zip(c2, d)))
            if antinode[0] in lim_x and antinode[1] in lim_y:
                antinode_coords.add(antinode)

    print(len(antinode_coords))
