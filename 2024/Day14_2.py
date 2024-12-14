from PIL import Image

width = 101
height = 103
max_steps = width * height
with open("input.txt") as f:
    input = f.read()


def draw_image(robots):
    global width
    global height

    with Image.new("RGB", (width, height)) as img:
        for x, y, _, _ in robots:
            img.putpixel((x, y), (255, 255, 255))
        img.save("day14_part2.png")


if __name__ == "__main__":
    robots = []
    for line in input.splitlines():
        p, v = line.split(" ")
        x, y = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robots.append((x, y, vx, vy))

    for step in range(max_steps):
        for i, robot in enumerate(robots):
            x, y, vx, vy = robot
            x += vx
            x = x % width

            y += vy
            y = y % height

            robots[i] = (x, y, vx, vy)

        coords = set((x, y) for x, y, _, _ in robots)

        if len(coords) == len(robots):
            draw_image(robots)
            print(f"Found at step {step + 1}!")
            break
