import math

input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    data = []
    for block in input.split("\n\n"):
        block = block.splitlines()
        button = block[0]
        xy_a = button.split(": ")[-1].split(", ")
        xy_a = tuple(map(int, [c.split("+")[-1] for c in xy_a]))

        button = block[1]
        xy_b = button.split(": ")[-1].split(", ")
        xy_b = tuple(map(int, [c.split("+")[-1] for c in xy_b]))

        prize = block[2]
        xy_price = prize.split(": ")[-1].split(", ")
        xy_price = tuple(map(int, [c.split("=")[-1] for c in xy_price]))

        data.append((xy_a, xy_b, xy_price))

    sum_tokens = 0
    for xy_a, xy_b, xy_price in data:
        max_presses_a = int(math.ceil(xy_price[0] / xy_a[0]))
        for num_presses_a in range(max_presses_a, 0, -1):
            x_travel_a = num_presses_a * xy_a[0]
            x_travel_left = xy_price[0] - x_travel_a
            b_can_reach = x_travel_left % xy_b[0]
            if b_can_reach == 0:
                num_presses_b = x_travel_left // xy_b[0]

                if num_presses_a * xy_a[1] + num_presses_b * xy_b[1] == xy_price[1]:
                    sum_tokens += num_presses_a * 3 + num_presses_b
                    break

    print(sum_tokens)
