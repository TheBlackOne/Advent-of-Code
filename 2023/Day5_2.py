from tqdm import tqdm
from multiprocessing.pool import ThreadPool
from concurrent.futures import ProcessPoolExecutor

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# with open('input.txt') as f:
#    input = f.read()

seeds = []
maps = {}


def get_destination(source, mapping):
    destination = source
    for destination_start, source_start, num in mapping:
        if source_start <= source and source <= source_start + num - 1:
            destination = source + destination_start - source_start
            return destination

    return destination


def task(args):
    seed_start, seed_range, _maps = args
    min_location = 9999999999999999999999

    print(f"Seed start: {seed_start}, seed range: {seed_range}")

    for seed in range(seed_start, seed_start + seed_range):
        # print(f"Seed: {seed}")
        destination = seed
        for category_name, mapping in _maps.items():
            destination = get_destination(destination, mapping)
            # print(f"{category_name}: {destination}")

        min_location = min(min_location, destination)

    return min_location


if __name__ == "__main__":
    categories = input.split("\n\n")
    seeds = [int(x) for x in categories[0].split(": ")[-1].split()]
    for name in categories[1::]:
        header, data = name.split(":\n")
        map_name, _ = header.split()
        maps[map_name] = []
        for line in data.split("\n"):
            maps[map_name].append([int(x) for x in line.split()])

    min_location = 9999999999999999999999
    with ProcessPoolExecutor(max_workers=10) as executor:
        # with ThreadPool(processes=2) as pool:
        seed_data = [
            (seed_start, seed_range, maps)
            for seed_start, seed_range in zip(*[iter(seeds)] * 2)
        ]
        # for seed_start, seed_range in zip(*[iter(seeds)]*2):
        for result in executor.map(task, seed_data):
            print(f"Result: {result}")
            min_location = min(result, min_location)

    print(f"Lowest location: {min_location}")
