from collections import defaultdict

from tqdm import tqdm

input = """125 17"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    stones = defaultdict(lambda: 0)
    for stone in list(input.split()):
        stones[stone] += 1

    for _ in tqdm(range(75)):
        new_stones = defaultdict(lambda: 0)

        for stone, num in stones.items():
            if stone == "0":
                new_stones["1"] += num
            else:
                length = len(stone)
                if length % 2 == 0:
                    left = stone[0 : length // 2]
                    right = str(int(stone[length // 2 :]))

                    new_stones[left] += num
                    new_stones[right] += num
                else:
                    new_stone = str(int(stone) * 2024)
                    new_stones[new_stone] += num

            stones = new_stones

    print(sum(stones.values()))
