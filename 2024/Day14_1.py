from collections import defaultdict
from math import prod

input = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

width = 11
height = 7
num_steps = 100

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    robots = []
    for line in input.splitlines():
        p, v = line.split(" ")
        x, y = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robots.append((x, y, vx, vy))

    new_robots = []
    for x, y, vx, vy in robots:
        x += vx * num_steps
        x = x % width

        y += vy * num_steps
        y = y % height
        new_robots.append((x, y))

    # grid_line = list("." * width)
    # grid = [grid_line.copy() for _ in range(height)]
    #
    # for x, y in new_robots:
    #    if grid[y][x] == ".":
    #        grid[y][x] = "1"
    #    else:
    #        grid[y][x] = str(int(grid[y][x]) + 1)

    quadrants = defaultdict(lambda: 0)
    left = width // 2
    top = height // 2
    for x, y in new_robots:
        if x == left or y == top:
            continue
        quadrant_key = (x < left, y < top)
        quadrants[quadrant_key] += 1

    safety_factor = prod(quadrants.values())
    print(safety_factor)
