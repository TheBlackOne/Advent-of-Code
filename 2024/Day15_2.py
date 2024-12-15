import keyboard

input = """#######
#.....#
#.O#.##
#@O...#
#.....#
#######

>>v>^^"""

with open("input.txt") as f:
    input = f.read()

directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}


def get_all_box_coords(grid):
    box_coords = set()
    for y, line in enumerate(grid):
        for x in [x for x, field in enumerate(line) if field == "["]:
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


def collect_box_candidates_vertical(pos, direction):
    global grid

    positions = [pos]

    candidates = []

    while True:
        new_candidates = set()
        add_new_candidates = True
        for position in positions:
            neighbour_pos = tuple(map(sum, zip(position, direction)))
            neighbour_field = get_grid_field(neighbour_pos)

            if neighbour_field == "[":
                new_candidates.add(neighbour_pos)
                x, y = neighbour_pos
                new_candidates.add((x + 1, y))
            elif neighbour_field == "]":
                new_candidates.add(neighbour_pos)
                x, y = neighbour_pos
                new_candidates.add((x - 1, y))
            elif neighbour_field == "#":
                candidates = []
                add_new_candidates = False
                break
        if len(new_candidates) == 0:
            break

        positions = new_candidates
        if add_new_candidates:
            candidates.append(new_candidates)

    return candidates


def collect_box_candidates_horizontal(pos, direction):
    global grid

    candidates = []
    while True:
        pos = tuple(map(sum, zip(pos, direction)))
        field = get_grid_field(pos)
        if field == "[" or field == "]":
            candidates.append(pos)
        elif field == "#":
            candidates = []
            break
        elif field == ".":
            break

    return candidates


if __name__ == "__main__":
    grid = []

    robot_pos = None
    layout, movements = input.split("\n\n")
    for y, line in enumerate(layout.splitlines()):
        new_line = ""
        for x, field in enumerate(line):
            if field == "@":
                new_line += "@."
                robot_pos = (x * 2, y)
            elif field == "#" or field == ".":
                new_line += field * 2
            elif field == "O":
                new_line += "[]"

        grid.append(list(new_line))
    # print_grid(grid)

    movements = list(movements.replace("\n", ""))

    # print(len(get_all_box_coords(grid)))

    step = 0
    for movement in movements:
        # print("\033[H\033[xJ", end="")
        # print_grid(grid)
        # print(movement)
        direction = directions[movement]
        new_robot_pos = tuple(map(sum, zip(robot_pos, direction)))

        neighbour = get_grid_field(new_robot_pos)

        if movement == "<" or movement == ">":
            if neighbour == "[" or neighbour == "]":
                box_candidates = collect_box_candidates_horizontal(robot_pos, direction)
                if len(box_candidates) > 0:
                    for box_pos in box_candidates[::-1]:
                        new_box_pos = tuple(map(sum, zip(box_pos, direction)))
                        swap_grid_fields(box_pos, new_box_pos)
                    neighbour = get_grid_field(new_robot_pos)
        else:
            if neighbour == "[" or neighbour == "]":
                box_candidates = collect_box_candidates_vertical(robot_pos, direction)
                for boxes in box_candidates[::-1]:
                    for box_pos in boxes:
                        new_box_pos = tuple(map(sum, zip(box_pos, direction)))
                        swap_grid_fields(box_pos, new_box_pos)
                neighbour = get_grid_field(new_robot_pos)

        if neighbour == ".":
            swap_grid_fields(robot_pos, new_robot_pos)
            robot_pos = new_robot_pos

        # print(step)
        # print("\033[H\033[xJ", end="")
        # print_grid(grid)
        # print(movement)

        # keyboard.wait("space")

        step += 1

    # print_grid(grid)
    box_coords = get_all_box_coords(grid)
    # print(len(box_coords))
    sum_coords = sum(x + y * 100 for x, y in box_coords)
    print(sum_coords)
