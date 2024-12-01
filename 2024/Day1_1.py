import itertools

input = """3   4
4   3
2   5
1   3
3   9
3   3"""

# with open('input.txt') as f:
#    input = f.read()

if __name__ == "__main__":
    left = []
    right = []
    for line in input.split("\n"):
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    sum = 0

    for l, r in zip(left, right):
        sum += abs(l - r)

    print(sum)
