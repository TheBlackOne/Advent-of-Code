from os import path
import numpy as np

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

# input = """R 7 #
# D 4 #
# L 3 #
# U 1 #
# L 2 #
# D 1 #
# L 2 #
# U 4 #"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#  input = f.read()

directions = {"3": (0, -1), "2": (-1, 0), "1": (0, 1), "0": (1, 0)}

dig_plan = []


def save_to_file():
    with open("map.txt", "w") as f:
        for line in map:
            f.write("".join([c for c in line]))
            f.write("\n")


def shoelace(x_y):
    x_y = np.array(x_y, dtype=np.int64)
    x_y = x_y.reshape(-1, 2)

    x = x_y[:, 0]
    y = x_y[:, 1]

    S1 = np.sum(x * np.roll(y, -1))
    S2 = np.sum(y * np.roll(x, -1))

    area = 0.5 * np.absolute(S1 - S2)

    return area


if __name__ == "__main__":
    for line in input.splitlines():
        _, _, color = line.split()
        distance = color[2:7]
        distance = int(distance, 16)
        direction = color[-2]
        dig_plan.append((direction, int(distance), color))
    polygon_corners = []
    x, y = 0, 0

    total_distance = 0
    for direction, distance, _ in dig_plan:
        step_x, step_y = directions[direction]
        step_x = step_x * distance
        step_y = step_y * distance
        x = x + step_x
        y = y + step_y
        polygon_corners.append((x, y))
        total_distance += distance

    dug_out = shoelace(polygon_corners)

    dug_out = dug_out + (total_distance + 2) // 2

    print(dug_out)
