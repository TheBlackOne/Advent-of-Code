import queue

op_parameter_count = {
    1 : { "number_parameters" : 3 },
    2 : { "number_parameters" : 3 },
    3 : { "number_parameters" : 1 },
    4 : { "number_parameters" : 1 },
    5 : { "number_parameters" : 2 },
    6 : { "number_parameters" : 2 },
    7 : { "number_parameters" : 3 },
    8 : { "number_parameters" : 3 },
    9 : { "number_parameters" : 1 },
    99 : { "number_parameters" : 0 },
}

class IntcodeCPU:
    def __init__(self, _program):
        self.instruction_pointer = 0
        self.program = _program
        self.inputs = queue.Queue(maxsize=99)
        self.output = None
        self.paused = False
        self.halted = False
        self.relative_base = 0

    def add_input(self, _input):
        self.inputs.put(_input)

    def get_output(self):
        return self.output

    def op_input(self, result_address):
        if self.inputs.empty():
            print("trying to get input from an empty queue")
        self.write_to_address(result_address, self.inputs.get())

    def op_output(self, address):
        parameter = self.read_from_address(address)
        self.output = parameter
        self.paused = True

    def jump_true(self, address1, address2):
        parameter1 = self.read_from_address(address1)
        parameter2 = self.read_from_address(address2)
        if parameter1 != 0: return parameter2
        else: return None

    def jump_false(self, address1, address2):
        parameter1 = self.read_from_address(address1)
        parameter2 = self.read_from_address(address2)
        if parameter1 == 0: return parameter2
        else: return None 

    def add(self, address1, address2, result_address):
        parameter1 = self.read_from_address(address1)
        parameter2 = self.read_from_address(address2)
        self.write_to_address(result_address, parameter1 + parameter2)

    def mul(self, address1, address2, result_address):
        parameter1 = self.read_from_address(address1)
        parameter2 = self.read_from_address(address2)
        self.write_to_address(result_address, parameter1 * parameter2)

    def less(self, address1, address2, result_address):
        parameter1 = self.read_from_address(address1)
        parameter2 = self.read_from_address(address2)
        result = int(parameter1 < parameter2)
        self.write_to_address(result_address, result)

    def equals(self, address1, address2, result_address):
        parameter1 = self.read_from_address(address1)
        parameter2 = self.read_from_address(address2)
        result = int(parameter1 == parameter2)
        self.write_to_address(result_address, result)

    def adjust_relative_base(self, address):
        parameter = self.read_from_address(address)
        self.relative_base += parameter

    def check_and_extend_memory(self, address):
        if address >= len(self.program):
            extend_by = address - len(self.program)
            for i in range(extend_by + 1):
                self.program.append(0)

    def read_from_address(self, address):
        self.check_and_extend_memory(address)
        return self.program[address]

    def write_to_address(self, address, value):
        self.check_and_extend_memory(address)
        self.program[address] = value

    def get_opcode_parameter_addresses(self):
        opcode = self.read_from_address(self.instruction_pointer) % 100

        if opcode not in op_parameter_count.keys():
            print("opcode parameter count not found! Opcode was: \"{}\"".format(opcode))

        num_parameters = op_parameter_count[opcode]["number_parameters"]
        parameter_addresses = []

        for i in range(num_parameters):
            mode = self.read_from_address(self.instruction_pointer) // (10 ** (2 + i)) % 10

            parameter_address = self.instruction_pointer + i + 1
            if mode == 0:
                parameter_address = self.read_from_address(parameter_address)
            elif mode == 2:
                parameter_address = self.relative_base + self.read_from_address(parameter_address)

            parameter_addresses.append(parameter_address)

        return (opcode, parameter_addresses)

    def run_program(self):
        self.paused = False
        self.output = None

        while True:
            opcode, parameter_addresses = self.get_opcode_parameter_addresses()
            next_instruction_pointer = self.instruction_pointer + len(parameter_addresses) + 1

            if opcode == 99:
                #print("Encountered opcode 99, breaking...")
                self.halted = True
            elif opcode == 1:
                self.add(parameter_addresses[0], parameter_addresses[1], parameter_addresses[2])
            elif opcode == 2:
                self.mul(parameter_addresses[0], parameter_addresses[1], parameter_addresses[2])
            elif opcode == 3:
                self.op_input(parameter_addresses[0])
            elif opcode == 4:
                self.op_output(parameter_addresses[0])
            elif opcode == 5:
                jump = self.jump_true(parameter_addresses[0], parameter_addresses[1])
                if jump != None:
                    next_instruction_pointer = jump
            elif opcode == 6:
                jump = self.jump_false(parameter_addresses[0], parameter_addresses[1])
                if jump != None:
                    next_instruction_pointer = jump
            elif opcode == 7:
                self.less(parameter_addresses[0], parameter_addresses[1], parameter_addresses[2])
            elif opcode == 8:
                self.equals(parameter_addresses[0], parameter_addresses[1], parameter_addresses[2])
            elif opcode == 9:
                self.adjust_relative_base(parameter_addresses[0])
            else:
                print("Unknown opcode: {}".format(opcode))

            self.instruction_pointer = next_instruction_pointer

            if self.paused or self.halted:
                break