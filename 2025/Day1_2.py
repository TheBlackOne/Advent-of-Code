input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

#with open("input.txt") as f:
#   input = f.read()

current = 50
password = 0

if __name__ == "__main__":
    for line in input.splitlines():
        direction = line[0]
        distance = int(line[1:])
        if direction == 'R':
            for _ in range(distance):
                current += 1
                if current > 99:
                    current = 0
                if current == 0:
                    password += 1
        elif direction == 'L':
            for _ in range(distance):
                current -= 1
                if current == 0:
                    password += 1
                if current < 0:
                    current = 99

print(password)
