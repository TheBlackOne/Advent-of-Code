from collections import defaultdict

input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

# with open("input.txt") as f:
#    input = f.read()

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def walk(trailhead, pos, grid):
    global limits
    global trailhead_summit

    x, y = pos
    score = grid[y][x]
    target_score = str(int(score) + 1)

    for direction in directions:
        dx, dy = direction
        new_x = x + dx
        new_y = y + dy

        if all(p in lim for p, lim in zip([new_x, new_y], limits)):
            if grid[new_y][new_x] == target_score:
                if target_score == "9":
                    trailhead_summit[trailhead] += 1
                else:
                    walk(trailhead, (new_x, new_y), grid)


if __name__ == "__main__":
    input = input.splitlines()
    max_x = len(input[0])
    max_y = len(input)
    limits = [range(max_x), range(max_y)]
    grid = []
    trailheads = set()
    trailhead_summit = defaultdict(lambda: 0)

    for y, line in enumerate(input):
        new_list = list(line)
        grid.append(new_list)
        for x, c in enumerate(new_list):
            if c == "0":
                trailheads.add((x, y))

    for start in trailheads:
        walk(start, start, grid)

    print(sum(trailhead_summit.values()))
