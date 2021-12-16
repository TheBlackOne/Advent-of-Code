import numpy as np


with open('input.txt', 'r') as file:
    coordinates = []
    part1, part2 = file.read().split('\n\n')

    for line in part1.split():
        coordinate = line.strip().split(',')[::-1]
        coordinates.append(coordinate)

    folds = []
    for line in part2.split('\n'):
        axis = 0
        fold_along, number = line.strip().split('=')
        if 'x' in fold_along: axis = 1
        folds.append((axis, int(number)))


coordinates = np.asarray(coordinates, dtype=int)
max_y, max_x = np.max(coordinates, axis=0)

sheet = np.zeros((max_y + 1, max_x + 1), dtype=bool)
sheet[tuple(coordinates.T)] = True

for axis, number in folds:
    remaining, _, to_cover = np.split(sheet, [number, number + 1], axis)
    to_cover = np.flip(to_cover, axis)

    size_remaining = remaining.shape[axis]
    size_to_cover = to_cover.shape[axis]
    diff = abs(size_remaining - size_to_cover)
    
    if size_remaining < size_to_cover:
        to_insert = np.zeros(remaining.T.shape[axis], dtype=bool)
        remaining = np.insert(remaining, 0, to_insert, axis=axis)
    elif size_to_cover < size_remaining:
        to_insert = np.zeros(to_cover.T.shape[axis], dtype=bool)
        to_cover = np.insert(to_cover, 0, to_insert, axis=axis)

    sheet = remaining | to_cover

for line in sheet.astype(int):
    string_line = ""
    for c in line:
        if c: string_line += 'X '
        else: string_line += '  '
    print(string_line)