from os import path
from itertools import islice
import operator
from tqdm import tqdm
from sympy import Ray2D, Point2D
from concurrent.futures import ProcessPoolExecutor

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


def task(args):
    result = []
    h1, h2, test_range_x_batch, test_range_y = args

    for test_vx in tqdm(test_range_x_batch, ascii=True):
        for test_vy in test_range_y:
            if test_vx == -3 and test_vy == 1:
                pass
            if test_vx == 1 and test_vy == 2:
                pass
            x1, y1, vx1, vy1 = h1
            x2, y2, vx2, vy2 = h2

            p1_1 = Point2D(x1, y1)
            p1_2 = Point2D(x1 + vx1 - test_vx, y1 + vy1 - test_vy)
            if p1_1 == p1_2:
                continue
            r1 = Ray2D(p1_1, p1_2)

            p2_1 = Point2D(x2, y2)
            p2_2 = Point2D(x2 + vx2 - test_vx, y2 + vy2 - test_vy)
            if p2_1 == p2_2:
                continue
            r2 = Ray2D(p2_1, p2_2)

            intersections = r1.intersection(r2)
            for intersection in intersections:
                if isinstance(intersection, Point2D):
                    # if True:
                    ix, iy = intersection.coordinates
                    ix = ix.p / ix.q
                    iy = iy.p / iy.q
                    if ix.is_integer() and iy.is_integer():
                        result.append((intersection, test_vx, test_vy))
    return result


def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def get_intersection_candidates(h1, h2):
    candidates = []

    num_workers = 7
    test_range_x = range(-500, 500)
    test_range_y = test_range_x
    test_range_x_batch = chunk(test_range_x, len(test_range_x) // num_workers)
    data = [(h1, h2, b, test_range_y) for b in test_range_x_batch]

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for result in executor.map(task, data):
            candidates += result

    return candidates


def condense_intersection_points(h, candidates):
    result = []
    x, y, vx, vy = h
    p1 = Point2D(x, y)

    for candidate in candidates:
        test_point, test_vx, test_vy = candidate
        p2 = Point2D(x + vx - test_vx, y + vy - test_vy)
        if p1 != p2:
            ray = Ray2D(p1, p2)

            if ray.contains(test_point):
                result.append((test_point, test_vx, test_vy))

    return result


def construct_2d(point, index):
    coords = point[index : index + 2]
    velocities = point[index + 3 : index + 5]
    result = (*coords, *velocities)
    return result


def condense_intersections(point_index):
    intersection_candidates = []
    h1 = hail_data[0]
    h2 = hail_data[1]

    h1 = construct_2d(h1, point_index)
    h2 = construct_2d(h2, point_index)
    intersection_candidates = get_intersection_candidates(h1, h2)

    for h in hail_data[2:]:
        h = construct_2d(h, point_index)
        intersection_candidates = condense_intersection_points(
            h, intersection_candidates
        )

        if len(intersection_candidates) < 2:
            break

    return intersection_candidates


if __name__ == "__main__":
    for line in input.splitlines():
        coords, velocities = line.split(" @ ")
        x, y, z = [int(c) for c in coords.split(", ")]
        vx, vy, vz = [int(v) for v in velocities.split(", ")]
        hail_data.append((x, y, z, vx, vy, vz))

    intersections_xy = condense_intersections(0)
    intersections_yz = condense_intersections(1)

    p1 = intersections_xy[0][0]
    p2 = intersections_yz[0][0]
    coords1 = p1.coordinates
    coords2 = p2.coordinates

    result = sum(coords1) + coords2[1]

    print(result)
