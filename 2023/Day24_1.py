from os import path
from itertools import combinations
import operator

input = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#    input = f.read()

hail_data = []


def get_comparator(velocity):
    op = operator.eq
    if velocity > 0:
        op = operator.gt
    elif velocity < 0:
        op = operator.lt

    return op


def intersects_in_future(h1, h2, intersection):
    x1, y1, vx1, vy1 = h1
    x2, y2, vx2, vy2 = h2

    comp_vx1 = get_comparator(vx1)
    comp_vy1 = get_comparator(vy1)
    comp_vx2 = get_comparator(vx2)
    comp_vy2 = get_comparator(vy2)

    ix, iy = intersection
    comparator_results = []
    comparator_results.append(comp_vx1(ix, x1))
    comparator_results.append(comp_vy1(iy, y1))
    comparator_results.append(comp_vx2(ix, x2))
    comparator_results.append(comp_vy2(iy, y2))

    result = all(comparator_results)
    return result


def compute_intersection(h1, h2):
    result = None

    x1, y1, vx1, vy1 = h1
    x2, y2, vx2, vy2 = h2

    s1 = vy1 / vx1
    s2 = vy2 / vx2

    if s1 != s2:
        y1_zero = y1 - s1 * x1
        y2_zero = y2 - s2 * x2

        x_left = s1
        x_right = s2
        x_left -= x_right

        y_zero_left = y1_zero
        y_zero_right = y2_zero
        y_zero_right -= y_zero_left

        x_intersect = y_zero_right / x_left
        y_intersect = s1 * x_intersect + y1_zero

        result = (x_intersect, y_intersect)

    return result

    print()


if __name__ == "__main__":
    for line in input.splitlines():
        coords, velocities = line.split(" @ ")
        x, y, _ = [int(c) for c in coords.split(", ")]
        vx, vy, _ = [int(v) for v in velocities.split(", ")]
        hail_data.append((x, y, vx, vy))

    intersection_counter = 0
    window = (7, 27)
    # window = (200000000000000, 400000000000000)

    for h1, h2 in combinations(hail_data, 2):
        intersection = compute_intersection(h1, h2)
        if intersection != None:
            ix, iy = intersection
            min, max = window
            if min <= ix <= max and min <= iy <= max:
                if h1[:2] == (18, 19) and h2[:2] == (20, 19):
                    print()
                valid_intersection = intersects_in_future(h1, h2, intersection)
                if valid_intersection:
                    intersection_counter += 1

    print(intersection_counter)
