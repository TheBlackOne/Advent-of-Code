input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

#with open("input.txt") as f:
#   input = f.read()

invalid_ids = []

if __name__ == "__main__":
    for line in input.split(','):
        first, second = line.split('-')
        for id in range(int(first), int(second) + 1):
            if len(str(id)) % 2 == 0:
                firstpart, secondpart = str(id)[:len(str(id))//2], str(id)[len(str(id))//2:]
                if firstpart == secondpart:
                    invalid_ids.append(id)
    print(sum(invalid_ids))