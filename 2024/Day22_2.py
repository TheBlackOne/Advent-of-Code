from collections import defaultdict

from tqdm import tqdm

input = """1
2
3
2024"""

# with open("input.txt") as f:
#    input = f.read()


def generate(secret_number):
    result1 = secret_number * 64
    secret_number = result1 ^ secret_number
    secret_number = secret_number % 16777216

    result2 = secret_number // 32
    secret_number = result2 ^ secret_number
    secret_number = secret_number % 16777216

    result3 = secret_number * 2048
    secret_number = result3 ^ secret_number
    secret_number = secret_number % 16777216

    return secret_number


if __name__ == "__main__":
    iterations = 2000
    secret_numbers = list(map(int, input.splitlines()))

    banana_maps = []

    for secret_number in tqdm(secret_numbers):
        buyer_banana_map = {}
        buyer_secret_numbers = [int(str(secret_number)[-1])]
        for _ in range(iterations):
            secret_number = generate(secret_number)
            buyer_secret_numbers.append(int(str(secret_number)[-1]))

        price_changes = []
        for s1, s2 in zip(buyer_secret_numbers[:-1], buyer_secret_numbers[1:]):
            price_changes.append(s2 - s1)

        for i, price in enumerate(buyer_secret_numbers[4:], 3):
            if price > 0:
                sequence_key = (
                    price_changes[i - 3],
                    price_changes[i - 2],
                    price_changes[i - 1],
                    price_changes[i],
                )

                if sequence_key not in buyer_banana_map.keys():
                    buyer_banana_map[sequence_key] = price

        banana_maps.append(buyer_banana_map)

    combined_banana_map = defaultdict(lambda: 0)
    for map in banana_maps:
        for k, v in map.items():
            combined_banana_map[k] += v

    print(max(combined_banana_map.values()))
