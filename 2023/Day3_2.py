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
gear_candidates = {}


def search_symbol(match, y):
    for search_x in range(match.start() - 1, match.end() + 1):
        if search_x < 0:
            continue
        for search_y in range(y - 1, y + 2):
            if search_y < 0:
                continue
            # print(f"{search_x} / {search_y}")
            if (search_x, search_y) in symbol_coords:
                if (search_x, search_y) not in gear_candidates.keys():
                    gear_candidates[(search_x, search_y)] = [int(match.group())]
                else:
                    gear_candidates[(search_x, search_y)].append(int(match.group()))
    # print("===========")


def parse_part_numbers(line, y):
    for match in list(re.finditer(r"\d+", line)):
        search_symbol(match, y)


if __name__ == "__main__":
    y = 0
    for line in input.splitlines():
        for match in re.finditer(r"\*", line):
            symbol_coords.append((match.start(), y))
        y += 1

    y = 0
    for line in input.splitlines():
        parse_part_numbers(line, y)
        y += 1

    result = 0
    for numbers in gear_candidates.values():
        if len(numbers) == 2:
            result += numbers[0] * numbers[1]

    print(f"Result: {result}")
