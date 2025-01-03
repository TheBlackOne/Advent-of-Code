from functools import cache

input = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

# with open("input.txt") as f:
#    input = f.read()


@cache
def match_design(design, index):
    global available_patterns

    if index == len(design):
        return True

    for pattern in available_patterns:
        if design[index:].startswith(pattern):
            new_index = index + len(pattern)
            found = match_design(design, new_index)
            if found:
                return True

    return False


if __name__ == "__main__":
    available_patterns = []
    desired_designs = []

    first, second = input.split("\n\n")
    available_patterns = first.split(", ")
    desired_designs = second.splitlines()

    num_matched = 0
    for design in desired_designs:
        found = match_design(design, 0)
        if found:
            num_matched += 1

    print(num_matched)
