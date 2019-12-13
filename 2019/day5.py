opcode_num_parameters = {
    1 : (3, 1),
    2 : (3, 1),
    3 : (1, 1),
    4 : (1, 0),
    5 : (2, 0),
    6 : (2, 0),
    7 : (3, 1),
    8 : (3, 1)
}

def add(parameter1, parameter2, parameter3, _instruction_pointer, _program):
    print("add: parameter1: {}, parameter2: {}, parameter3: {}".format(parameter1, parameter2, parameter3))
    _program[parameter3] = parameter1 + parameter2
    return _instruction_pointer + 4

def mul(parameter1, parameter2, parameter3, _instruction_pointer, _program):
    print("mul: parameter1: {}, parameter2: {}, parameter3: {}".format(parameter1, parameter2, parameter3))
    _program[parameter3] = parameter1 * parameter2
    return _instruction_pointer + 4

def op_input(parameter1, _instruction_pointer, _program):
    print("op_input: parameter1: {}".format(parameter1))
    input_number = input("Input: ")
    _program[parameter1] = int(input_number)
    return _instruction_pointer + 2

def output(parameter1, _instruction_pointer):
    print("output: parameter1: {}".format(parameter1))
    print("Output: {}".format(parameter1))
    return _instruction_pointer + 2

def jump_true(parameter1, parameter2, _instruction_pointer):
    print("jump_true: parameter1: {}, parameter2: {}".format(parameter1, parameter2))
    if parameter1 != 0: return parameter2
    else: return _instruction_pointer + 3

def jump_false(parameter1, parameter2, _instruction_pointer):
    print("jump_true: parameter1: {}, parameter2: {}".format(parameter1, parameter2))
    if parameter1 == 0: return parameter2
    else: return _instruction_pointer + 3

def less(parameter1, parameter2, parameter3, _instruction_pointer, _program):
    print("less: parameter1: {}, parameter2: {}, parameter3: {}".format(parameter1, parameter2, parameter3))
    if parameter1 < parameter2: _program[parameter3] = 1
    else: _program[parameter3] = 0
    return _instruction_pointer + 4

def equals(parameter1, parameter2, parameter3, _instruction_pointer, _program):
    print("equals: parameter1: {}, parameter2: {}, parameter3: {}".format(parameter1, parameter2, parameter3))
    if parameter1 == parameter2: _program[parameter3] = 1
    else: _program[parameter3] = 0
    return _instruction_pointer + 4

def fill_parameters(_opcode, _modes, _instruction_pointer, _program):
    if _opcode not in opcode_num_parameters.keys():
        print("Unknown opcode!")

    opcode_details = opcode_num_parameters[_opcode]
    num_parameters = opcode_details[0]
    num_write_adresses = opcode_details[1]

    parameters = _program[_instruction_pointer + 1:_instruction_pointer + 1 + num_parameters]
    write_address = _program[_instruction_pointer + num_parameters - 1]
    
    for i in range(num_parameters - num_write_adresses):
        mode = 0
        if len(_modes) > i:
            mode = _modes[i]
        if mode == 0:
            parameter_address = parameters[i]
            parameters[i] = _program[parameter_address]

    if len(parameters) < num_parameters:
        print("Less parameters than opcode needs!")

    return (parameters, write_address)


def parse_opcode_modes(_instruction_pointer, _program):
    opcode = _program[_instruction_pointer]
    modes = []
    if int(opcode) > 10:
        opcode_str = str(_program[_instruction_pointer])
        opcode = int(opcode_str[-2] + opcode_str[-1])
        modes_str = reversed(opcode_str[0:-2])
        for mode in modes_str:
            modes.append(mode)

    return (opcode, modes)

def run_program(_program):
    instruction_pointer = 0
    while True:
        next_instruction_pointer = 0

        print("instruction_pointer: {}".format(instruction_pointer))
        
        opcode, modes = parse_opcode_modes(instruction_pointer, _program)
        parameters, write_address = fill_parameters(opcode, modes, instruction_pointer, _program)

        if opcode == 99:
            print("Encountered opcode 99, breaking...")
            break
        elif opcode == 1:
            next_instruction_pointer = add(parameters[0], parameters[1], write_address, instruction_pointer, _program)
        elif opcode == 2:
            next_instruction_pointer = mul(parameters[0], parameters[1], write_address, instruction_pointer, _program)
        elif opcode == 3:
            next_instruction_pointer = op_input(parameters[0], instruction_pointer, _program)
        elif opcode == 4:
            next_instruction_pointer = output(parameters[0], instruction_pointer, _program)
        elif opcode == 5:
            next_instruction_pointer = jump_true(parameters[0], parameters[1], instruction_pointer)
        elif opcode == 6:
            next_instruction_pointer = jump_false(parameters[0], parameters[1], instruction_pointer)
        elif opcode == 7:
            next_instruction_pointer = less(parameters[0], parameters[1], write_address, instruction_pointer, _program)
        elif opcode == 8:
            next_instruction_pointer = equals(parameters[0], parameters[1], write_address, instruction_pointer, _program)
        else:
            print("Unknown opcode: {}".format(opcode))

        instruction_pointer = next_instruction_pointer
        
    return _program[0]

#initial_program = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,5,23,1,6,23,27,1,27,5,31,2,31,10,35,2,35,6,39,1,39,5,43,2,43,9,47,1,47,6,51,1,13,51,55,2,9,55,59,1,59,13,63,1,6,63,67,2,67,10,71,1,9,71,75,2,75,6,79,1,79,5,83,1,83,5,87,2,9,87,91,2,9,91,95,1,95,10,99,1,9,99,103,2,103,6,107,2,9,107,111,1,111,5,115,2,6,115,119,1,5,119,123,1,123,2,127,1,127,9,0,99,2,0,14,0]
#
# initial_program = [3,0,4,0,99]
#initial_program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
initial_program = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,16,13,225,1001,88,68,224,101,-114,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,8,76,224,101,-84,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1101,63,58,225,1102,14,56,224,101,-784,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,29,46,225,102,60,187,224,101,-2340,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1102,60,53,225,1101,50,52,225,2,14,218,224,101,-975,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1002,213,79,224,101,-2291,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,114,117,224,101,-103,224,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1101,39,47,225,101,71,61,224,101,-134,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,29,13,225,1102,88,75,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,102,2,223,223,1006,224,329,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,344,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,359,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,374,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,389,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,404,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,434,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,509,1001,223,1,223,1008,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,554,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,569,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,599,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,107,226,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,659,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

def main():
    result = run_program(initial_program)
    #print(result)

if __name__== "__main__":
  main()