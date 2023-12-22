from os import path

input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#    input = f.read()

bricks = {}


def get_support(brick_key, brick, down=False):
    supportees = set()
    brick_type, block_coords = brick
    test_z = max([c[-1] for c in block_coords]) + 1

    if down:
        test_z = min([c[-1] for c in block_coords]) - 1
    for x, y, _ in block_coords:
        for test_brick_key, test_brick in bricks.items():
            if test_brick_key == brick_key:
                continue
            _, test_block_coords = test_brick
            if (x, y, test_z) in test_block_coords:
                supportees.add(test_brick_key)
    return supportees


def get_at_xy(brick_key, x, y):
    all_xyz = []
    for test_brick_key, brick in bricks.items():
        _, block_coords = brick
        if test_brick_key == brick_key:
            continue
        for block_x, block_y, block_z in block_coords:
            if block_x == x and block_y == y:
                all_xyz.append((block_x, block_y, block_z))
    return all_xyz


def try_fall_brick(brick_key, brick):
    can_fall = False

    _, block_coords = brick
    lowest_z = block_coords[0][2]
    if lowest_z > 1:
        can_all_blocks_fall = []
        for block_x, block_y, block_z in block_coords:
            can_block_fall = False
            if block_z > lowest_z:
                continue
            block_z -= 1
            test_coords_at_xy = get_at_xy(brick_key, block_x, block_y)
            test_all_z = [c[-1] for c in test_coords_at_xy]
            if block_z not in test_all_z:
                can_block_fall = True

            can_all_blocks_fall.append(can_block_fall)
        can_fall = all(can_all_blocks_fall)

    return can_fall


if __name__ == "__main__":
    for i, line in enumerate(input.splitlines()):
        start, end = line.split("~")
        start_x, start_y, start_z = [int(n) for n in start.split(",")]
        end_x, end_y, end_z = [int(n) for n in end.split(",")]

        blocks = []
        len_x = 0
        for x in range(start_x, end_x + 1):
            len_y = 0
            for y in range(start_y, end_y + 1):
                len_z = 0
                for z in range(start_z, end_z + 1):
                    block = (x, y, z)
                    blocks.append(block)
                    len_z += 1
                len_y += 1
            len_x += 1

        brick_type = None
        if len_y > 1:
            brick_type = "y"
        elif len_z > 1:
            brick_type = "z"
        else:
            brick_type = "x"
        brick_key = chr(ord("@") + i + 1)
        bricks[brick_key] = (brick_type, blocks)

    print("Settling bricks...")
    # Fall down all bricks
    while True:
        have_fallen = False
        for brick_key, brick in bricks.items():
            can_fall = try_fall_brick(brick_key, brick)
            if can_fall:
                new_block_coords = []
                brick_type, block_coords = brick
                for x, y, z in block_coords:
                    z -= 1
                    new_block_coords.append((x, y, z))
                bricks[brick_key] = (brick_type, new_block_coords)
                have_fallen = True
                # print(f"Brick {brick_key} falls down by 1!")
        if not have_fallen:
            break

    print("Checking for save removal...")
    remove_counter = 0
    # Chech supportees
    for brick_key, brick in bricks.items():
        can_be_removed = False
        supportee_brick_keys = get_support(brick_key, brick)
        if len(supportee_brick_keys) == 0:
            # print(f"Brick {brick_key} does not support any other brick!")
            can_be_removed = True
        else:
            # print(f"Brick {brick_key} supports another brick, checking...")
            all_have_support = []
            for supportee_brick_key in supportee_brick_keys:
                supportee_brick = bricks[supportee_brick_key]
                supporters = get_support(supportee_brick_key, supportee_brick, True)
                supporters.remove(brick_key)
                has_support = len(supporters) > 0
                if has_support:
                    supporter_brick_keys = [str(k) for k in supporters]
                    # print(
                    #    f"Brick {supportee_brick_key} is supported by {', '.join(supporter_brick_keys)}"
                    # )
                all_have_support.append(has_support)
            can_be_removed = all(all_have_support)
        if can_be_removed:
            # print(f"Brick {brick_key} can be safely removed!")
            remove_counter += 1

    print(remove_counter)
