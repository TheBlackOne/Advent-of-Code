import itertools

input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

# with open('input.txt') as f:
#    input = f.read()

if __name__ == "__main__":
    sum_safe = 0
    for report in input.splitlines():
        # print(report)
        increase_decrease = 0
        finished = True
        numbers = report.split()
        for first, second in zip(numbers[:-1], numbers[1:]):
            # (f"{first} {second}")
            d = int(first) - int(second)

            if abs(d) in range(1, 4):
                id = d // abs(d)
                if increase_decrease == 0:
                    increase_decrease = id
                else:
                    if id != increase_decrease:
                        finished = False
                        break
            else:
                finished = False
                break

        if finished:
            sum_safe += 1

    print(sum_safe)
