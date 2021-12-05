import numpy as np

lines = []
max_dimension = 0

with open('input.txt', 'r') as file:
    for line in [line.strip() for line in file.readlines()]:
        start, end = line.split(' -> ')
        x1, y1 = [int(_) for _ in start.split(',')]
        x2, y2 = [int(_) for _ in end.split(',')]

        delta_x = abs(x1 - x2)
        delta_y = abs(y1 - y2)

        if delta_x == 0 or delta_y == 0 or delta_x == delta_y:
            line_coords = np.linspace([x1, y1], [x2, y2], max(delta_x, delta_y) + 1).astype(int)
            max_dimension = max(max_dimension, line_coords.max())
            lines.append(line_coords)

lines_map = np.zeros((max_dimension + 1, max_dimension + 1))

for line_coords in lines:
    for x, y in line_coords:
        lines_map[x, y] += 1

result = len(np.where(lines_map > 1)[0])

print(result)