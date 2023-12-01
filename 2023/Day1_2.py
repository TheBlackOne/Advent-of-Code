import regex as re

input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

numbers_string = '|'.join(numbers)

if __name__ == "__main__":
    sum = 0

    for line in input.splitlines():
        # overlapped=True is vital here!
        digits = re.findall(rf"(\d|{numbers_string})", line, overlapped=True)
        first = digits[0]
        last = digits[-1]

        #print(f"{line} = {first} {last}")

        if len(first) > 1:
            first = numbers.index(first) + 1

        if len(last) > 1:
            last = numbers.index(last) + 1

        linedigits = f"{first}{last}"
        sum += int(linedigits)
        print(linedigits)

    print(f"Result: {sum}")