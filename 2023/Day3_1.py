import re

input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# with open('input.txt') as f:
#    input = f.read()

symbol_coords = []
part_numbers = []


def search_symbol(match, y):
    for search_x in range(match.start() - 1, match.end() + 1):
        if search_x < 0:
            continue
        for search_y in range(y - 1, y + 2):
            if search_y < 0:
                continue
            # print(f"{search_x} / {search_y}")
            if (search_x, search_y) in symbol_coords:
                part_numbers.append(int(match.group()))
                return
    # print("===========")


def parse_part_numbers(line, y):
    for match in list(re.finditer(r'\d+', line)):
        search_symbol(match, y)
        # print(match.group())


if __name__ == "__main__":
    y = 0
    for line in input.splitlines():
        for match in re.finditer(r'[^\d\.]', line):
            symbol_coords.append((match.start(), y))
        y += 1

    y = 0
    for line in input.splitlines():
        parse_part_numbers(line, y)
        y += 1

    result = sum(part_numbers)

    # print(part_numbers)
    print(f"Result: {result}")
