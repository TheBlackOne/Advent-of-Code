import itertools
import queue

amp_data = []
amp_index = 0

op_parameter_count = {
    1 : { "number_parameters" : 3, "number_output_parameters" : 1 },
    2 : { "number_parameters" : 3, "number_output_parameters" : 1 },
    3 : { "number_parameters" : 1, "number_output_parameters" : 1 },
    4 : { "number_parameters" : 1, "number_output_parameters" : 0 },
    5 : { "number_parameters" : 2, "number_output_parameters" : 0 },
    6 : { "number_parameters" : 2, "number_output_parameters" : 0 },
    7 : { "number_parameters" : 3, "number_output_parameters" : 1 },
    8 : { "number_parameters" : 3, "number_output_parameters" : 1 },
    99 : { "number_parameters" : 0, "number_output_parameters" : 0 },
}

class Amplifier:
    def __init__(self, _program):
        self.instruction_pointer = 0
        self.program = _program
        self.inputs = queue.Queue(maxsize=99)
        self.output = None
        self.paused = False
        self.halted = False

    def add_input(self, _input):
        self.inputs.put(_input)

    def get_output(self):
        return self.output

    def op_input(self, result_address):
        if self.inputs.empty():
            print("trying to get input from an empty queue")
        self.program[result_address] = self.inputs.get()

    def op_output(self, parameter):
        self.output = parameter
        self.paused = True

    def jump_true(self, parameter1, parameter2):
        if parameter1 != 0: return parameter2
        else: return None

    def jump_false(self, parameter1, parameter2):
        if parameter1 == 0: return parameter2
        else: return None 

    def add(self, parameter1, parameter2, result_address):
        self.program[result_address] = parameter1 + parameter2

    def mul(self, parameter1, parameter2, result_address):
        self.program[result_address] = parameter1 * parameter2

    def less(self, parameter1, parameter2, result_address):
        result = 0
        if parameter1 < parameter2: result = 1
        self.program[result_address] = result

    def equals(self, parameter1, parameter2, result_address):
        result = 0
        if parameter1 == parameter2: result = 1
        self.program[result_address] = result

    def get_opcode_parameters(self):
        opcode = int(str(self.program[self.instruction_pointer])[-2:])

        if opcode not in op_parameter_count.keys():
            print("opcode parameter count not found!")
        num_parameters = op_parameter_count[opcode]["number_parameters"]
        index_start_output_parameters = num_parameters - op_parameter_count[opcode]["number_output_parameters"]
        parameters = []
        modes = str(self.program[self.instruction_pointer])[:-2]
        modes = ''.join(reversed(modes))
        for i in range(num_parameters):
            parameter = self.program[self.instruction_pointer + i + 1]

            mode = 0
            if i < index_start_output_parameters:
                if i < len(modes):
                    mode = int(modes[i])
                if mode == 0:
                    parameter = self.program[parameter]

            parameters.append(parameter)

        return (opcode, parameters)

    def run_program(self):
        self.paused = False
        self.output = None

        while True:
            opcode, parameters = self.get_opcode_parameters()
            next_instruction_pointer = self.instruction_pointer + len(parameters) + 1
            #print(self.instruction_pointer)

            if opcode == 99:
                #print("Encountered opcode 99, breaking...")
                self.halted = True
            elif opcode == 1:
                self.add(parameters[0], parameters[1], parameters[2])
            elif opcode == 2:
                self.mul(parameters[0], parameters[1], parameters[2])
            elif opcode == 3:
                self.op_input(parameters[0])
            elif opcode == 4:
                self.op_output(parameters[0])
            elif opcode == 5:
                jump = self.jump_true(parameters[0], parameters[1])
                if jump != None:
                    next_instruction_pointer = jump
            elif opcode == 6:
                jump = self.jump_false(parameters[0], parameters[1])
                if jump != None:
                    next_instruction_pointer = jump
            elif opcode == 7:
                self.less(parameters[0], parameters[1], parameters[2])
            elif opcode == 8:
                self.equals(parameters[0], parameters[1], parameters[2])
            else:
                print("Unknown opcode: {}".format(opcode))

            self.instruction_pointer = next_instruction_pointer

            if self.paused or self.halted:
                break

#initial_program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#initial_program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
initial_program = [3,8,1001,8,10,8,105,1,0,0,21,38,47,72,97,122,203,284,365,446,99999,3,9,1001,9,3,9,1002,9,5,9,1001,9,4,9,4,9,99,3,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,102,5,9,9,101,3,9,9,1002,9,5,9,101,4,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,101,2,9,9,102,3,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,2,9,9,1001,9,4,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99]

def main():
    phase_settings = list(range(5, 10))
    phase_permutations = list(itertools.permutations(phase_settings))

    results = []
 
    for perm in phase_permutations:
        amplifiers = []
        for setting in perm:
            new_amp = Amplifier(initial_program.copy())
            new_amp.add_input(setting)
            amplifiers.append(new_amp)

        amplifiers[0].add_input(0)
        amp_index = 0
        amp = amplifiers[amp_index]

        while not amp.halted:
            amp = amplifiers[amp_index]

            #print("Running amp #{}".format(amp_index))
            amp.run_program()

            output = amplifiers[amp_index].get_output()
            amp_index += 1
            if amp_index >= len(amplifiers):
                amp_index = 0

            amplifiers[amp_index].add_input(output)

        results.append(amplifiers[-1].get_output())

    print(max(results))

if __name__== "__main__":
  main()