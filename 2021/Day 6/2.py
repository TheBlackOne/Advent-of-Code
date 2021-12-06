import numpy as np

lanternfish = {}
for age in range(-1, 9): lanternfish[age] = 0

with open('input.txt', 'r') as file:
    lanternfish_ages = np.array([int(_) for _ in file.read().split(',')])
    (unique, counts) = np.unique(lanternfish_ages, return_counts=True)
    for age, num in zip(unique, counts):
        lanternfish[age] = num
    print()

for _ in range(0, 256):
    for age, num in lanternfish.items():
        if age > -1:
            lanternfish[age - 1] = num

    num_new_born = lanternfish[-1]
    lanternfish[8] = num_new_born
    lanternfish[6] += num_new_born

print(sum(lanternfish.values()))