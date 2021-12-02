input = []
with open('input.txt', 'r') as file:
    input =  [line.strip() for line in file.readlines()]

sliding_measurements = []

for index, elem in enumerate(input):
    if index + 2 < len(input):
        summed = int(elem) + int(input[index + 1]) + int(input[index + 2])
        sliding_measurements.append(summed)

increases = 0

for index, elem in enumerate(sliding_measurements):
    if index == 0: continue
    if int(elem) > int(sliding_measurements[index - 1]): increases += 1

print(increases)