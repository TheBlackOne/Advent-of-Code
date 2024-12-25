input = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    locks = []
    keys = []
    locks_keys = input.split("\n\n")
    for lock_key in locks_keys:
        rows = lock_key.splitlines()
        pins = [0, 0, 0, 0, 0]
        if rows[0] == "#####":
            for row in rows[1:]:
                for i, pin in enumerate(row):
                    if pin == "#":
                        pins[i] += 1
            locks.append(pins)
        else:
            for row in rows[:-1]:
                for i, pin in enumerate(row):
                    if pin == "#":
                        pins[i] += 1
            keys.append(pins)

    num_fits = 0
    for lock in locks:
        for key in keys:
            pin_fits = [k + l for k, l in zip(lock, key)]
            if max(pin_fits) <= 5:
                num_fits += 1

    print(num_fits)
