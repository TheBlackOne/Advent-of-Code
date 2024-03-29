import numpy as np

base_pattern = [0, 1, 0, -1]

def pattern_generator(stage):
    i = 0
    while True:
        for r in range(0, stage):
            yield base_pattern[i % 4]
        i += 1

input = "59750530221324194853012320069589312027523989854830232144164799228029162830477472078089790749906142587998642764059439173975199276254972017316624772614925079238407309384923979338502430726930592959991878698412537971672558832588540600963437409230550897544434635267172603132396722812334366528344715912756154006039512272491073906389218927420387151599044435060075148142946789007756800733869891008058075303490106699737554949348715600795187032293436328810969288892220127730287766004467730818489269295982526297430971411865028098708555709525646237713045259603175397623654950719275982134690893685598734136409536436003548128411943963263336042840301380655801969822"
#input = "80871224585914546619083218645595"
input = np.array([int(x) for x in input])
length = len(input)

stage_matrix = []
for stage in range(1, length + 1):
    pattern_gen = pattern_generator(stage)
    skip = True
    multiplicators = []
    for c in range(1, length + 1):
        multiplicator = next(pattern_gen)
        if skip:
            multiplicator = next(pattern_gen)
            skip = False
        multiplicators.append(multiplicator)
    stage_matrix.append(multiplicators)
stage_matrix = np.array(stage_matrix)

for n in range(0, 100):
    temp_input = []
    for stage_array in stage_matrix:
        result = np.multiply(input, stage_array)
        temp_input.append(abs(np.sum(result)) % 10)
    input = np.array(temp_input)

# part 1
print(''.join([str(c) for c in input[0:8]]))