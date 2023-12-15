input = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

# with open("input.txt") as f:
#    input = f.read()


def hash(input):
    current = 0
    for c in input:
        current += ord(c)
        current *= 17
        current = current % 256
    return current


if __name__ == "__main__":
    result = 0
    for step in input.split(","):
        result += hash(step)

    print(result)
