import itertools
import shapely
from shapely import Polygon
import tqdm

input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

#with open("input.txt") as f:
#   input = f.read()

if __name__ == "__main__":
    red_tiles = []
    green_tiles = []

    for line in input.splitlines():
        x, y = line.split(',')
        red_tiles.append((int(x), int(y)))
    
    polygon = Polygon(red_tiles)
    shapely.prepare(polygon)

    areas = []

    for corner1, corner2 in tqdm.tqdm(list(itertools.combinations(red_tiles, 2))):
        if any(c1 == c2 for c1, c2 in zip(corner1, corner2)):
            continue

        corners = [corner1, corner2]
        corners.append((corner1[0], corner2[1]))
        corners.append((corner2[0], corner1[1]))
        corners = set(corners)

        if len(corners) == 4:
            test_polygon = Polygon(corners)
            test_polygon = shapely.make_valid(test_polygon)
            
            if shapely.covers(polygon, test_polygon):
                area = (abs(corner2[0] - corner1[0]) + 1) * (abs(corner2[1] - corner1[1]) + 1)
                areas.append(area)

    print(max(areas))