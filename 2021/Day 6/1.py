import numpy as np

lanternfish = []
with open('input.txt', 'r') as file:
    lanternfish = np.array([int(_) for _ in file.read().split(',')])

for _ in range(80):
    with np.nditer(lanternfish, op_flags=['readwrite']) as it:
        for fish in it:
            fish -= 1

    fish_give_birth = np.where(lanternfish == -1)[0]
    for index in fish_give_birth:
        lanternfish[index] = 6

    num_new_fish = len(fish_give_birth)
    lanternfish = np.append(lanternfish, np.repeat(8, num_new_fish))

print(len(lanternfish))