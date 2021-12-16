binary_transmission = ""

versions = []

with open('input.txt', 'r') as file:
    for char in file.read().strip():
        binary_transmission += "{0:04b}".format(int(char, 16))

def get_header(cursor):
    version = int(binary_transmission[cursor:cursor+3], 2)
    type = int(binary_transmission[cursor+3:cursor+6], 2)

    versions.append(version)

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
    print("Value: {}".format(value))
    
    return (value, cursor)

def parse(cursor=0):
    version, type_id, cursor = get_header(cursor)
    if type_id == 4:
        value, cursor = parse_4(cursor)
    else:
        length_type_id = int(binary_transmission[cursor], 2)
        cursor += 1
        if length_type_id == 0:
            length = int(binary_transmission[cursor:cursor + 15], 2)
            cursor += 15
            start_cursor = cursor
            while True:
                value, cursor = parse(cursor)
                if cursor - start_cursor >= length: break
        else:
            count = int(binary_transmission[cursor:cursor + 11], 2)
            cursor += 11
            for _ in range(count):
                value, cursor = parse(cursor)
    return (0, cursor)
        
parse()
print(sum(versions))