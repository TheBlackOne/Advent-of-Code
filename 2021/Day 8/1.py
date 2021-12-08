interesting_numbers = [2, 3, 4, 7]
result = 0

with open('input.txt', 'r') as file:
    for line in file.readlines():
        _, second = line.split('|')

        displays = second.strip().split(' ')
        for display in displays:
            if len(display) in interesting_numbers: result += 1

print(result)