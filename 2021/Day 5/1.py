import numpy as np

lines = []

with open('input.txt', 'r') as file:
    for line in [line.strip() for line in file.readlines()]:
        start, end = line.split(' -> ')
        x1, y1 = [int(_) for _ in start.split(',')]
        x2, y2 = [int(_) for _ in end.split(',')]

        if x1 == x2 or y1 == y2:
            lines.append([(x1, y1), (x2, y2)])

lines = np.array(lines)
lines_map = np.zeros((lines.max() + 1, lines.max() + 1))

for start, end in lines:
    x1, y1 = start
    x2, y2 = end

    step_x = 0
    if x2 > x1: step_x = 1
    elif x2 < x1: step_x = -1

    step_y = 0
    if y2 > y1: step_y = 1
    elif y2 < y1: step_y = -1

    delta = max(abs(x2 - x1), abs(y2 - y1))
    x = x1
    y = y1

    for _ in range(0, delta + 1):
        lines_map[x, y] += 1
        x += step_x
        y += step_y

result = len(np.where(lines_map > 1)[0])

print(result)