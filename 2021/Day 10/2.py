opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

valid_pairs = [o+c for o, c in zip(opening, closing)]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def get_closing_character(opening_character):
    i = opening.index(opening_character)
    closing_character = closing[i]
    return closing_character

invalid_pairs = {}
for c in closing:
    for o in opening:
        pair = o+c
        if pair not in valid_pairs:
            score = points[c]
            invalid_pairs[pair] = score

with open('input.txt', 'r') as file:
    input = [_.strip() for _ in file.readlines()]

total_scores = []
for line in input:
    found = True
    corrupted = False
    while found:
        found = False
        for pair in valid_pairs:
            if pair in line:
                found = True
                line = line.replace(pair, '')
        for pair, score in invalid_pairs.items():
            if pair in line:
                found = True
                corrupted = True
                line = line.replace(pair, '')
    if not corrupted:
        score = 0
        closing_string = ""
        for opening_character in line:
            closing_string += get_closing_character(opening_character)
        closing_string = closing_string[::-1]

        for closing_character in closing_string:
            score *= 5
            score += closing.index(closing_character) + 1
        total_scores.append(score)

total_scores = sorted(total_scores, reverse=True)
result = total_scores[len(total_scores) // 2]

print(result)