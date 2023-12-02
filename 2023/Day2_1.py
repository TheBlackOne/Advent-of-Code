input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

with open('input.txt') as f:
    input = f.read()

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def processLine(line: str):
    id = 0

    (game, cubes) = line.split(': ')
    (_, id) = game.split(' ')
    id = int(id)
    rounds = cubes.split('; ')
    for round in rounds:
        count_colors = round.split(', ')
        for count_color in count_colors:
            (count, color) = count_color.split(' ')
            if int(count) > max_cubes[color]:
                return (id, False)
            
    return (id, True)

if __name__ == "__main__":
    sum = 0

    for line in input.splitlines():
        (id, possible) = processLine(line)
        if possible:
            sum += id        

    print(f"Result: {sum}")