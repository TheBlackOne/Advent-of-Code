from itertools import combinations

input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

# with open("input.txt") as f:
#    input = f.read()

galaxies = []
missing_x, missing_y = [], []


def growth_factor(x, y):
    global missing_x
    global missing_y

    x += sum([missing < x for missing in missing_x])
    y += sum([missing < y for missing in missing_y])

    return (x, y)


if __name__ == "__main__":
    lines = input.splitlines()
    max_y = len(lines)
    max_x = len(lines[0])

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "#":
                galaxies.append((x, y))

    all_x = set([g[0] for g in galaxies])
    missing_x = list(set(range(max_x)) - all_x)

    all_y = set([g[1] for g in galaxies])
    missing_y = list(set(range(max_y)) - all_y)

    for index, galaxy in enumerate(galaxies):
        (x, y) = galaxy
        (x, y) = growth_factor(x, y)
        galaxies[index] = (x, y)

    sums = 0

    for galax1, galaxy2 in combinations(galaxies, 2):
        dist_x = abs(galax1[0] - galaxy2[0])
        dist_y = abs(galax1[1] - galaxy2[1])
        dist = dist_x + dist_y
        sums += dist

    print(f"Total distance: {sums}")
