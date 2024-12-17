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


def run_program(program, a_octal):
    global a
    global instruction_map
    global output_buffer

    a = int(a_octal, 8)
    pointer = 0
    output_buffer = []

    while True:
        if pointer >= len(program):
            break

        instruction = program[pointer]
        operand = program[pointer + 1]

        pointer = instruction_map[instruction](operand, pointer)

    return ",".join(map(str, output_buffer))


if __name__ == "__main__":
    instruction_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    output_buffer = []
    final_candidates = []

    registers, program = input.split("\n\n")
    a, b, c = map(int, [r.split(": ")[-1] for r in registers.splitlines()])
    program = list(map(int, program.split(": ")[-1].split(",")))
    program_string = ",".join(map(str, program))

    candidates = [""]
    for counter in range(len(program)):
        new_candidates = []
        for a_octal in candidates:
            for x in range(8):
                new_a_octal = a_octal + str(x)
                program_result = run_program(program, new_a_octal)
                if program_string == program_result:
                    final_candidates.append(new_a_octal)
                elif program_string.endswith(program_result):
                    new_candidates.append(new_a_octal)
        candidates = new_candidates
        # print(candidates)
    print(int(min(final_candidates), 8))
