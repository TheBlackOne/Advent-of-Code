input = """AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA"""

# with open("input.txt") as f:
#    input = f.read()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_whole_plot(plant, pos, plots, found):
    global limits

    x, y = pos
    for direction in directions:
        dx, dy = direction
        new_x = x + dx
        new_y = y + dy

        if (new_x, new_y) not in found:
            if all(p in lim for p, lim in zip([new_x, new_y], limits)):
                if plots[new_y][new_x] == plant:
                    new_pos = (new_x, new_y)
                    found.add(new_pos)
                    found.update(get_whole_plot(plant, new_pos, plots, found))
    return found


def get_num_neighbours(pos, plot):
    num = 0
    x, y = pos
    for direction in directions:
        dx, dy = direction
        new_x = x + dx
        new_y = y + dy
        if (new_x, new_y) in plot:
            num += 1

    return num


def get_plant(x, y, plots, plot):
    global limits

    plant = None

    if all(p in lim for p, lim in zip([x, y], limits)):
        if (x, y) in plot:
            plant = plots[y][x]

    return plant


if __name__ == "__main__":
    plots = list(map(list, [line for line in input.splitlines()]))

    max_x = len(plots[0])
    max_y = len(plots)
    limits = [range(max_x), range(max_y)]
    visited = set()
    plots_identified = {}

    for y in limits[1]:
        for x in limits[0]:
            start = (x, y)
            if start not in visited:
                plant = plots[y][x]
                found = set()
                found.add(start)
                found = get_whole_plot(plant, (x, y), plots, found)
                plots_identified[start] = found
                visited.update(found)

    diagonals = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    areas_sides = []
    for start, plot in plots_identified.items():
        num_lines = 0
        for pos in plot:
            num_neighbours = get_num_neighbours(pos, plot)
            # Single plant, accounts for 4 sides
            if num_neighbours == 0:
                num_lines += 4
            # Detect a tip of a row, accounts for 2 sides
            elif num_neighbours == 1:
                num_lines += 2
            else:
                x, y = pos
                plant = plots[y][x]
                for diagonal in diagonals:
                    dx, dy = diagonal
                    new_x = x + dx
                    new_y = y + dy

                    diagonal_plant = get_plant(new_x, new_y, plots, plot)
                    plant1 = get_plant(new_x, y, plots, plot)
                    plant2 = get_plant(x, new_y, plots, plot)

                    # If plant on diagonal position is different
                    # Either inside or outside corner
                    if diagonal_plant != plant:
                        # Inside corner
                        if plant1 == plant and plant2 == plant:
                            num_lines += 1
                        # Outside corner
                        elif plant1 != plant and plant2 != plant:
                            num_lines += 1
                    # Special case:
                    # Plant on diagonal position is the same and
                    # the neighbouring plants are different
                    # the diagonal A in the middle
                    #
                    # AAAAAA
                    # AAABBA
                    # AAABBA
                    # ABBAAA
                    # ABBAAA
                    # AAAAAA
                    #
                    elif plant1 != plant and plant2 != plant:
                        num_lines += 1
        areas_sides.append((len(plot), num_lines))
        # print(f"{len(plot)}, {num_lines}")

    result = sum(a * p for a, p in areas_sides)
    print(result)
