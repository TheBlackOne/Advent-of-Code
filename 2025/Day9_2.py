import itertools
import shapely
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
#    input = f.read()

if __name__ == "__main__":
    red_tiles = []
    green_tiles = []

    for line in input.splitlines():
        x, y = line.split(',')
        red_tiles.append((int(x), int(y)))
    
    polygon = shapely.LinearRing(red_tiles)
    shapely.prepare(polygon)

    areas = []
    for corner1, corner2 in itertools.combinations(red_tiles, 2):
        if any(c1 == c2 for c1, c2 in zip(corner1, corner2)):
            continue
        area = (abs(corner2[0] - corner1[0]) + 1) * (abs(corner2[1] - corner1[1]) + 1)
        areas.append((area, corner1, corner2))

    answer = None
    for area, corner1, corner2 in tqdm.tqdm(sorted(areas, key=lambda x: x[0])[::-1]):
        corner3 = (corner1[0], corner2[1])
        corner4 = (corner2[0], corner1[1])

        lines = []
        lines.append(shapely.LineString((corner1, corner3)))
        lines.append(shapely.LineString((corner1, corner4)))
        lines.append(shapely.LineString((corner2, corner3)))
        lines.append(shapely.LineString((corner3, corner4)))

        if not any(shapely.crosses(polygon, l) for l in lines):
            answer = area
            break

    print(answer)