from tqdm import tqdm

input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

# with open("input.txt") as f:
#    input = f.read()

data = []


def calc_load():
    global data
    sums = 0

    local_data = data[::-1]
    for y in range(len(local_data)):
        line = local_data[y]
        num = line.count("O")
        sums += num * (y + 1)
    return sums


def get_lowest_field_N(x, y):
    result = y
    for check_y in range(y, -1, -1):
        if check_y == y:
            continue
        if data[check_y][x] == ".":
            result = check_y
        else:
            break
    return result


def get_lowest_field_S(x, y):
    global data
    max_y = len(data)
    result = y
    for check_y in range(y, max_y):
        if check_y == y:
            continue
        if data[check_y][x] == ".":
            result = check_y
        else:
            break
    return result


def get_lowest_field_W(x, y):
    result = x
    for check_x in range(x, -1, -1):
        if check_x == x:
            continue
        if data[y][check_x] == ".":
            result = check_x
        else:
            break
    return result


def get_lowest_field_E(x, y):
    global data
    max_x = len(data)
    result = x
    for check_x in range(x, max_x):
        if check_x == x:
            continue
        if data[y][check_x] == ".":
            result = check_x
        else:
            break
    return result


if __name__ == "__main__":
    results = []
    found = False

    for line in input.splitlines():
        data_line = [c for c in line]
        data.append(data_line)

    for cycle in tqdm(range(1000)):
        for direction in ["N", "W", "S", "E"]:
            all_x = range(len(data[0]))
            if direction == "E":
                all_x = range(len(data[0]) - 1, -1, -1)
            for x in all_x:
                all_y = range(len(data))
                if direction == "S":
                    all_y = range(len(data) - 1, -1, -1)
                for y in all_y:
                    if data[y][x] == "O":
                        next_free_x = x
                        next_free_y = y
                        if direction == "N":
                            next_free_y = get_lowest_field_N(x, y)
                        elif direction == "W":
                            next_free_x = get_lowest_field_W(x, y)
                        elif direction == "S":
                            next_free_y = get_lowest_field_S(x, y)
                        else:
                            next_free_x = get_lowest_field_E(x, y)

                        if next_free_x != x or next_free_y != y:
                            data[next_free_y][next_free_x] = "O"
                            data[y][x] = "."

        result = calc_load()
        results.append(result)
    counts = {}
    for result in results:
        if result not in counts.keys():
            counts[result] = results.count(result)

    with open("counts.txt", "w") as f:
        for key, value in counts.items():
            f.write("%s:%s\n" % (key, value))

    with open("results.txt", "w") as fp:
        fp.write("\n".join([str(r) for r in results]))
