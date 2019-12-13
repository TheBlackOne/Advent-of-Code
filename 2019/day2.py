def add(parameter1, parameter2):
    return parameter1 + parameter2

def mul(parameter1, parameter2):
    return parameter1 * parameter2

def opcode3(_instruction_pointer, _program):
    opcode = _program[_instruction_pointer]

    address_parameter1 = _program[_instruction_pointer + 1]
    address_b = _program[_instruction_pointer + 2]
    result_address =  _program[_instruction_pointer + 3]

    parameter1 = _program[address_parameter1]
    parameter2 = _program[address_b]    

    result = 0
    if opcode == 1: result = add(parameter1, parameter2)
    elif opcode == 2: result = mul(parameter1, parameter2)
    elif opcode == 99: 
        print("Encountered opcode 99, returning...")
        return 1
    else: raise("invalid opcode")

    _program[result_address] = result

    return 4

def run_program(_program):
    address = 0
    while True:
        step = 1
        opcode = _program[address]
        if opcode == 99:
            #print("Encountered opcode 99, breaking...")
            break
        elif opcode == 1 or opcode == 2:
            step = opcode3(address, _program)
        address += step

    return _program[0]

initial_program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]

def main():
    for noun in range(100):
        for verb in range(100):
            test_program = initial_program.copy()
            test_program[1] = noun
            test_program[2] = verb

            #print("Running program with: {} {}".format(noun, verb))
            result = run_program(test_program)

            print("Result: {}".format(result))

            if result == 19690720:
                print("Found solution! {} {}".format(noun, verb))
                print(noun * 100 + verb)
                return

if __name__== "__main__":
  main()