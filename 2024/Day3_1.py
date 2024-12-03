import re

input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    expression = "mul\([0-9]+,[0-9]+\)"
    mul = re.findall(expression, input)

    sum = 0

    for instruction in mul:
        cleaned = instruction[4:-1]
        first, second = cleaned.split(",")
        sum += int(first) * int(second)

    print(sum)
