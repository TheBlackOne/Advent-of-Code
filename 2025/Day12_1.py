input = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

# only works for my real data

#with open("input.txt") as f:
#   input = f.read()

shapes = []

if __name__ == "__main__":
    blocks = input.split("\n\n")
    shape_info = blocks[0:-1]
    fitments = blocks[-1].split('\n')

    shapes = []

    for si in shape_info:
        shapes.append(si.count('#'))

    num_fits = 0

    for fitment in fitments:
        xy, indices = fitment.split(': ')
        x, y = (int(c) for c in xy.split('x'))
        size = x * y
        needed_size = 0
        for i, num in enumerate(int(c) for c in indices.split()):
            needed_size += num * shapes[i]

        if needed_size <= size:
            num_fits += 1

    print(num_fits)