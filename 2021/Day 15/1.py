from functools import total_ordering
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

cave = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        cave.append([int(_) for _ in line.strip()])

grid = Grid(matrix=cave)

start = grid.node(0, 0)
end = grid.node(len(cave) - 1, len(cave) - 1)

finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

path, runs = finder.find_path(start, end, grid)

total_risk = 0
for x, y in path[1:]:
    total_risk += cave[y][x]

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))

print(total_risk)