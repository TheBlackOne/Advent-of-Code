import os
import heapq

directions = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0)}

ninetee_degrees = {"N": ("W", "E"), "S": ("W", "E"), "W": ("N", "S"), "E": ("N", "S")}

input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

map = []
max_x, max_y = 0, 0
goal_x, goal_y = 0, 0

dir = os.path.dirname(__file__)
input_path = os.path.join(dir, "input.txt")
# with open(input_path) as f:
#   input = f.read()


def is_on_map(x, y):
    global max_x, max_y

    if x >= 0 and x <= max_x and y >= 0 and y <= max_y:
        return True
    else:
        return False


def dijkstra(map):
    global max_x
    global max_y
    global directions
    global goal_x, goal_y

    visited = set()

    priority_queue = []

    start_positions = [(1, 0, "E"), (0, 1, "S")]

    for x, y, direction in start_positions:
        heat_loss = map[y][x]
        queue_key = (heat_loss, x, y, direction, 1)
        heapq.heappush(priority_queue, queue_key)

    while priority_queue:
        (heat_loss, x, y, direction, dir_steps) = heapq.heappop(priority_queue)

        if (x, y) == (goal_x, goal_y):
            print(f"Total heat loss: {heat_loss}")
            break

        visited_key = (x, y, direction, dir_steps)
        if visited_key in visited:
            continue

        visited.add(visited_key)

        if dir_steps < 10:
            (step_x, step_y) = directions[direction]
            new_x = x + step_x
            new_y = y + step_y

            if is_on_map(new_x, new_y):
                new_heat_loss = heat_loss + map[new_y][new_x]
                queue_key = (
                    new_heat_loss,
                    new_x,
                    new_y,
                    direction,
                    dir_steps + 1,
                )
                heapq.heappush(priority_queue, queue_key)

        if dir_steps >= 4:
            for new_direction in ninetee_degrees[direction]:
                (step_x, step_y) = directions[new_direction]
                new_x = x + step_x
                new_y = y + step_y

                if is_on_map(new_x, new_y):
                    new_heat_loss = heat_loss + map[new_y][new_x]
                    queue_key = (new_heat_loss, new_x, new_y, new_direction, 1)
                    heapq.heappush(priority_queue, queue_key)


if __name__ == "__main__":
    for line in input.splitlines():
        map.append([int(c) for c in line])
    max_x = len(map[0]) - 1
    max_y = len(map) - 1
    goal_x = max_x
    goal_y = max_y

    dijkstra(map)
