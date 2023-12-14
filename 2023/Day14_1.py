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


def get_lowest_free_field(x, y):
    result = y
    for check_y in range(y, -1, -1):
        if check_y == y:
            continue
        if data[check_y][x] == ".":
            result = check_y
        else:
            break
    return result


if __name__ == "__main__":
    for line in input.splitlines():
        data_line = [c for c in line]
        data.append(data_line)

    for x in range(len(data[0])):
        for y in range(len(data)):
            if data[y][x] == "O":
                lowest_free_y = get_lowest_free_field(x, y)
                if lowest_free_y != y:
                    data[lowest_free_y][x] = "O"
                    data[y][x] = "."

    sums = 0

    data = data[::-1]
    for y in range(len(data)):
        line = data[y]
        num = line.count("O")
        sums += num * (y + 1)

    print(f"Result: {sums}")
