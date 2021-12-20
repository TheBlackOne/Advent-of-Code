from itertools import product, permutations, combinations
import numpy as np
from tqdm import tqdm
from datetime import datetime

coordinate_systems = set()
for rot in product((-1, 1), repeat=3):
    for perm in permutations((1, 2, 3), 3):
        coord_system = tuple(map(lambda i, j: i * j, rot, perm))
        coordinate_systems.add(coord_system)

def subtract_tuple(tuple1, tuple2):
    return tuple(map(lambda i, j: i - j, tuple1, tuple2))

def negate_tuple(tuple1):
    return tuple([i * -1 for i in tuple1])

def to_coordinate_system(coord, coordinate_system):
    result = []
    for part in coordinate_system:
        value = coord[abs(part) - 1]
        if part < 0: value *= -1
        result.append(value)
    return tuple(result)

scanner_data = {}
with open('input.txt', 'r') as file:
    for block in file.read().split('\n\n'):
        scanner_parts = block.split('\n')
        scanner_number = int(scanner_parts[0].split()[2])
        scanner_data[scanner_number] = []
        for coordinates in scanner_parts[1:]:
            coordinates = tuple([int(_) for _ in coordinates.split(',')])
            scanner_data[scanner_number].append(coordinates)

def get_distance_count(data1, data2, axis):
    dist = []
    for coord1, coord2 in product(data1, data2):
        dist.append(coord1[axis] - coord2[axis])
    dists, count = np.unique(np.asarray(dist), return_counts=True)
    max_count = max(count)
    max_count_index = np.where(count==max_count)[0]
    return (dists[max_count_index], max_count)

index_combinations = list(combinations(scanner_data.keys(), 2))
combinations_found = []
found = {}
whole_map = set()
normalized = [0]
scanners = set()

start_time = datetime.now()
while True:
    for scanner1_name in normalized:
        for scanner2_name in scanner_data.keys():
            if (scanner1_name, scanner2_name) in combinations_found or (scanner2_name, scanner1_name) in combinations_found: continue
            if scanner1_name == scanner2_name: continue

            #print("{} {}".format(scanner1_name, scanner2_name))

            scanner1_data = scanner_data[scanner1_name]
            scanner2_data = scanner_data[scanner2_name]

            for coordinate_system in coordinate_systems:
                rotated_data = [to_coordinate_system(coord, coordinate_system) for coord in scanner2_data]

                diff = None
                diff_x, count_x = get_distance_count(scanner1_data, rotated_data, 0)
                if count_x >= 12:
                    diff_y, count_y = get_distance_count(scanner1_data, rotated_data, 1)
                    if count_y >= 12:
                        diff_z, count_z = get_distance_count(scanner1_data, rotated_data, 2)
                        if count_z >= 12:
                            if scanner2_name != 0:
                                diff = (diff_x[0], diff_y[0], diff_z[0])

                                corrected_data = [subtract_tuple(coord, negate_tuple(diff)) for coord in rotated_data]
                                scanner_data[scanner2_name] = corrected_data
                                combinations_found.append((scanner1_name, scanner2_name))
                                normalized.append(scanner2_name)

                                scanner_coord = subtract_tuple((0, 0, 0), negate_tuple(diff))
                                scanners.add(scanner_coord)
                                break
    break
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

distances = []
for scanner1, scanner2 in combinations(scanners, 2):
    diff = subtract_tuple(scanner1, scanner2)
    distances.append(sum([abs(part) for part in diff]))
print(max(distances))