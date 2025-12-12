import z3

input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

#with open("input.txt") as f:
#   input = f.read()

if __name__ == "__main__":
    instructions = []

    for line in input.splitlines():
        elements = line.split()
        button_presses = elements[1:-1]
        joltages = elements[-1]
        joltages = joltages[1:-1].split(',')
        joltages = [int(j) for j in joltages]
        
        buttons_list = []
        for buttons in button_presses:
            buttons = buttons[1:-1].split(',')
            buttons = [int(b) for b in buttons]
            buttons_list.append(buttons)
        instructions.append((joltages, buttons_list))

    all_presses = []
    for joltages, buttons in instructions:
        optimizer = z3.Optimize()

        button_variables = []
        for i in range(len(buttons)):
            button_variable = z3.Int(f"button_{i}")
            optimizer.add(button_variable >= 0)
            button_variables.append(button_variable)

        for i, joltage in enumerate(joltages):
            joltage_equation = 0
            for button, variable in zip(buttons, button_variables):
                if i in button:
                    joltage_equation = joltage_equation + variable
            optimizer.add(joltage_equation == joltage)

        presses_variable = z3.Int("presses")
        presses_equation = 0
        for variable in button_variables:
            presses_equation = presses_equation + variable
        optimizer.add(presses_variable == presses_equation)

        optimizer.minimize(presses_variable)
        optimizer.check()
        presses = optimizer.model()[presses_variable].as_long()
        all_presses.append(presses)
    
    print(sum(all_presses))