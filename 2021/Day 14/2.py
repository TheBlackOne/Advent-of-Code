from collections import defaultdict

polymer = ""
rules = {}
element_count = defaultdict(lambda: 0)

with open('input.txt', 'r') as file:
    polymer, second = file.read().split('\n\n')

    for line in second.split('\n'):
        pattern, insert = line.split(' -> ')
        rules[pattern] = insert

pairs_count = {}
for i in range(len(polymer) - 1):
    pair = polymer[i] + polymer[i + 1]
    if pair in pairs_count.keys():
        pairs_count[pair] += 1
    else:
        pairs_count[pair] = 1

for element in polymer:
    element_count[element] += 1

for step in range(40):
    new_pairs_count = {}

    for pair, count in pairs_count.items():
        new_pairs = [pair]

        if pattern in rules.keys():
            insert = rules[pair]
            new_pairs = [pair[0] + insert, insert + pair[1]]
            element_count[insert] += count

        for new_pair in new_pairs:
            if new_pair in new_pairs_count.keys():
                new_pairs_count[new_pair] += count
            else:
                new_pairs_count[new_pair] = count
        
    pairs_count = new_pairs_count

sorted_counts = sorted(element_count.values())

most = sorted_counts[-1]
least = sorted_counts[0]
print(most - least)