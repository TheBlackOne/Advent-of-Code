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


def process(operants, test_value):
    global sum

    if len(operants) > 1:
        if operants[0] > test_value:
            return

        plus_result = operants[0] + operants[1]
        mul_result = operants[0] * operants[1]
        concat_result = int(str(operants[0]) + str(operants[1]))

        plus_list = operants[1:]
        plus_list[0] = plus_result

        mul_list = operants[1:]
        mul_list[0] = mul_result

        concat_list = operants[1:]
        concat_list[0] = concat_result

        process(plus_list, test_value)
        process(mul_list, test_value)
        process(concat_list, test_value)
    else:
        if operants[0] == test_value:
            valid_test_values.add(test_value)


if __name__ == "__main__":
    for line in tqdm(input.splitlines()):
        test_value, operants = line.split(": ")
        test_value = int(test_value)
        operants = list(map(int, operants.split()))

        process(operants, test_value)

    print(sum(valid_test_values))
