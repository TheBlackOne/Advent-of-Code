input = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

with open("input.txt") as f:
    input = f.read()


if __name__ == "__main__":
    logic_map = {}

    logic = input.split("\n\n")[1]
    for line in logic.splitlines():
        formula, variable = line.split(" -> ")
        logic_map[variable] = formula

    last_z = sorted([z for z in logic_map.keys() if z.startswith("z")], reverse=True)[0]

    # Rules from: https://www.reddit.com/r/adventofcode/comments/1hla5ql/comment/m3lh9un/
    #
    # Rule 1: XOR only outputs a bit if it doesn't take an input bit
    # Rule 2: XOR only takes an input bit if a XOR follows it, unless the input bits are the first bits
    # Rule 3: OR either outputs into z45 or is followed by an AND and a XOR
    # Rule 4: ANDs are only followed by ORs, unless the input bits are the first bits

    problem_candidates = set()
    for target_wire, formula in logic_map.items():
        wire1, operation, wire2 = formula.split()
        takes_x_or_y = wire1[0] in ("x", "y") or wire2[0] in ("x", "y")
        takes_x00_or_y00 = wire1 in ("x00", "y00") or wire2 in ("x00", "y00")
        writes_to_z = target_wire.startswith("z")
        writes_to_last_z = target_wire == last_z

        following_operations = set()
        for other_formula in logic_map.values():
            if target_wire in other_formula:
                following_operation = other_formula.split()[1]
                following_operations.add(following_operation)

        and_follows = "AND" in following_operations
        or_follows = "OR" in following_operations
        xor_follows = "XOR" in following_operations

        problem_found = True
        if operation == "XOR":
            # Rule 1
            if writes_to_z and not takes_x_or_y:
                problem_found = False
            # Rule 2
            elif (takes_x_or_y and xor_follows) or takes_x00_or_y00:
                problem_found = False
        elif operation == "OR":
            # Rule 3
            if writes_to_last_z or (and_follows and xor_follows):
                problem_found = False
        elif operation == "AND":
            # Rule 4
            if (or_follows and not and_follows and not xor_follows) or takes_x00_or_y00:
                problem_found = False

        if problem_found:
            problem_candidates.add(target_wire)

    problem_candidates = sorted(problem_candidates)
    print(",".join(problem_candidates))
