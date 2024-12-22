from tqdm import tqdm

input = """1
10
100
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
    new_secret_numbers = []
    iterations = 2000
    secret_numbers = list(map(int, input.splitlines()))

    for secret_number in tqdm(secret_numbers):
        for _ in range(iterations):
            secret_number = generate(secret_number)
        new_secret_numbers.append(secret_number)

    print(sum(new_secret_numbers))
