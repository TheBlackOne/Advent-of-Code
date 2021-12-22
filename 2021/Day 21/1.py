dice  = 0
num_dice_rolls = 0
score1 = 0
score2 = 0

position1 = 4
position2 = 2

position1 -= 1
position2 -= 1

def roll_dice():
    global dice
    global num_dice_rolls

    dice += 1
    if dice > 100: dice -= 100

    num_dice_rolls += 1
    return dice

def get_new_position(position, step):
    position += step
    return position % 10

#with open('input.txt', 'r') as file:

while True:
    step1 = roll_dice()
    step1 += roll_dice()
    step1 += roll_dice()
    position1 = get_new_position(position1, step1)
    score1 += position1 + 1

    if score1 >= 1000:
        break

    step2 = roll_dice()
    step2 += roll_dice()
    step2 += roll_dice()
    position2 = get_new_position(position2, step2)
    score2 += position2 + 1

    if score2 >= 1000:
        break

result = min((score1, score2)) * num_dice_rolls

print(result)