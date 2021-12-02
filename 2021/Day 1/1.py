input = []
with open('input.txt', 'r') as file:
    input =  [line.strip() for line in file.readlines()]

increases = 0

for index, elem in enumerate(input):
    if index == 0: continue
    if int(elem) > int(input[index - 1]): increases += 1

print(increases)