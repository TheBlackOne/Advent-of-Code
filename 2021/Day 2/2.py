input = []
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file.readlines()]

position = 0
depth = 0
aim = 0

for command_number in input:
    command, number = command_number.split(' ')
    number = int(number)

    if command == 'up': aim -= number
    elif command == 'down': aim += number
    elif command == 'forward':
        position += number
        depth += aim * number

print("{}".format(position * depth))