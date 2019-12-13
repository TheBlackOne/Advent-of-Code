import itertools

inputs = []
input_cursor = 0

output = ""

def op_input():
    global result
    global input_cursor
    result = inputs[input_cursor]
    input_cursor += 1

    return int(result)

def op_output(parameter):
    global output
    #print("Output: {}".format(parameter))
    output = parameter
    return None

def jump_true(parameter1, parameter2):
    if parameter1 != 0: return parameter2
    else: return None

def jump_false(parameter1, parameter2):
    if parameter1 == 0: return parameter2
    else: return None 

def add(parameter1, parameter2):
    return parameter1 + parameter2

def mul(parameter1, parameter2):
    return parameter1 * parameter2

def less(parameter1, parameter2):
    if parameter1 < parameter2: return 1
    else: return 0

def equals(parameter1, parameter2):
    if parameter1 == parameter2: return 1
    else: return 0

def opcode1(_instruction_pointer, _program):
    opcode = _program[_instruction_pointer]
    if int(opcode) > 10:
        str_opcode = str(opcode)
        opcode = int(str_opcode[-2] + str_opcode[-1])
    modes = int(_program[_instruction_pointer] // 100)
    mode1 = modes % 10

    parameter1 = _program[_instruction_pointer + 1]
    if mode1 == 0:
        address_parameter1 = _program[_instruction_pointer + 1]
        parameter1 = _program[address_parameter1]
    result_address =  _program[_instruction_pointer + 1]

    result = None
    if opcode == 3: result = op_input()
    elif opcode == 4: result = op_output(parameter1)
    elif opcode == 99:
        print("Encountered opcode 99, returning...")
        return 1
    else: raise("invalid opcode")

    if result != None:
        _program[result_address] = result

    return _instruction_pointer + 2

def jump(_instruction_pointer, _program):
    opcode = _program[_instruction_pointer]
    org_opcode = opcode
    if int(opcode) > 10:
        str_opcode = str(opcode)
        opcode = int(str_opcode[-2] + str_opcode[-1])
    modes = int(_program[_instruction_pointer] // 100)
    mode1 = modes % 10
    mode2 = (modes // 10) % 10

    #print("Op: {} opcode: {} mode1: {} mode2: {}".format(org_opcode, opcode, mode1, mode2))    

    parameter1 = _program[_instruction_pointer + 1]
    if mode1 == 0:
        address_parameter1 = _program[_instruction_pointer + 1]
        parameter1 = _program[address_parameter1]

    parameter2 = _program[_instruction_pointer + 2]
    if mode2 == 0:
        address_parameter2 = _program[_instruction_pointer + 2]
        parameter2 = _program[address_parameter2]
    
    step = _instruction_pointer + 3
    if opcode == 5:
        result = jump_true(parameter1, parameter2)
        if result != None:
            step = result
    elif opcode == 6:
        result = jump_false(parameter1, parameter2)
        if result != None:
            step = result
    
    return step

def opcode3(_instruction_pointer, _program):
    opcode = _program[_instruction_pointer]
    org_opcode = opcode
    if int(opcode) > 10:
        str_opcode = str(opcode)
        opcode = int(str_opcode[-2] + str_opcode[-1])
    modes = int(_program[_instruction_pointer] // 100)
    mode1 = modes % 10
    mode2 = (modes // 10) % 10
    mode3 = modes // 100

    #print("Op: {} opcode: {} mode1: {} mode2: {}".format(org_opcode, opcode, mode1, mode2))

    parameter1 = _program[_instruction_pointer + 1]
    if mode1 == 0:
        address_parameter1 = _program[_instruction_pointer + 1]
        parameter1 = _program[address_parameter1]

    parameter2 = _program[_instruction_pointer + 2]
    if mode2 == 0:
        address_parameter2 = _program[_instruction_pointer + 2]
        parameter2 = _program[address_parameter2]
    
    if mode3 == 1:
        raise("Unknown mode for result parameter")

    result_address =  _program[_instruction_pointer + 3]

    result = 0
    step = 4
    if opcode == 1:
        result = add(parameter1, parameter2)
        _program[result_address] = result
    elif opcode == 2:
        result = mul(parameter1, parameter2)
        _program[result_address] = result
    elif opcode == 7:
        result = less(parameter1, parameter2)
        if result != None:
            _program[result_address] = result
    elif opcode == 8:
        result = equals(parameter1, parameter2)
        if result != None:
            _program[result_address] = result
    elif opcode == 99: 
        print("Encountered opcode 99, returning...")
        return 1
    else: raise("invalid opcode")

    return _instruction_pointer + step

def run_program(_program):
    result = 0
    address = 0
    while True:
        step = 1
        opcode = _program[address]
        if int(opcode) > 10:
            str_opcode = str(opcode)
            opcode = int(str_opcode[-2] + str_opcode[-1])
        if opcode == 99:
            #print("Encountered opcode 99, breaking...")
            result = None
            break
        elif opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            step = opcode3(address, _program)
        elif opcode == 5 or opcode == 6:
            step = jump(address, _program)
        elif opcode == 3 or opcode == 4:
            step = opcode1(address, _program)
        else:
            print("Unknown opcode: {}".format(opcode))
        address = step

    return result

#initial_program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
#initial_program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
initial_program = [3,8,1001,8,10,8,105,1,0,0,21,38,47,72,97,122,203,284,365,446,99999,3,9,1001,9,3,9,1002,9,5,9,1001,9,4,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,102,5,9,9,101,3,9,9,1002,9,5,9,101,4,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,101,2,9,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,2,9,9,1001,9,4,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99]

def main():
    phase_settings = list(range(5))
    phase_permutations = list(itertools.permutations(phase_settings))

    global inputs
    global input_cursor
    global output

    results = []
 
    for perm in reversed(phase_permutations):
        output = 0
        for setting in perm:
            input_cursor = 0
            inputs = []
            inputs.append(setting)
            inputs.append(output)

            result = run_program(initial_program.copy())
            results.append(output)
            #print(output)
    print(max(results))

if __name__== "__main__":
  main()