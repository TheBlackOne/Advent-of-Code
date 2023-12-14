input = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

maps = []
sums = 0

# with open("input.txt") as f:
#    input = f.read()


def detect_reflections(map, multiplier):
    max_length = len(map[0])
    num_lines = len(map)
    global sums

    collision_map = {}

    for x in range(1, len(map[0])):
        lefts = []
        rights = []
        for line in map:
            left = line[:x]
            right = line[x:]
            length_diff = len(left) - len(right)
            if length_diff < 0:
                right = right[:length_diff]
            elif length_diff > 0:
                left = left[length_diff:]

            lefts.append(left)
            rights.append(right)

        left = "".join(lefts[::-1])
        right = "".join(rights)

        if left == right[::-1]:
            sums += x * multiplier


if __name__ == "__main__":
    for patterns in input.split("\n\n"):
        map = patterns.split()
        maps.append(map)

    for map in maps:
        detect_reflections(map, 1)

        # rotate map
        map = list(zip(*map))
        map = ["".join(m) for m in map]
        map = [l for l in map[::-1]]
        detect_reflections(map, 100)

    print(f"Result: {sums}")
