from colorama import init, Fore
init()

from intcode_cpu import IntcodeCPU

direction_vectors = ((0, 1),(1, 0),(0, -1),(-1, 0))
direction_index = 0

def calc_turn(clockwise):
    global direction_index

    increment = -1
    if clockwise: increment = 1

    direction_index += increment
    if direction_index < 0: direction_index = len(direction_vectors) - 1
    elif direction_index >= len(direction_vectors): direction_index = 0

    return direction_vectors[direction_index]

initial_program = [3,8,1005,8,335,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,28,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,51,1006,0,82,1006,0,56,1,1107,0,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,83,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,104,1006,0,58,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,129,1006,0,54,1006,0,50,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,161,2,101,14,10,1006,0,43,1006,0,77,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,193,2,101,12,10,2,109,18,10,1,1009,13,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,226,1,1103,1,10,1,1007,16,10,1,3,4,10,1006,0,88,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,263,1006,0,50,2,1108,17,10,1006,0,36,1,9,8,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,300,1006,0,22,2,106,2,10,2,1001,19,10,1,3,1,10,101,1,9,9,1007,9,925,10,1005,10,15,99,109,657,104,0,104,1,21101,0,937268454156,1,21102,1,352,0,1106,0,456,21101,0,666538713748,1,21102,363,1,0,1105,1,456,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,3316845608,0,1,21102,1,410,0,1105,1,456,21101,0,209475103911,1,21101,421,0,0,1106,0,456,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,984353603944,1,21101,444,0,0,1105,1,456,21102,1,988220752232,1,21102,1,455,0,1106,0,456,99,109,2,22101,0,-1,1,21102,40,1,2,21101,487,0,3,21101,0,477,0,1106,0,520,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,482,483,498,4,0,1001,482,1,482,108,4,482,10,1006,10,514,1102,0,1,482,109,-2,2105,1,0,0,109,4,2101,0,-1,519,1207,-3,0,10,1006,10,537,21101,0,0,-3,22101,0,-3,1,22101,0,-2,2,21102,1,1,3,21101,556,0,0,1106,0,561,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,584,2207,-4,-2,10,1006,10,584,21201,-4,0,-4,1106,0,652,22101,0,-4,1,21201,-3,-1,2,21202,-2,2,3,21101,0,603,0,1105,1,561,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,622,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,644,21201,-1,0,1,21101,644,0,0,105,1,519,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

def main():
    visited_fields = {}
    bot_position = (0, 0)
    turn_direction = direction_vectors[0]

    cpu = IntcodeCPU(initial_program.copy())
    # part 1
    #cpu.add_input(0)
    
    # part 2
    cpu.add_input(1)

    lowestx = 0
    lowesty = 0
    highestx = 0
    highesty = 0

    while not cpu.halted:
        cpu.run_program()
        color = cpu.get_output()
        visited_fields[bot_position] = color

        cpu.run_program()
        turn = cpu.get_output()

        turn_direction = calc_turn(turn)
        bot_position = tuple(map(lambda x, y: x + y, bot_position, turn_direction))

        if bot_position not in visited_fields.keys():
            cpu.add_input(0)
        else:
            cpu.add_input(visited_fields[bot_position])

        x, y = bot_position
        if x < lowestx: lowestx = x
        if y < lowesty: lowesty = y
        if x > highestx: highestx = x
        if y > highesty: highesty = y
    
    num_visited = len(visited_fields.keys())
    print("Fields visited (at least once): {}".format(num_visited))

    for y in reversed(range(lowesty, highesty + 1)):
        for x in range(lowestx, highestx + 1):
            if (x, y) in visited_fields.keys():
                color = visited_fields[(x, y)]
                if color == 0:
                    print(Fore.BLACK + "█", end = '')
                elif color == 1:
                    print(Fore.WHITE + "█", end = '')
            else:
                print(" ", end = '')
        print("")

if __name__== "__main__":
  main()