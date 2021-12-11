import numpy as np
from colorama import Fore, Style

octopi = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        octopi.append([int(_) for _ in line.strip()])

octopi = np.asarray(octopi)
max = len(octopi)

def get_neighbours(_row, _col):
    rows = []
    cols = []

    for col in [_col-1, _col, _col+1]:
        for row in [_row-1, _row, _row+1]:
            if row >= 0 and row < max and col >= 0 and col < max:
                if octopi[row][col] >= 0:
                    rows.append(row)
                    cols.append(col)
    return (rows, cols)

step = 1
while True:
    octopi += 1
    while True:
        flashing = np.where(octopi > 9)
        if len(flashing[0]) == 0: break

        octopi[octopi > 9] = -1

        for row, col in zip(*flashing):
            neighbours = get_neighbours(row, col)
            np.add.at(octopi, (neighbours[0], neighbours[1]), 1)

    octopi[octopi < 0] = 0
    
    if np.all(octopi == 0):
        print(step)
        break
    
    step += 1