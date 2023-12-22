from os import path

input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
#with open(input_path) as f:
#   input = f.read()

directions = {
    'N': (0, -1),
    'W': (-1, 0),
    'S': (0, 1),
    'E': (1, 0)
}


map = []
max_x, max_y = 0, 0
start = None
reached_fields = set()


def is_on_map(x, y):
    global max_x, max_y

    if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
        return True
    else:
        return False

if __name__ == "__main__":
    for y, line in enumerate(input.splitlines()):
        map.append([*line])

        if 'S' in line:
            x = line.index('S')
            start = (x, y)

    max_x = len(map[0]) - 1
    max_y = len(map) - 1

    x, y = start
    map[y][x] = '.'
    reached_fields.add(start)

    for step in range(6):
        new_reached_fields = set()
        for x, y in reached_fields:
            for step_x, step_y in directions.values():
                check_x = x + step_x
                check_y = y + step_y

                if is_on_map(check_x, check_y):
                    if map[check_y][check_x] == '.':
                        new_reached_fields.add((check_x, check_y))
        reached_fields = new_reached_fields
    
    result = len(reached_fields)
    print(result)