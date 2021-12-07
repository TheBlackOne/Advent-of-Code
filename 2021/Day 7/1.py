import numpy as np

with open('input.txt', 'r') as file:
    positions = np.array([int(_) for _ in file.read().split(',')])

fuels = []
for position in positions:
    fuel = np.sum(np.absolute(np.subtract(positions, position)))
    fuels.append(fuel)

fuels.sort()
print(fuels[0])