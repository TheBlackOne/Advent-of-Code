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

    sum = 0

    for number in left:
        sum += number * right.count(number)

    print(sum)
