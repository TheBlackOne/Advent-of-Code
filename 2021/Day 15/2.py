from functools import total_ordering
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

import numpy as np

from datetime import datetime

cave = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        cave.append([int(_) for _ in line.strip()])

original_cave = np.asarray(cave)
extended_cave = np.asarray(cave)
for _ in range(4):
    original_cave += 1
    original_cave[original_cave == 10] = 1
    extended_cave = np.concatenate((extended_cave, original_cave), axis=1)

original_cave = extended_cave.copy()
for _ in range(4):
    original_cave += 1
    original_cave[original_cave == 10] = 1
    extended_cave = np.concatenate((extended_cave, original_cave), axis=0)

grid = Grid(matrix=extended_cave)

start = grid.node(0, 0)
end = grid.node(len(extended_cave) - 1, len(extended_cave) - 1)

start_time = datetime.now()

finder = DijkstraFinder(diagonal_movement=DiagonalMovement.never)

path, runs = finder.find_path(start, end, grid)

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

total_risk = 0
for x, y in path[1:]:
    total_risk += extended_cave[y][x]

print('operations:', runs, 'path length:', len(path))
#print(grid.grid_str(path=path, start=start, end=end))

print(total_risk)