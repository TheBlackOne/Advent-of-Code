input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

# with open('input.txt') as f:
#   input = f.read()

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

    steps = 0
    node = 'AAA'

    while node != 'ZZZ':
        next_instruction = get_next_instruction()
        node = node_dict[node][next_instruction]
        steps += 1

    print(f"Steps needed: {steps}")
