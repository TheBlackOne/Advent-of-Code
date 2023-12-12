from itertools import product, chain
from fnmatch import fnmatch
from more_itertools import roundrobin

input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

# with open("input.txt") as f:
#    input = f.read()


def get_perfect_arrangement(conditions):
    springs = ["#" * n for n in conditions]
    return ".".join(springs)


def compare_arrangements(arrangement1, arrangement2):
    return fnmatch(arrangement2, arrangement1)


def is_valid_arrangement(arrangement, conditions):
    arrangements = arrangement.split(".")
    group_lengths = [len(a) for a in arrangements if a != ""]

    return group_lengths == conditions


data = []

if __name__ == "__main__":
    lines = input.splitlines()
    for line in lines:
        arrangement, conditions = line.split()
        conditions = [int(c) for c in conditions.split(",")]
        data.append((arrangement, conditions))

    sums = 0

    for arrangement, conditions in data:
        perfect_arrangement = get_perfect_arrangement(conditions)
        len_difference = len(arrangement) - len(perfect_arrangement)

        if len_difference == 0:
            if compare_arrangements(arrangement, perfect_arrangement):
                sums += 1
        else:
            permutation_length = len(conditions) + 1
            formatting_string = ".".join(
                ["{}" * (len(conditions) + permutation_length)]
            )
            arrangement_groups = perfect_arrangement.split(".")
            factors = list(range(len_difference + 1))
            growth_factors = [
                c
                for c in product(factors, repeat=permutation_length)
                if sum(c) == len_difference
            ]

            for growth_factor in growth_factors:
                growth_groups = [
                    "." * g
                    if index == 0 or index == len(growth_factor) - 1
                    else "." * g + "."
                    for index, g in enumerate(growth_factor)
                ]

                test = list(roundrobin(growth_groups, arrangement_groups))
                test = "".join(test)
                # print(f"{arrangement}\n{test}\n")
                if compare_arrangements(arrangement, test):
                    sums += 1

    print(sums)
