import networkx as nx

input = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

# with open("input.txt") as f:
#    input = f.read()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def manhattan_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return abs(x1 - x2) + abs(y1 - y2)


def get_grid_field(pos, grid):
    global grid_size
    result = None

    x, y = pos
    if x in range(len(grid[0])) and y in range(len(grid)):
        result = grid[y][x]

    return result


if __name__ == "__main__":
    start = None
    end = None
    grid = []

    for y, line in enumerate(input.splitlines()):
        grid.append(list(line))
        if "S" in line:
            x = line.index("S")
            start = (x, y)
        elif "E" in line:
            x = line.index("E")
            end = (x, y)

    width = len(grid[0])
    height = len(grid)

    G = nx.grid_graph((width, height))

    for y, line in enumerate(grid):
        for x, field in enumerate(line):
            if field == "#":
                G.remove_node((x, y))

    path = nx.shortest_path(G, start, end)
    original_length = len(path) - 1
    shortcuts_found = 0
    min_dist_saved = 76
    cheat_length = 20

    for index, pos in enumerate(path):
        for found_index, end_pos in enumerate(
            path[index + min_dist_saved :],
            index + min_dist_saved,
        ):
            dist = manhattan_distance(pos, end_pos)
            if dist <= cheat_length:
                dist_saved = found_index - index - dist
                if dist_saved >= min_dist_saved:
                    shortcuts_found += 1

    print(shortcuts_found)
