from collections import defaultdict

from tqdm import tqdm

input = """125 17"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    stones = list(input.split())

    for _ in tqdm(range(25)):
        new_stones = []
        for stone in stones:
            if stone == "0":
                new_stones.append("1")
            else:
                length = len(stone)
                if length % 2 == 0:
                    left = stone[0 : length // 2]
                    right = str(int(stone[length // 2 :]))
                    new_stones.append(left)
                    new_stones.append(right)
                else:
                    new_stones.append(str(int(stone) * 2024))
        stones = new_stones

    print(len(stones))
