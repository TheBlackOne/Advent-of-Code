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


def get_grid_field(pos, grid):
    global grid_size
    result = None

    x, y = pos
    if x in range(len(grid[0])) and y in range(len(grid)):
        result = grid[y][x]

    return result


def get_neighbour_positions(pos):
    result = []
    for direction in directions:
        new_pos = tuple(map(sum, zip(pos, direction)))
        result.append(new_pos)
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
    for index, pos in enumerate(path):
        for direction in directions:
            new_pos = tuple(map(sum, zip(pos, direction)))
            if get_grid_field(new_pos, grid) == "#":
                new_pos = tuple(map(sum, zip(new_pos, direction)))
                try:
                    found_index = path.index(new_pos, index)
                    saved_length = found_index - index - 2
                    if saved_length >= 100:
                        shortcuts_found += 1
                except ValueError:
                    pass

    print(shortcuts_found)
