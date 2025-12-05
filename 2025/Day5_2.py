import multirange as mr

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

if __name__ == "__main__":
    fresh_lines, _ = input.split('\n\n')
    for fresh_line in fresh_lines.splitlines():
        start, stop = [int(f) for f in fresh_line.split('-')]
        fresh_ranges.append(range(start, stop + 1))

    normalized_ranges = mr.normalize_multi(fresh_ranges)

    print(sum([len(r) for r in normalized_ranges]))
