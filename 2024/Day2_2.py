import itertools

input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# with open("input.txt") as f:
#    input = f.read()


def check_report(numbers):
    increase_decrease = 0
    is_safe = True

    for first, second in zip(numbers[:-1], numbers[1:]):
        d = int(first) - int(second)

        if abs(d) in range(1, 4):
            id = d // abs(d)
            if increase_decrease == 0:
                increase_decrease = id
            else:
                if id != increase_decrease:
                    is_safe = False
                    break
        else:
            is_safe = False
            break

    return is_safe


if __name__ == "__main__":
    sum_safe = 0
    for report in input.splitlines():
        numbers = report.split()

        if check_report(numbers):
            sum_safe += 1
        else:
            # print(report)

            for unsafe_index in range(len(numbers)):
                new_numbers = numbers[0:unsafe_index] + numbers[unsafe_index + 1 :]
                if check_report(new_numbers):
                    sum_safe += 1
                    break

    print(sum_safe)
