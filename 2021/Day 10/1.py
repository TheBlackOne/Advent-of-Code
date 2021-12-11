opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

valid_pairs = [o+c for o, c in zip(opening, closing)]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

invalid_pairs = {}
for c in closing:
    for o in opening:
        pair = o+c
        if pair not in valid_pairs:
            score = points[c]
            invalid_pairs[pair] = score

with open('input.txt', 'r') as file:
    input = [_.strip() for _ in file.readlines()]

total_score = 0
for line in input:
    found = True
    while found:
        found = False
        for pair in valid_pairs:
            if pair in line:
                found = True
                line = line.replace(pair, '')
        for pair, score in invalid_pairs.items():
            if pair in line:
                found = True
                line = line.replace(pair, '')
                total_score += score

print(total_score)