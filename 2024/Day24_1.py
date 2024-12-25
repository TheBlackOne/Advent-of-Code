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

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    value_map = {}
    logic_map = {}

    values, logic = input.split("\n\n")
    for line in values.splitlines():
        variable, value = line.split(": ")
        value_map[variable] = str(bool(int(value)))

    for line in logic.splitlines():
        formula, variable = line.split(" -> ")
        formula = formula.replace("XOR", "^")
        formula = formula.lower()
        logic_map[variable] = f"{formula}"

    for variable, value in value_map.items():
        for old_variable, formula in logic_map.items():
            logic_map[old_variable] = formula.replace(variable, value)

    gates_processed = []

    processed = True
    while processed:
        processed = False
        for target_gate in logic_map.keys():
            if target_gate not in gates_processed:
                formula = logic_map[target_gate]
                wire1, operator, wire2 = formula.split()
                if wire1 in ("True", "False") and wire2 in ("True", "False"):
                    gate_result = str(eval(formula))
                    processed = True
                    gates_processed.append(target_gate)
                    logic_map[target_gate] = gate_result

                    if target_gate[0] != "z":
                        for wire, formula in logic_map.items():
                            logic_map[wire] = formula.replace(target_gate, gate_result)

    z_list = sorted([k for k in logic_map.keys() if k.startswith("z")])[::-1]
    z_results = [str(int(eval(logic_map[z]))) for z in z_list]
    result = int("".join(z_results), 2)
    print(result)
