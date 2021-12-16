from collections import Counter

polymer = ""
rules = []

with open('input.txt', 'r') as file:
    polymer, second = file.read().split('\n\n')

    for line in second.split('\n'):
        rules.append(line.split(' -> '))

for step in range(10):
    pairs = []
    for i in range(len(polymer) - 1):
        pairs.append(polymer[i] + polymer[i + 1])

    for pattern, insert in rules:
        while pattern in pairs:
            i = pairs.index(pattern)
            if i >= 0:
                new_pattern = pattern[0] + insert + pattern[1]
                pairs[i] = new_pattern
    
    polymer = polymer[0] + ''.join([pair[1:] for pair in pairs])

counter = Counter(polymer)
most = max(counter, key = counter.get)
least = min(counter, key = counter.get)

print(counter[most] - counter[least])