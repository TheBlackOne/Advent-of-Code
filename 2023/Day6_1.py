input = """Time:      7  15   30
Distance:  9  40  200"""

# with open('input.txt') as f:
#    input = f.read()

races = []

if __name__ == "__main__":
    lines = input.splitlines()
    times = lines[0].split(": ")[-1].split()
    distances = lines[1].split(": ")[-1].split()

    for time, distance in zip(times, distances):
        races.append((int(time), int(distance)))

    result = 1

    for time, distance in races:
        num_wins = 0
        for hold_time in range(time):
            speed = hold_time
            remaining_time = time - hold_time
            race_distance = speed * remaining_time

            if race_distance > distance:
                num_wins += 1
        print(f"Ways to win: {num_wins}")
        result *= num_wins

    print(f"Result: {result}")
