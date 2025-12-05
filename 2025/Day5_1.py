input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

#with open("input.txt") as f:
#   input = f.read()

fresh_ranges = []
num_fresh = 0

if __name__ == "__main__":
    fresh_lines, ingredients_lines = input.split('\n\n')
    for fresh_line in fresh_lines.splitlines():
        start, stop = [int(f) for f in fresh_line.split('-')]
        fresh_ranges.append(range(start, stop + 1))

    for ingredient_line in ingredients_lines.splitlines():
        for fresh_range in fresh_ranges:
            if int(ingredient_line) in fresh_range:
                num_fresh += 1
                break

    print(num_fresh)
