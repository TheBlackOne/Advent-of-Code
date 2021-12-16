import math

binary_transmission = ""

with open('input.txt', 'r') as file:
    for char in file.read().strip():
        binary_transmission += "{0:04b}".format(int(char, 16))

def get_header(cursor):
    version = int(binary_transmission[cursor:cursor+3], 2)
    type = int(binary_transmission[cursor+3:cursor+6], 2)

    return (version, type, cursor + 6)

def parse_4(cursor):
    payload = binary_transmission[cursor:]
    value_string = ""
    while True:
        part = binary_transmission[cursor:cursor+5]
        value_string += part[1:]
        cursor += 5
        if part[0] == '0': break

    value = int(value_string, 2)
    
    return (value, cursor)

def parse(cursor=0):
    values = []

    version, type_id, cursor = get_header(cursor)
    if type_id == 4:
        value, cursor = parse_4(cursor)
        values.append(value)
    else:
        length_type_id = int(binary_transmission[cursor], 2)
        cursor += 1
        if length_type_id == 0:
            length = int(binary_transmission[cursor:cursor + 15], 2)
            cursor += 15
            start_cursor = cursor
            while True:
                local_values, cursor = parse(cursor)
                values += local_values
                if cursor - start_cursor >= length: break
        else:
            count = int(binary_transmission[cursor:cursor + 11], 2)
            cursor += 11
            for _ in range(count):
                local_values, cursor = parse(cursor)
                values += local_values

    if type_id == 0:
        values = [sum(values)]
    elif type_id == 1:
        values = [math.prod(values)]
    elif type_id == 2:
        values = [min(values)]
    elif type_id == 3:
        values = [max(values)]
    elif type_id == 5:
        greater = values[0] > values[1]
        values = [int(greater)]
    elif type_id == 6:
        less = values[0] < values[1]
        values = [int(less)]
    elif type_id == 7:
        equal = values[0] == values[1]
        values = [int(equal)]

    return (values, cursor)
        
value, _ = parse()
print(value)