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
#  input = f.read()

seeds = []
maps = {}

def get_destination(source, map_name):
    destination = source
    for destination_start, source_start, num in maps[map_name]:
        if source_start <= source and source <= source_start + num - 1:
            destination = source + destination_start - source_start
            return destination
    
    return destination

if __name__ == "__main__":
    categories = input.split("\n\n")
    seeds = [int(x) for x in categories[0].split(": ")[-1].split()]
    for name in categories[1::]:
        header, data = name.split(":\n")
        map_name, _ = header.split()
        maps[map_name] = []
        for line in data.split("\n"):
            maps[map_name].append([int(x) for x in line.split()])

    locations = []
    for seed in seeds:
        #print(f"Seed: {seed}")
        destination = seed
        for category_name, mapping in maps.items():
            destination = get_destination(destination, category_name) 
        
        locations.append(destination)
        #print(f"{category_name}: {destination}")

    print(f"Lowest location: {min(locations)}")