input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

# with open('input.txt') as f:
#   input = f.read()


def process_card(card_list, card_index, card_counter):
    card_counter += 1
    card_line = card_list[card_index]

    header, numbers = card_line.split(': ')
    # print(f"Processing card {header}")

    winning_numbers_string, your_numbers_string = numbers.split(' | ')
    winning_numbers = set(filter(None, winning_numbers_string.split(' ')))
    your_numbers = set(filter(None, your_numbers_string.split(' ')))

    winners = list(winning_numbers & your_numbers)
    new_card_indizes = list(
        range(card_index + 1, card_index + len(winners) + 1))
    for new_card_index in new_card_indizes:
        card_counter = process_card(card_list, new_card_index, card_counter)

    return card_counter


if __name__ == "__main__":
    card_counter = 0
    card_list = input.splitlines()
    for card_index in range(0, len(card_list)):
        card_counter = process_card(card_list, card_index, card_counter)

    print(f"Result: {card_counter}")
