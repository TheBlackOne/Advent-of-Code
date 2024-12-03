import re

input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    expression = "(mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\))"
    instructions = re.findall(expression, input)

    sum = 0
    enabled = True

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            cleaned = instruction[4:-1]
            first, second = cleaned.split(",")
            sum += int(first) * int(second)

    print(sum)
