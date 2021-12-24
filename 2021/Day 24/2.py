from tqdm.contrib.itertools import product
from tqdm import tqdm
import json
import copy

instructions = []

variables = { 'w': 0, 'x': 0, 'y': 0, 'z': 0 }

def get_values(first, second):
    global variables
    value1 = variables[first]
    value2 = None
    if second in variables.keys():
        value2 = copy.deepcopy(variables[second])
    else:
        value2 = int(second)
    return (value1, value2)

def inp(destination, value):
    variables[destination] = value

def add(parameters):
    first, second = parameters
    value1, value2 = get_values(first, second)
    variables[first] = value1 + value2

def mul(parameters):
    first, second = parameters
    value1, value2 = get_values(first, second)
    variables[first] = value1 * value2

def div(parameters):
    first, second = parameters
    value1, value2 = get_values(first, second)
    variables[first] = int(value1 / value2)

def mod(parameters):
    first, second = parameters
    value1, value2 = get_values(first, second)
    variables[first] = value1 % value2

def eql(parameters):
    first, second = parameters
    value1, value2 = get_values(first, second)
    variables[first] = int(value1 == value2)

with open('input.txt', 'r') as file:
    for block in file.read().split('inp w'):
        if block == "": continue
        new_instructions = [(inp, 'w')]
        for line in block.split('\n'):
            if line == "": continue
            parts = line.split()
            cmd = parts[0]
            parameters = None
            if cmd == 'inp':
                cmd = inp
                parameters = parts[1]
            else:
                parameters = (parts[1], parts[2])
                if cmd == 'add': cmd = add
                elif cmd == 'mul': cmd = mul
                elif cmd == 'div': cmd = div
                elif cmd == 'mod': cmd = mod
                elif cmd == 'eql': cmd = eql
            new_instructions.append((cmd, parameters))
        instructions.append(new_instructions)

z_values = { 0: 0 }
step = 1

for block in instructions:
    new_z_values = {}
    print("step: {}".format(step))

    for input, state in product(range(1, 10), z_values.items()):
        z, number = state
        variables = { 'w': 0, 'x': 0, 'y': 0, 'z': z }

        for cmd, parameters in block:
            if cmd == inp: cmd(parameters, input)
            else: cmd(parameters)

        new_z = copy.deepcopy(variables['z'])
        new_number = number * 10 + input
        if new_z not in new_z_values.keys():
            new_z_values[new_z] = new_number
        else:
            if new_number < new_z_values[new_z]: new_z_values[new_z] = new_number
        
    step += 1
    z_values = new_z_values

print(z_values[0])