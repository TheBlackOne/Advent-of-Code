from itertools import product
from collections import defaultdict
from tqdm import tqdm

def get_new_position(position, step):
    global num_fields
    position += step
    return position % num_fields

dice_states = defaultdict(lambda: 0)
for one in range(1, 4):
    for two in range(1, 4):
        for three in range(1, 4):
            dice_states[one + two + three] += 1

wins = defaultdict(lambda: 0)

states = {}

max_points = 21
num_fields = 10
for score1, score2 in product(range(max_points), repeat=2):
    for pos1, pos2 in product(range(num_fields), repeat=2):
        states[(pos1, score1, pos2, score2)] = 0

states[(4 - 1, 0, 2 - 1, 0)] = 1

player = 1
play = True
while play:
    play = False
    states_copy = defaultdict(int)
    for (pos1, score1, pos2, score2), number in states.items():
        if player == 1:
            pos = pos1
            score = score1
        else:
            pos = pos2
            score = score2

        play = True
        for dice, dice_num in dice_states.items():
            new_pos = get_new_position(pos, dice)
            new_score = score + new_pos + 1
            if new_score >= max_points:
                wins[player] += number * dice_num
            else: 
                if player == 1:
                    states_copy[(new_pos, new_score, pos2, score2)] += number * dice_num
                else:
                    states_copy[(pos1, score1, new_pos, new_score)] += number * dice_num

    player = 3 - player

    states = states_copy
print(max(wins.values()))