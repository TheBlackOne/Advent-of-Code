input = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<"""

# with open("input.txt") as f:
#    input = f.read()

directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def get_all_box_coords(grid):
    box_coords = set()
    for y, line in enumerate(grid):
        for x in [x for x, field in enumerate(line) if field == "O"]:
            box_coords.add((x, y))

    return box_coords


def print_grid(grid):
    for line in grid:
        line = "".join(line)
        print(line)


def get_grid_field(pos):
    x, y = pos
    return grid[y][x]


def swap_grid_fields(pos1, pos2):
    global grid

    x1, y1 = pos1
    x2, y2 = pos2

    grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]


def collect_box_candidates(pos, direction):
    global grid

    candidates = []
    while True:
        pos = tuple(map(sum, zip(pos, direction)))
        x, y = pos
        field = grid[y][x]
        if field == "O":
            candidates.append(pos)
        elif field == "#":
            candidates = []
            break
        elif field == ".":
            candidates.append(pos)
            break

    return candidates


if __name__ == "__main__":
    grid = []

    robot_pos = None
    layout, movements = input.split("\n\n")
    for y, line in enumerate(layout.splitlines()):
        possible_x = line.find("@")
        if possible_x > -1:
            robot_pos = (possible_x, y)
            # line = line.replace("@", ".")
        grid.append(list(line))

    movements = list(movements.replace("\n", ""))

    for movement in movements:
        direction = directions[movement]
        new_robot_pos = tuple(map(sum, zip(robot_pos, direction)))

        neighbour = get_grid_field(new_robot_pos)

        if neighbour == "O":
            box_candites = collect_box_candidates(robot_pos, direction)
            if len(box_candites) > 0:
                box_pos1 = box_candites[0]
                box_pos2 = box_candites[-1]

                swap_grid_fields(box_pos1, box_pos2)

                neighbour = get_grid_field(box_pos1)
        if neighbour == ".":
            swap_grid_fields(robot_pos, new_robot_pos)
            robot_pos = new_robot_pos

        # print_grid(grid)

    box_coords = get_all_box_coords(grid)
    sum_coords = sum(x + y * 100 for x, y in box_coords)
    print(sum_coords)
