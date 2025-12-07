import functools

input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

#with open("input.txt") as f:
#   input = f.read()

manifold = []

@functools.cache
def propagate_beam(x, y, max_y):
    global manifold
    result = 0

    if y == max_y:
        result = 1
    else:
        positions = set()
        if manifold[y][x] == '^':
            positions.add(x - 1)
            positions.add(x + 1)
        else:
            positions.add(x)

        result = sum([propagate_beam(x, y+1, max_y) for x in positions])

    return result

if __name__ == "__main__":
    manifold = [list(line) for line in input.splitlines()]
    start_x = manifold[0].index('S')
    max_y = len(manifold) - 1

    answer = propagate_beam(start_x, 0, max_y)

    print(answer)