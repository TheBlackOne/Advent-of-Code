from copy import deepcopy

import networkx as nx

input = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

# with open("input.txt") as f:
#    input = f.read()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
grid_size = 7


def print_grid_path(grid, all_paths):
    grid = deepcopy(grid)
    for path in all_paths:
        for x, y in path:
            grid[y][x] = "O"

    for line in grid:
        line = "".join(line)
        print(line)


def get_grid_field(pos, grid):
    global grid_size
    result = None

    x, y = pos
    if x in range(grid_size) and y in range(grid_size):
        # if 0 < x < len(grid[0]) and 0 < y < len(grid):
        result = grid[y][x]

    return result


if __name__ == "__main__":
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    grid = []

    for _ in range(grid_size):
        grid.append(list("." * grid_size))

    byte_stack = []
    for line in input.splitlines():
        x, y = line.split(",")
        byte_stack.append((int(x), int(y)))

    G = nx.Graph()
    for y, line in enumerate(grid):
        for x, field in enumerate(line):
            if field == ".":
                pos = (x, y)
                G.add_node(pos)

                for direction in directions:
                    new_pos = tuple(map(sum, zip(pos, direction)))
                    if get_grid_field(new_pos, grid) == ".":
                        G.add_edge(pos, new_pos)

    # print_grid_path(grid, [[]])

    for block in byte_stack:
        G.remove_node(block)
        if not nx.has_path(G, start, end):
            print(",".join(map(str, block)))
            break
