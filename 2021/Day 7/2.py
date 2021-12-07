import numpy as np

with open('input.txt', 'r') as file:
    positions = np.array([int(_) for _ in file.read().split(',')])

def calc_fuel(distance):
    return sum(range(1, distance + 1))
calc_fuel = np.vectorize(calc_fuel)

fuels = []
for position in positions:
    fuel = np.sum(calc_fuel(np.absolute(np.subtract(positions, position))))
    fuels.append(fuel)

fuels.sort()
print(fuels[0])