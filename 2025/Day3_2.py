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
        batteries_on = []
        max_pos = -1
        for margin in reversed(range(12)):
            batteries_temp = batteries[max_pos + 1:-margin]
            if margin == 0:
                batteries_temp = batteries[max_pos + 1:]
            
            max_battery = max(batteries_temp)
            batteries_on.append(str(max_battery))

            # the start parameter is important here, it finds the wrong batteries otherwise
            max_pos = batteries.index(max_battery, max_pos + 1)

        joltage = int(''.join(batteries_on))
        joltage_sum += joltage

print(joltage_sum)