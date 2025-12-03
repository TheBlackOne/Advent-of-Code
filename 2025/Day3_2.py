input = """987654321111111
811111111111119
234234234234278
818181911112111"""

#with open("input.txt") as f:
#   input = f.read()

joltage_sum = 0

def next_battery(bank, num):
    limit = len(bank) - num + 1
    max_batt = max(bank[:limit])
    pos = bank.index(max_batt)

    if num == 1:
        return str(max_batt)
    else:
        return str(max_batt) + next_battery(bank[pos + 1:], num - 1)

if __name__ == "__main__":
    for line in input.splitlines():
        batteries = [int(b) for b in line]
        joltage = next_battery(batteries, 12)

        joltage_sum += int(joltage)

print(joltage_sum)