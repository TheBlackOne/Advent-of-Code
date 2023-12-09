import re

input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

if __name__ == "__main__":
    sum = 0

    for line in input.splitlines():
        digits = re.findall(r"\d", line)
        first = digits[0]
        last = digits[-1]
        linedigits = f"{first}{last}"
        sum += int(linedigits)
        # (linedigits)

    print(f"Result: {sum}")
