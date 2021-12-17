# test input
target = ((20, 30), (-10, -5))

hits = 0

for init_vel_x in range(1, target[0][1] + 1):
    for init_vel_y in range(target[1][0], 5000):
        x = 0
        y = 0
        vel_x = init_vel_x
        vel_y = init_vel_y

        hit = False

        while not hit:
            x += vel_x
            y += vel_y
            if vel_x > 0: vel_x -= 1
            elif vel_x < 0: vel_x += 1
            vel_y -= 1

            if target[0][0] <= x <= target[0][1] and target[1][0] <= y <= target[1][1]:
                hit = True
                print("{}:{}".format(init_vel_x, init_vel_y))
                hits += 1

            if x > target[0][1]: break
            if x < target[0][0] and vel_x == 0: break
            if y < target[1][0]: break

print(hits)