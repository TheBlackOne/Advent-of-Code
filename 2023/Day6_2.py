from tqdm import tqdm

input = """Time:      7  15   30
Distance:  9  40  200"""

# with open('input.txt') as f:
#    input = f.read()

if __name__ == "__main__":
    lines = input.splitlines()
    time = int(lines[0].split(": ")[-1].replace(" ", ""))
    distance = int(lines[1].split(": ")[-1].replace(" ", ""))

    result = 1

    num_wins = 0
    win_found = False

    for hold_time in tqdm(range(time)):
        speed = hold_time
        remaining_time = time - hold_time
        race_distance = speed * remaining_time

        if race_distance > distance:
            num_wins += 1
            win_found = True
        elif win_found:
            break

    result *= num_wins

    print(f"Result: {result}")
