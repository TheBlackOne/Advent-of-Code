peak = 0

# test input
target = ((20, 30), (-10, -5))

for init_vel_x in range(1, target[0][1]):
    for init_vel_y in range(10000):
        x = 0
        y = 0
        vel_x = init_vel_x
        vel_y = init_vel_y
        local_peak = 0

        hit = False

        while not hit:
            x += vel_x
            y += vel_y
            if vel_x > 0: vel_x -= 1
            elif vel_x < 0: vel_x += 1
            vel_y -= 1

            if y > local_peak:
                local_peak = y

            if target[0][0] <= x <= target[0][1] and target[1][0] <= y <= target[1][1]:
                hit = True
                
                if local_peak > peak:
                    print("New peak found! {}".format(local_peak))
                    peak = local_peak

            if x > target[0][1]: break
            if x < target[0][0] and vel_x == 0: break
            if y < target[1][0]: break