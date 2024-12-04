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

# with open("input.txt") as f:
#    input = f.read()

chars = []
max_x = 0
max_y = 0


if __name__ == "__main__":
    chars = [list(line) for line in input.splitlines()]
    debug_chars = chars.copy()

    num_found = 0
    for y in range(1, len(chars) - 1):
        line = chars[y]
        for x in range(1, len(line) - 1):
            char = line[x]
            if char == "A":
                test1 = chars[y - 1][x - 1] + "A" + chars[y + 1][x + 1]
                if test1 == "MAS" or test1 == "SAM":
                    test2 = chars[y - 1][x + 1] + "A" + chars[y + 1][x - 1]
                    if test2 == "MAS" or test2 == "SAM":
                        num_found += 1

    print(num_found)
