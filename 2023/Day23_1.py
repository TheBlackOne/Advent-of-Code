from os import path

input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
with open(input_path) as f:
   input = f.read()

directions = {
    'N': (0, -1),
    'W': (-1, 0),
    'S': (0, 1),
    'E': (1, 0)
}

slopes = {
    '^': 'N',
    '<': 'W',
    'v': 'S',
    '>': 'E'
}

map = []
start = (1, 0)
destination = None
paths = []

def follow_path(path, position):
    while True:            
        path.append(position)

        if position == destination:
            paths.append(path)
            return
        
        next_fields = []
        x, y = position
        for direction, (delta_x, delta_y) in directions.items():
            test_x = x + delta_x
            test_y = y + delta_y
            if (test_x, test_y) not in path:
                test_field = map[test_y][test_x]
                if  test_field == '.':
                    next_fields.append((test_x, test_y))
                elif test_field in slopes.keys():
                    if slopes[test_field] == direction:
                        next_fields.append((test_x, test_y))

        if len(next_fields) == 0:
            return
        
        for next_field in next_fields[1:]:
            follow_path(path.copy(), next_field)

        position = next_fields[0]



if __name__ == "__main__":
    for line in input.splitlines():
        map.append([_ for _ in [*line]])
    
    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    destination = (max_x - 1, max_y)

    follow_path([], start)

    longest_path = max([len(p) - 1 for p in paths])
    print(longest_path)