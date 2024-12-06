from tqdm import tqdm

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
max_x = None
max_y = None
barrier_candidate_coords = set()
start = None


def turn_right(direction_index):
    direction_index += 1
    if direction_index >= len(directions):
        direction_index = 0
    return direction_index


def is_barrier_to_right(pos, direction_index):
    found = False
    direction_index = turn_right(direction_index)
    dx, dy = directions[direction_index]

    while True:
        x, y, _ = pos
        new_x = x + dx
        new_y = y + dy
        if new_x not in range(max_x) or new_y not in range(max_y):
            break
        elif grid[new_y][new_x] == "#":
            found = True
            break
        pos = (new_x, new_y, None)
    return found


def walk(grid, pos, direction_index, record_barrier_candidates=False):
    visited = []

    while True:
        x, y, _ = pos
        direction = directions[direction_index]
        dx, dy = direction
        new_x = x + dx
        new_y = y + dy

        if new_x not in range(max_x) or new_y not in range(max_y):
            # print("exit found!")
            return False

        if grid[new_y][new_x] != "#":
            if (
                record_barrier_candidates
                and is_barrier_to_right(pos, direction_index)
                and (new_x, new_y) != (start[0], start[1])
            ):
                barrier_candidate_coords.add((new_x, new_y))

            pos = (new_x, new_y, direction_index)

            if pos not in visited:
                visited.append(pos)
            else:
                return True
                # return loop_counter + 1
        else:
            direction_index = turn_right(direction_index)


if __name__ == "__main__":
    grid = []

    start_y = 0
    for row in input.splitlines():
        grid.append(list(row))
        if "^" in row:
            start_x = row.index("^")
            start = (start_x, start_y, 0)
        start_y += 1

    max_x = len(grid[0])
    max_y = len(grid)

    # walk the whole path and record candidated for added barriers
    walk(grid, start, 0, True)

    # test all barrier candidates if they will result in a loop
    barrier_coords = set()
    for candidate in tqdm(barrier_candidate_coords, ascii=True):
        x, y = candidate
        grid[y][x] = "#"
        if walk(grid, start, 0):
            barrier_coords.add(candidate)
        grid[y][x] = "."

    print(len(barrier_coords))
