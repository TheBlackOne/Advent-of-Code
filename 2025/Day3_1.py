input = """987654321111111
811111111111119
234234234234278
818181911112111"""

#with open("input.txt") as f:
#   input = f.read()

joltage_sum = 0

if __name__ == "__main__":
    for line in input.splitlines():
        batteries = [int(b) for b in line]
        first_max = max(batteries[:-1])
        first_pos = batteries[:-1].index(first_max)
        second_max = max(batteries[first_pos + 1:])
        joltage = first_max * 10 + second_max
        joltage_sum += joltage

print(joltage_sum)