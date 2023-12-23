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
longest_path = 0
last_crossing = None

def print_to_file(path):
    global map

    with open("map.txt", "w", encoding="utf-8") as f:
        for y, line in enumerate(map):
            for x, field in enumerate(line):
                if field == '.':
                    field = ' '
                elif field == '#':
                    field = "█"
                if (x, y) in path:
                    field = 'o'
                f.write(field)
            f.write('\n')
        

def follow_path(path, position, last_position, visited_crossings):
    global last_crossing
    global longest_path

    while True:            
        path.append(position)

        if position == destination:
            path_length = len(path) - 1
            longest_path = max([longest_path, path_length])
            last_crossing = visited_crossings[-1]
            print(f"Path found! {longest_path}")
            return
        
        next_fields = []
        x, y = position
        for delta_x, delta_y in directions.values():
            test_x = x + delta_x
            test_y = y + delta_y
            test_coords = (test_x, test_y)
            if test_coords != last_position and test_coords not in visited_crossings:
                test_field = map[test_y][test_x]
                if  test_field != '#':
                    next_fields.append(test_coords)

        if len(next_fields) == 0:
            #print(f"Dead end found at {position}!")
            return
        else:
            last_position = position
            
            if len(next_fields) > 1:
                visited_crossings.append(position)            
            
            for next_field in next_fields[1:]:
                if last_position == last_crossing:
                    continue
                #print_to_file(path)
                #print(f"Crossing found at {position}! Following {next_field}")
                follow_path(path.copy(), next_field, last_position, visited_crossings.copy())

            if last_position == last_crossing:
                last_crossing = None
                return
            position = next_fields[0]



if __name__ == "__main__":
    for line in input.splitlines():
        map.append([_ for _ in [*line]])
    
    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    destination = (max_x - 1, max_y)

    follow_path([], start, (1, -1), [])

    print(longest_path)