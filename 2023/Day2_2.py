import math

input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

# with open('input.txt') as f:
#    input = f.read()


def processLine(line: str):
    min_cubes = {"red": None, "green": None, "blue": None}

    (_, cubes) = line.split(": ")
    rounds = cubes.split("; ")
    for round in rounds:
        count_colors = round.split(", ")
        for count_color in count_colors:
            (count, color) = count_color.split(" ")
            count = int(count)
            if min_cubes[color] == None or min_cubes[color] < count:
                min_cubes[color] = count

    return math.prod(min_cubes.values())


if __name__ == "__main__":
    sum = 0

    for line in input.splitlines():
        sum += processLine(line)

    print(f"Result: {sum}")
