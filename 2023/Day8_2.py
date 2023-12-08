from functools import reduce
from math import lcm

input = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

#with open('input.txt') as f:
#    input = f.read()

instructions = []
node_dict = {}

instruction_index = 0


def get_next_instruction() -> int:
    global instruction_index
    result = instructions[instruction_index]
    instruction_index += 1
    if instruction_index >= len(instructions):
        instruction_index = 0
    return result


if __name__ == "__main__":
    instructions_string, nodes_string = input.split('\n\n')
    instructions_string = instructions_string.replace(
        'L', '0').replace('R', '1')
    instructions = [int(i) for i in instructions_string]

    for line in nodes_string.splitlines():
        key, values = line.split(' = ')
        values = values.replace('(', '').replace(')', '')
        nodes = values.split(', ')
        node_dict[key] = nodes

    nodes = list(filter(lambda x: x[-1] == 'A', node_dict.keys()))
    all_steps = []

    for node in nodes:
        instruction_index = 0
        steps = 0
        while node[-1] != 'Z':
            next_instruction = get_next_instruction()
            node = node_dict[node][next_instruction]
            steps += 1
        all_steps.append(steps)

    least = reduce(lcm, all_steps)

    print(f"Steps needed: {least}")
