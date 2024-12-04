input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]

# with open("input.txt") as f:
#    input = f.read()

chars = []
max_x = 0
max_y = 0


def retrieve(x, y, direction):
    dx, dy = direction
    result = ""

    debug_c = []

    if direction == (1, -1):
        pass

    for _ in range(3):
        x += dx
        y += dy
        if x > max_x:
            break
        elif x < 0:
            break
        if y > max_y:
            break
        elif y < 0:
            break
        result += chars[y][x]

        debug_c.append((x, y))

    return result


if __name__ == "__main__":
    chars = [list(line) for line in input.splitlines()]
    debug_chars = chars.copy()

    max_y = len(chars) - 1
    max_x = len(chars[0]) - 1

    num_found = 0
    for y in range(len(chars)):
        line = chars[y]
        for x in range(len(line)):
            char = line[x]
            if char == "X":
                for direction in directions:
                    test = retrieve(x, y, direction)
                    if test == "MAS":
                        num_found += 1

    print(num_found)
