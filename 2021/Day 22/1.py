from itertools import product

cubes = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        on_off, dimensions = line.split()
        if on_off == 'on': on_off = 1
        else: on_off = 0

        cube = []
        for dimension in dimensions.split(','):
            _, length = dimension.split('=')
            start, end = length.split('..')
            cube.append((int(start), int(end)))
        cubes.append((cube, on_off))

reactor = {}

for cube, on_off in cubes:
    x_dim, y_dim, z_dim = cube
    x1, x2 = x_dim
    y1, y2 = y_dim
    z1, z2 = z_dim

    if all(dim >= -50 and dim <= 50 for dim in (x1, x2, y1, y2, z1, z2)):
        for x, y, z in product(range(x1, x2 + 1), range(y1, y2 + 1), range(z1, z2 + 1)):
            reactor[(x, y, z)] = on_off
            
print(sum(reactor.values()))