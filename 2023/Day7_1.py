input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# with open('input.txt') as f:
#    input = f.read()

labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

hands = []


def determine_type(cards):
    cards = ''.join(sorted(cards, reverse=True,))
    groups = []
    group_size = 1
    current_card = cards[0]
    for card in cards[1::]:
        if card == current_card:
            group_size += 1
        else:
            groups.append(group_size)
            group_size = 1
        current_card = card
    groups.append(group_size)

    num_groups = len(groups)
    biggest_group = max(groups)
    if num_groups == 1:
        return 1
    elif num_groups == 2:
        if biggest_group == 4:
            return 2
        else:
            return 3
    elif num_groups == 3:
        if biggest_group == 3:
            return 4
        else:
            return 5
    elif num_groups == 4:
        return 6
    else:
        return 7

    print()


if __name__ == "__main__":
    for line in input.splitlines():
        cards, bid = line.split()
        hand_type = determine_type(cards)
        hands.append((cards, bid, hand_type))

    hands = sorted(hands,
                   reverse=True,
                   key=lambda x: (x[2], labels.index(x[0][0]), labels.index(x[0][1]), labels.index(x[0][2]), labels.index(x[0][3]), labels.index(x[0][4])))

    winnings = 0
    for rank, hand in enumerate(hands):
        winnings += int(hand[1]) * (rank + 1)
        print(f"Hand: {hand} rank: {rank + 1} bid: {hand[1]}")

    print(f"Winnings: {winnings}")
