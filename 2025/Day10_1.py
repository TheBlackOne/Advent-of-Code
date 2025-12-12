input = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

#with open("input.txt") as f:
#   input = f.read()

def int_to_lights(lights_int, num_lights):
    lights = bin(lights_int)[2:].rjust(num_lights, '0')[::-1]
    lights = lights.replace('0', '.')
    lights = lights.replace('1', '#')
    lights = f"[{lights}]"
    return lights

if __name__ == "__main__":
    instructions = []

    for line in input.splitlines():
        elements = line.split()
        lights = elements[0]
        button_presses = elements[1:-1]

        lights = lights[1:-1]
        lights = lights.replace('.', '0')
        lights = lights.replace('#', '1')
        lights_int = int(lights[::-1], 2)
        num_lights = len(lights)

        #test = int_to_lights(lights_int, num_lights)

        buttons_list = []
        for buttons in button_presses:
            buttons = buttons[1:-1].split(',')
            indices = list((int(b) for b in buttons))
            max_index = max(indices)
            buttons_str = ['0'] * (max_index + 1)
            for i in indices:
                buttons_str[i] = '1'
            buttons_int = int(''.join(buttons_str[::-1]), 2)
            buttons_list.append(buttons_int)
        
        instructions.append((lights_int, num_lights, buttons_list))

    total_steps = []
    for target_lights, num_lights, buttons in instructions:
        lights_states = set([0])
        steps = 0
        found = False

        while not found:
            new_lights_states = set()
            steps += 1
            for state in lights_states:
                if found : break

                for button in buttons:
                    new_state = state ^ button
                    if new_state == target_lights:
                        total_steps.append(steps)
                        found = True
                        break
                    else:
                        new_state = state ^ button
                        new_lights_states.add(new_state)
            lights_states = new_lights_states
            
    print(sum(total_steps))