import itertools

input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

grid = []

neighbours = list(itertools.product([-1, 0, 1], [-1, 0, 1]))

#with open("input.txt") as f:
#   input = f.read()

if __name__ == "__main__":
    for line in input.splitlines():
        new_row = []
        for cell in line:
            new_row.append(cell)
        grid.append(new_row)

    num_accessible = 0

    max_x = len(grid[0])
    max_y = len(grid)

    for y in range(max_y):
        for x in range(max_x):
            if grid[y][x] == '@':
                num_free_neighbours = 0
                for dx, dy in neighbours:
                    if dx == 0 and dy == 0: continue

                    neihgbour_x = x + dx
                    neighbour_y = y + dy

                    if neihgbour_x < 0 or neighbour_y < 0 or neihgbour_x >= max_x or neighbour_y >= max_y:
                        num_free_neighbours += 1
                        continue
                    if grid[neighbour_y][neihgbour_x] == '.':
                        num_free_neighbours += 1
                if num_free_neighbours >= 5:
                    num_accessible += 1

    print(num_accessible)