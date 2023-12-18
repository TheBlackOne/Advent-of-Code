from os import path
import sys
from PIL import Image, ImageDraw

sys.setrecursionlimit(3000)

input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#  input = f.read()

directions = {"U": (0, -1), "L": (-1, 0), "D": (0, 1), "R": (1, 0)}

dig_plan = []
map = []
max_x, max_y = 0, 0


def save_to_file():
    with open("map.txt", "w") as f:
        for line in map:
            f.write("".join([c for c in line]))
            f.write("\n")


def flood_fill(x, y, fill_char):
    global map
    global max_x
    global max_y

    for x_offset, y_offset in directions.values():
        check_x = x + x_offset
        check_y = y + y_offset
        if check_x >= 0 and check_x < max_x and check_y >= 0 and check_y < max_y:
            if map[check_y][check_x] == ".":
                map[check_y][check_x] = fill_char
                flood_fill(check_x, check_y, fill_char)


if __name__ == "__main__":
    for line in input.splitlines():
        direction, distance, color = line.split()
        dig_plan.append((direction, int(distance), color))

    map_size = 1000
    for y in range(map_size):
        line = ["." for _ in range(map_size)]
        map.append(line)

    max_x = map_size - 1
    max_y = map_size - 1

    x, y = 500, 500
    fill_character = "#"
    map[y][x] = fill_character
    for direction, distance, _ in dig_plan:
        step_x, step_y = directions[direction]
        for _ in range(distance):
            x += step_x
            y += step_y
            map[y][x] = fill_character

    im = Image.new(mode="RGB", size=(map_size, map_size), color=(0, 0, 0))
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == fill_character:
                im.putpixel(xy=(x, y), value=(255, 255, 255))

    x, y = 340, 340
    ImageDraw.floodfill(im, (x, y), value=(255, 255, 255))
    # im.save("map.png")

    dug_out = 0
    for pixel in im.getdata():
        if pixel == (255, 255, 255):
            dug_out += 1

    print(dug_out)
