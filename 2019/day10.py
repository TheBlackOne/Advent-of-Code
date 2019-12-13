import math

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

def get_normalized_vector(vector):
    dx, dy = vector

    if dx == 0:
        dx = 0
        dy /= abs(dy)
    elif dy == 0:
        dx /= abs(dx)
        dy = 0
    else:
        divisor = abs(dx)
        if abs(dy) < abs(dx): divisor = abs(dy)
        
        if abs(dx) > 1 and abs(dy) > 1:
            dx /= divisor
            dy /= divisor

    return (dx, dy)

visible_closest = {}
def normalize_vectors(vectors, store_closest = False):
    result = set()
    for vector in vectors:
        normalized = get_normalized_vector(vector)
        if normalized not in result:
            result.add(normalized)

        if store_closest:
            if normalized in visible_closest.keys():
                x1, y1 = visible_closest[normalized]
                distance1 = x1*x1 + y1*y1
                x2, y2 = vector
                distance2 = x2*x2 + y2*y2
                if distance2 < distance1:
                    visible_closest[normalized] = vector
            else:
                visible_closest[normalized] = vector

    return result

def calc_angle(vector):
    x, y = vector
    angle = math.atan2(-x, y)
    angle += math.pi

    if angle == 2*math.pi: angle = 0

    return angle

asteroid_map = """..#..###....#####....###........#
.##.##...#.#.......#......##....#
#..#..##.#..###...##....#......##
..####...#..##...####.#.......#.#
...#.#.....##...#.####.#.###.#..#
#..#..##.#.#.####.#.###.#.##.....
#.##...##.....##.#......#.....##.
.#..##.##.#..#....#...#...#...##.
.#..#.....###.#..##.###.##.......
.##...#..#####.#.#......####.....
..##.#.#.#.###..#...#.#..##.#....
.....#....#....##.####....#......
.#..##.#.........#..#......###..#
#.##....#.#..#.#....#.###...#....
.##...##..#.#.#...###..#.#.#..###
.#..##..##...##...#.#.#...#..#.#.
.#..#..##.##...###.##.#......#...
...#.....###.....#....#..#....#..
.#...###..#......#.##.#...#.####.
....#.##...##.#...#........#.#...
..#.##....#..#.......##.##.....#.
.#.#....###.#.#.#.#.#............
#....####.##....#..###.##.#.#..#.
......##....#.#.#...#...#..#.....
...#.#..####.##.#.........###..##
.......#....#.##.......#.#.###...
...#..#.#.........#...###......#.
.#.##.#.#.#.#........#.#.##..#...
.......#.##.#...........#..#.#...
.####....##..#..##.#.##.##..##...
.#.#..###.#..#...#....#.###.#..#.
............#...#...#.......#.#..
.........###.#.....#..##..#.##..."""

asteroid_list = {}
y = 0
for line in asteroid_map.splitlines():
    x = 0
    for point in line:
        if point == "#":
            asteroid_list[(x, y)] = set()
        x += 1
    y += 1

visible_map = {}

for start_coord in asteroid_list:
    for end_coord in asteroid_list:
        if start_coord != end_coord:
            x1, y1 = start_coord
            x2, y2 = end_coord
            dx = x2 - x1
            dy = y2 - y1
            asteroid_list[start_coord].add((dx, dy))

for key, value in asteroid_list.items():
    normalized = normalize_vectors(value)
    num = len(normalized)
    visible_map[key] = num

max_key = keywithmaxval(visible_map)
max_visible = visible_map[max_key]
# part1
print("{} visible from {}".format(max_visible, max_key))

# part2
shoot_from = max_key
shoot_at_candidates = asteroid_list[shoot_from]
shoot_at_visible_normalized = list(normalize_vectors(shoot_at_candidates, True))
shoot_at_visible_real = []
for normalized_vector in shoot_at_visible_normalized:
    shoot_at_visible_real.append(visible_closest[normalized_vector])
shoot_at_visible_real.sort(key=lambda x: calc_angle(x))

shootx, shooty = shoot_from
dx200, dy200 = shoot_at_visible_real[199]
x200 = shootx + dx200
y200 = shooty+ dy200
print("{} {}".format(x200, y200))