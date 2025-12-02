from tqdm import tqdm
import functools
import itertools

input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

#with open("input.txt") as f:
#   input = f.read()

invalid_ids = []

def chop_string(string, length):
    result = [''.join(t) for t in itertools.batched(string, length)]
    return result

# totally unnessary memoization flex
@functools.cache
def get_divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

if __name__ == "__main__":
    for line in tqdm(input.split(',')):
        first, second = line.split('-')
        for id in range(int(first), int(second) + 1):
            str_id = str(id)

            # gather all divisors the string can be chopped up evenly
            divisors = get_divisors(len(str_id))

            # dismiss the last divisor with :-1, it's the length of the whole string
            for divisor in divisors[:-1]:
                # chop up string into equal parts of the length
                chunks = chop_string(str_id, divisor)
                # fast method to check if all elements in the array are the same
                if chunks.count(chunks[0]) == len(chunks):
                    invalid_ids.append(id)
                    break

    # set because the list contained duplicates
    print(sum(set(invalid_ids)))