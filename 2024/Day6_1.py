input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# with open("input.txt") as f:
#    input = f.read()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

if __name__ == "__main__":
    start = None
    visited = []
    grid = []

    start_y = 0
    for row in input.splitlines():
        grid.append(list(row))
        if "^" in row:
            start_x = row.index("^")
            start = (start_x, start_y)
        start_y += 1
    visited.append(start)

    max_x = len(grid[0])
    max_y = len(grid)

    direction_index = 0
    pos = start
    while True:
        x, y = pos
        direction = directions[direction_index]
        dx, dy = direction
        new_x = x + dx
        new_y = y + dy

        if new_x not in range(max_x) or new_y not in range(max_y):
            break

        if grid[new_y][new_x] != "#":
            pos = (new_x, new_y)
            visited.append(pos)
        else:
            direction_index += 1
            if direction_index >= len(directions):
                direction_index = 0

    print(len(set(visited)))
