from os import path
from tqdm import tqdm

input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

input = """...........
......##.#.
.###..#..#.
..#.#...#..
....#.#....
.....S.....
.##......#.
.......##..
.##.#.####.
.##...#.##.
..........."""

total_steps = 26501365

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
with open(input_path) as f:
    input = f.read()

directions = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0)}


map = []
max_x, max_y = 0, 0
start = None
reached_fields = set()
board_size = 0

quadrant_counters = []


def print_to_file():
    global map
    global reached_fields
    global start

    local_map = map.copy()
    for x, y in reached_fields:
        local_map[y][x] = "O"

    x, y = start
    local_map[y][x] = "S"

    with open("map.txt", "w") as f:
        for line in local_map:
            f.write("".join([*line]))
            f.write("\n")


def board_grid_to_map_coords(x, y):
    global board_size

    x = x * board_size
    y = y * board_size

    return (x, y)


def count_reached_in_range(x, y):
    global board_size

    result = 0

    for reached_x, reached_y in reached_fields:
        if (
            reached_x >= x
            and reached_x < x + board_size
            and reached_y >= y
            and reached_y < y + board_size
        ):
            result += 1

    return result


def triangle_number(n):
    return (n * n + n) // 2


def is_on_map(x, y):
    global max_x, max_y

    if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
        return True
    else:
        return False


if __name__ == "__main__":
    repeat = 9

    for y, line in enumerate(input.splitlines()):
        if "S" in line:
            line = line.replace("S", ".")

        line = [*line]
        map.append(line)

    board_size = len(map)

    new_map = []
    for _ in range(repeat):
        for line in map:
            new_map.append(line * repeat)

    map = new_map

    max_x = len(map[0]) - 1
    max_y = len(map) - 1

    start = ((max_x + 1) // 2, (max_y + 1) // 2)
    x, y = start
    map[y][x] = "S"

    reached_fields.add(start)

    steps = board_size * ((repeat - 1) // 2) + ((board_size - 1) // 2)

    for step in tqdm(range(steps), ascii=True):
        new_reached_fields = set()
        for x, y in reached_fields:
            for step_x, step_y in directions.values():
                check_x = x + step_x
                check_y = y + step_y

                if is_on_map(check_x, check_y):
                    if map[check_y][check_x] != "#":
                        new_reached_fields.add((check_x, check_y))
        reached_fields = new_reached_fields

    print_to_file()

    board_grid_max = repeat - 1
    board_grid_mid = board_grid_max // 2

    total_fields = 0

    # total_steps = steps

    n = total_steps // board_size
    num_outer_partial_boards = n
    num_inner_partial_boards = num_outer_partial_boards - 1

    print(f"N: {n}")
    print(f"Number of outer partial boards: {num_outer_partial_boards}")
    print(f"Number of inner partial boards: {num_inner_partial_boards}")

    # collect fields of all four tip boards
    corner_board_grid_coords = [
        (0, board_grid_mid),
        (board_grid_mid, 0),
        (board_grid_max, board_grid_mid),
        (board_grid_mid, board_grid_max),
    ]

    for board_grid_x, board_grid_y in corner_board_grid_coords:
        (x, y) = board_grid_to_map_coords(board_grid_x, board_grid_y)
        total_fields += count_reached_in_range(x, y)

    # collect all four variants of "outer" partial boards
    outer_partial_fields = 0
    outer_partial_coords = [
        (0, board_grid_mid - 1),
        (board_grid_max, board_grid_mid - 1),
        (0, board_grid_mid + 1),
        (board_grid_max, board_grid_mid + 1),
    ]

    for board_grid_x, board_grid_y in outer_partial_coords:
        (x, y) = board_grid_to_map_coords(board_grid_x, board_grid_y)
        outer_partial_fields += count_reached_in_range(x, y) * num_outer_partial_boards

    # collect all four variants of "inner" partial boards
    inner_partial_fields = 0
    inner_partial_coords = [
        (1, board_grid_mid - 1),
        (board_grid_max - 1, board_grid_mid - 1),
        (1, board_grid_mid + 1),
        (board_grid_max - 1, board_grid_mid + 1),
    ]

    for board_grid_x, board_grid_y in inner_partial_coords:
        (x, y) = board_grid_to_map_coords(board_grid_x, board_grid_y)
        inner_partial_fields += count_reached_in_range(x, y) * num_inner_partial_boards

    total_fields += outer_partial_fields
    total_fields += inner_partial_fields

    # number of start and non-start boards
    corner_n = n - 2
    num_corner_boards = triangle_number(corner_n)

    print(f"Corner-N: {corner_n}")
    print(f"Number corner boards: {num_corner_boards}")

    num_start_boards = (num_corner_boards // corner_n) ** 2
    num_non_start_boards = num_corner_boards - num_start_boards

    print(f"Number corner start-boards: {num_start_boards}")
    print(f"Number corner non-start-boards: {num_non_start_boards}")

    # add start boards of straight lanes
    num_lane_boards = (n - 1) // 2
    num_start_boards += num_lane_boards
    print(f"Number start lane boards: {num_lane_boards}")
    num_start_boards *= 4

    # add non-start boards of straight lanes
    num_lane_boards = n // 2
    print(f"Number non-start lane boards: {num_lane_boards}")
    num_non_start_boards += num_lane_boards

    num_non_start_boards *= 4

    # add middle board
    num_start_boards += 1

    print(f"Total inner boards: {num_start_boards + num_non_start_boards}")

    # non-start fields
    (x, y) = board_grid_to_map_coords(board_grid_mid + 1, board_grid_mid)
    non_start_fields = count_reached_in_range(x, y)
    total_fields += non_start_fields * num_non_start_boards

    # start fields
    (x, y) = board_grid_to_map_coords(board_grid_mid, board_grid_mid)
    start_fields = count_reached_in_range(x, y)
    total_fields += start_fields * num_start_boards

    print(total_fields)
