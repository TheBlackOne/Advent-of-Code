input = """Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""

# with open("input.txt") as f:
#    input = f.read()


def get_operand_value(operand):
    global a, b, c

    result = None

    if operand in range(4):
        result = operand
    elif operand == 4:
        result = a
    elif operand == 5:
        result = b
    elif operand == 6:
        result = c
    else:
        print(f"Invalid operand {operand}!")

    return result


def adv(operand, pointer):
    global a, b, c

    operand = get_operand_value(operand)

    numerator = a
    denominator = pow(2, operand)
    a = int(numerator / denominator)

    return pointer + 2


def bxl(operand, pointer):
    global a, b, c

    # operand = get_operand_value(operand)

    b = b ^ operand

    return pointer + 2


def bst(operand, pointer):
    global a, b, c

    operand = get_operand_value(operand)

    b = operand % 8

    return pointer + 2


def jnz(operand, pointer):
    global a

    operand = get_operand_value(operand)

    if a == 0:
        pointer += 2
    else:
        pointer = operand

    return pointer


def bxc(_, pointer):
    global b, c

    b = b ^ c

    return pointer + 2


def out(operand, pointer):
    global output_buffer

    operand = get_operand_value(operand)

    output_buffer.append(operand % 8)

    return pointer + 2


def bdv(operand, pointer):
    global a, b, c

    operand = get_operand_value(operand)

    numerator = a
    denominator = pow(2, operand)
    b = int(numerator / denominator)

    return pointer + 2


def cdv(operand, pointer):
    global a, b, c

    operand = get_operand_value(operand)

    numerator = a
    denominator = pow(2, operand)
    c = int(numerator / denominator)

    return pointer + 2


if __name__ == "__main__":
    pointer = 0

    registers, program = input.split("\n\n")
    a, b, c = map(int, [r.split(": ")[-1] for r in registers.splitlines()])
    program = list(map(int, program.split(": ")[-1].split(",")))

    instruction_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
    output_buffer = []

    while True:
        if pointer >= len(program):
            break

        instruction = program[pointer]
        operand = program[pointer + 1]

        pointer = instruction_map[instruction](operand, pointer)

    print(",".join(map(str, output_buffer)))
