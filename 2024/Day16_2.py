from copy import deepcopy

import networkx as nx

input = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

# with open("input.txt") as f:
#    input = f.read()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def rotate_90(direction):
    dx, dy = direction
    return (-dy, dx)


def print_grid_path(grid, all_paths):
    grid = deepcopy(grid)
    for path in all_paths:
        for x, y in path:
            grid[y][x] = "O"

        for line in grid:
            line = "".join(line)
            print(line)


def get_grid_field(pos, grid):
    result = None

    x, y = pos
    if 0 < x < len(grid[0]) and 0 < y < len(grid):
        result = grid[y][x]

    return result


if __name__ == "__main__":
    start = None
    end = None
    start_direction = directions[1]
    grid = []

    for y, line in enumerate(input.splitlines()):
        grid.append(list(line))
        if "S" in line:
            x = line.index("S")
            start = (x, y)
            grid[y][x] = "."
        elif "E" in line:
            x = line.index("E")
            end = (x, y)
            grid[y][x] = "."

    G = nx.DiGraph()
    overstepped_fields = {}
    for y, line in enumerate(grid):
        for x, field in enumerate(line):
            if field == ".":
                pos = (x, y)
                G.add_node(pos)

                for direction in directions:
                    corner_found = False
                    new_pos = tuple(map(sum, zip(pos, direction)))
                    if get_grid_field(new_pos, grid) == ".":
                        # special case: from start to a direction different than east
                        if pos == start and direction != start_direction:
                            G.add_edge(pos, new_pos, weight=1001)
                        # special case: next field is end field
                        elif new_pos == end:
                            G.add_edge(pos, new_pos, weight=1)
                        else:
                            right_direction = rotate_90(direction)
                            right_pos = tuple(map(sum, zip(new_pos, right_direction)))
                            if get_grid_field(right_pos, grid) == ".":
                                G.add_edge(pos, right_pos, weight=1002)
                                corner_found = True
                                overstepped_fields[(pos, right_pos)] = new_pos

                            left_direction = rotate_90(rotate_90(right_direction))
                            left_pos = tuple(map(sum, zip(new_pos, left_direction)))
                            if get_grid_field(left_pos, grid) == ".":
                                G.add_edge(pos, left_pos, weight=1002)
                                corner_found = True
                                overstepped_fields[(pos, left_pos)] = new_pos

                            if corner_found:
                                further_pos = tuple(map(sum, zip(new_pos, direction)))
                                if get_grid_field(further_pos, grid) == ".":
                                    G.add_edge(pos, further_pos, weight=2)
                                    overstepped_fields[(pos, further_pos)] = new_pos
                            else:
                                G.add_edge(pos, new_pos, weight=1)

    visited_fields = set()
    all_paths = nx.all_shortest_paths(G, start, end, weight="weight")
    for path in all_paths:
        for n1, n2 in zip(path[:-1], path[1:]):
            visited_fields.add(n1)
            visited_fields.add(n2)
            if (n1, n2) in overstepped_fields.keys():
                visited_fields.add(overstepped_fields[(n1, n2)])

    print(len(visited_fields))
