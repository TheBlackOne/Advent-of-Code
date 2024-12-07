import math

from tqdm import tqdm

input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# with open("input.txt") as f:
#    input = f.read()

valid_test_values = set()


def process(first, rest, length, test_value):
    if length > 0:
        if first > test_value or test_value in valid_test_values:
            return

        plus_result = first + rest[0]
        mul_result = first * rest[0]

        # nice but does not speed things up
        # concat_result = first * 10 ** math.ceil(math.log(rest[0], 10)) + rest[0]
        concat_result = int(str(first) + str(rest[0]))

        length -= 1

        process(plus_result, rest[1:], length, test_value)
        process(mul_result, rest[1:], length, test_value)
        process(concat_result, rest[1:], length, test_value)
    else:
        if first == test_value:
            valid_test_values.add(test_value)


if __name__ == "__main__":
    for line in tqdm(input.splitlines()):
        test_value, operants = line.split(": ")
        test_value = int(test_value)
        operants = list(map(int, operants.split()))

        first = operants[0]
        rest = operants[1:]
        length = len(rest)
        process(first, rest, length, test_value)

    print(sum(valid_test_values))
