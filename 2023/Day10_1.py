input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

# with open("input.txt") as f:
#    input = f.read()

pipes = []

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

if __name__ == "__main__":
    for line in input.splitlines():
        pipes.append(line)

    for start_y, row in enumerate(pipes):
        if "S" in row:
            start_x = row.index("S")
            break

    last_directions = []

    for direction, (x_offset, y_offset) in directions.items():
        if direction in last_directions:
            continue

        step_counter = 1
        x = start_x + x_offset
        y = start_y + y_offset
        if x < 0 or y < 0 or pipes[y][x] == ".":
            continue

        current_pipe = pipes[y][x]
        while current_pipe in pipe_directions.keys():
            current_pipe_directions = pipe_directions[current_pipe]
            if direction not in current_pipe_directions.keys():
                break
            direction = current_pipe_directions[direction]
            (x_offset, y_offset) = directions[direction]
            x += x_offset
            y += y_offset
            current_pipe = pipes[y][x]
            step_counter += 1
            # print()

        if current_pipe == "S":
            last_directions.append(opposite_direction[direction])
            print(int(step_counter / 2))
