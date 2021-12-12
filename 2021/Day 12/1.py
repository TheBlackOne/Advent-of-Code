from collections import defaultdict

from datetime import datetime

start_time = datetime.now()

cave = defaultdict(list)

with open('input.txt', 'r') as file:
    for line in file.readlines():
        start, end = line.strip().split('-')
        cave[start].append(end)
        cave[end].append(start)

valid_paths = []

def find_next_cave(path):
    current_cave = path[-1]
    for next_cave in cave[current_cave]:
        if not (next_cave.islower() and next_cave in path):
            current_path = path.copy()
            current_path.append(next_cave)

            if next_cave == "end":                
                valid_paths.append(current_path)
            else:
                find_next_cave(current_path)

find_next_cave(["start"])

print(len(valid_paths))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))