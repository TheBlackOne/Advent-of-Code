from os import path
from PIL import Image, ImageDraw

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

if __name__ == "__main__":
    for line in input.splitlines():
        direction, distance, color = line.split()
        dig_plan.append((direction, int(distance), color))

    map_size = 1000
    x, y = 500, 500

    im = Image.new(mode="RGB", size=(map_size, map_size), color=(0, 0, 0))
    im.putpixel(xy=(x, y), value=(255, 255, 255))
    for direction, distance, _ in dig_plan:
        step_x, step_y = directions[direction]
        for _ in range(distance):
            x += step_x
            y += step_y
            im.putpixel(xy=(x, y), value=(255, 255, 255))

    # Start point for floodfill has to be adjust by looking at the picture
    # and finding a coordinate that is inside
    x, y = 501, 501
    ImageDraw.floodfill(im, (x, y), value=(255, 255, 255))
    im.save("map.png")

    dug_out = 0
    for pixel in im.getdata():
        if pixel == (255, 255, 255):
            dug_out += 1

    print(dug_out)
