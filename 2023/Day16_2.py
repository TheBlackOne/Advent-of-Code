import os

input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

directions = {
    'N': (0, -1),
    'W': (-1, 0),
    'S': (0, 1),
    'E': (1, 0)
}

element_direction_map = {
    '.': { 'N': ('N'), 'W': ('W'), 'S': ('S'), 'E': ('E')},
    '|': { 'N': ('N'), 'W': ('N', 'S'), 'S': ('S'), 'E': ('N', 'S') },
    '-': { 'N': ('E', 'W'), 'W': ('W'), 'S': ('E', 'W'), 'E': ('E') },
    '/': { 'N': ('E'), 'W': ('S'), 'S': ('W'), 'E': ('N') },
    "\\": { 'N': ('W'), 'W': ('N'), 'S': ('E'), 'E': ('S') }
}

map = []
energized_fields = set()
visited_elements_direction = []
max_x, max_y = 0, 0
num_energized_fields = 0

dir = os.path.dirname(__file__)
input_path = os.path.join(dir, "input.txt")
#with open(input_path) as f:
#   input = f.read()

def follow_beam(x, y, direction):
    while True:
        (step_x, step_y) = directions[direction]
        x += step_x
        y += step_y
        if x < 0 or x > max_x or y < 0 or y > max_y:
            break
        field = map[y][x]
        if field != '.':
            if (x, y, direction) in visited_elements_direction:
                break
            else:
                visited_elements_direction.append((x, y, direction))
        energized_fields.add((x, y))
        new_directions = element_direction_map[field][direction]
        direction = new_directions[0]
        for split_direction in new_directions[1:]:
            follow_beam(x, y, split_direction)

def start_beam(x, y, direction):
    global energized_fields
    global visited_elements_direction
    energized_fields = set()
    visited_elements_direction = []

    follow_beam(x, y, direction)

    global num_energized_fields
    num_energized_fields = max(num_energized_fields, len(energized_fields))
    

if __name__ == "__main__":
    for line in input.splitlines():
        map.append([c for c in line])

    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    

    direction = 'N'
    y = max_y + 1
    for x in range(max_x + 1):
        start_beam(x, y, direction)

    direction = 'S'
    y = -1
    for x in range(max_x + 1):
        start_beam(x, y, direction)

    direction = 'W'
    x = max_x + 1
    for y in range(max_y + 1):
        start_beam(x, y, direction)

    direction = 'E'
    x = -1
    for y in range(max_y + 1):
        start_beam(x, y, direction)    
    
    print(f"Energized fields: {num_energized_fields}")