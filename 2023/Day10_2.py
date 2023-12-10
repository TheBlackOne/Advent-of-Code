import sys

sys.setrecursionlimit(5000)

input = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

# with open("input.txt") as f:
#    input = f.read()

pipes = []
cleaned_pipes = []

directions = {"W": (-1, 0), "S": (0, 1), "E": (1, 0), "N": (0, -1)}

pipe_directions = {
    "|": {"S": "S", "N": "N"},
    "-": {"W": "W", "E": "E"},
    "L": {"S": "E", "W": "N"},
    "J": {"S": "W", "E": "N"},
    "7": {"N": "W", "E": "S"},
    "F": {"N": "E", "W": "S"},
}

opposite_direction = {"N": "S", "S": "N", "E": "W", "W": "E"}

direction_left_right = {
    "N": ("W", "E"),
    "S": ("E", "W"),
    "W": ("S", "N"),
    "E": ("N", "S"),
}

max_x, max_y = 0, 0


def flood_fill(x, y, fill_char):
    global cleaned_pipes
    global max_x
    global max_y

    for x_offset, y_offset in directions.values():
        check_x = x + x_offset
        check_y = y + y_offset
        if check_x >= 0 and check_x < max_x and check_y >= 0 and check_y < max_y:
            if cleaned_pipes[check_y][check_x] == " ":
                cleaned_pipes[check_y][check_x] = fill_char
                flood_fill(check_x, check_y, fill_char)


if __name__ == "__main__":
    for line in input.splitlines():
        pipes.append([*line])

    max_x = len(pipes[0])
    max_y = len(pipes)

    for start_y, row in enumerate(pipes):
        if "S" in row:
            start_x = row.index("S")
            break

    last_directions = []
    loop_coords = []
    loop_directions = []

    for direction, (x_offset, y_offset) in directions.items():
        if direction in last_directions:
            continue

        step_counter = 1
        x = start_x + x_offset
        y = start_y + y_offset
        if x < 0 or y < 0 or pipes[y][x] == ".":
            continue

        new_loop_coords = [(x, y)]
        current_pipe = pipes[y][x]
        new_loop_directions = [direction]

        while current_pipe in pipe_directions.keys():
            current_pipe_directions = pipe_directions[current_pipe]
            if direction not in current_pipe_directions.keys():
                break
            new_direction = current_pipe_directions[direction]
            (x_offset, y_offset) = directions[new_direction]
            x += x_offset
            y += y_offset
            new_loop_coords.append((x, y))
            new_loop_directions.append(new_direction)
            direction = new_direction
            current_pipe = pipes[y][x]
            step_counter += 1

        if current_pipe == "S":
            last_directions.append(opposite_direction[direction])
            loop_coords = new_loop_coords
            loop_directions = new_loop_directions

    for y, row in enumerate(pipes):
        cleaned_row = ""
        for x, pipe in enumerate(row):
            if (x, y) not in loop_coords:
                pipes[y][x] = " "

    cleaned_pipes = pipes

    empty_fields_left_right = [set(), set()]
    # check forwards
    for (x, y), direction in zip(loop_coords, loop_directions):
        left_right = direction_left_right[direction]
        for index, check_direction in enumerate(left_right):
            (offset_x, offset_y) = directions[check_direction]
            check_x = x + offset_x
            check_y = y + offset_y
            if check_x < 0 or check_y < 0 or check_x >= max_x or check_y >= max_y:
                continue

            pipe = cleaned_pipes[check_y][check_x]
            if pipe == " ":
                cleaned_pipes[check_y][check_x] = str(index)
                empty_fields_left_right[index].add((check_x, check_y))

    # check backwards
    for (x, y), direction in zip(loop_coords[::-1], loop_directions[::-1]):
        pipe = cleaned_pipes[y][x]
        if pipe != "S":
            direction = pipe_directions[pipe][direction]
            direction = opposite_direction[direction]
            left_right = direction_left_right[direction]
            for index, check_direction in enumerate(left_right[::-1]):
                (offset_x, offset_y) = directions[check_direction]
                check_x = x + offset_x
                check_y = y + offset_y
                if check_x < 0 or check_y < 0 or check_x >= max_x or check_y >= max_y:
                    continue

                pipe = cleaned_pipes[check_y][check_x]
                if pipe == " ":
                    cleaned_pipes[check_y][check_x] = str(index)
                    empty_fields_left_right[index].add((check_x, check_y))

    # flood fill
    for index, inside_candidates in enumerate(empty_fields_left_right):
        for x, y in inside_candidates:
            flood_fill(x, y, str(index))

    # with open("output.txt", "w") as filehandle:
    #    for line in cleaned_pipes:
    #        filehandle.write("".join(line))
    #        filehandle.write("\n")

    sums = []
    for index in (0, 1):
        linesum = 0
        for line in cleaned_pipes:
            linesum += line.count(str(index))
        sums.append(linesum)

    print(f"One of these two numbers is the correct answer: {sums}")
