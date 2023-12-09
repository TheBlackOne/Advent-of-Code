from itertools import pairwise

input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

# with open('input.txt') as f:
#    input = f.read()

values = []

if __name__ == "__main__":
    for line in input.splitlines():
        line_values = [int(v) for v in line.split()]
        values.append(line_values)

    histories = 0

    for line_values in values:
        extrapolation_data = []
        extrapolation_data.append(line_values)

        while True:
            diffs = [y-x for (x, y) in pairwise(extrapolation_data[-1])]
            extrapolation_data.append(diffs)

            if all(d == 0 for d in diffs):
                break

        last_history = extrapolation_data[-1][0]
        for extrapolations in extrapolation_data[::-1][1:]:
            last_history = extrapolations[0] - last_history

        histories += last_history

    print(f"Sum of histories: {histories}")
