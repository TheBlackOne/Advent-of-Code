import numpy

def calc_score(winning_board, winning_marked_board, winning_number):
    result = 0
    score_matrix = numpy.multiply(winning_board, numpy.invert(winning_marked_board))
    result = numpy.sum(score_matrix) * winning_number
    return result

numbers_to_draw = []
boards = []
marked_boards = []

input = []
with open('input.txt', 'r') as file:
    new_board = []
    new_marked_board = []

    for line in [_.strip() for _ in file.readlines()]:
        if ',' in line:
            numbers_to_draw = [int(_) for _ in line.split(',')]
        elif len(line) == 0:
            if len(new_board) > 0:
                boards.append(new_board)
                marked_boards.append(new_marked_board)
                new_board = []
                new_marked_board = []
        else:
            new_board.append([int(_) for _ in line.split()])
            new_marked_board.append([False for _ in range(0, len(new_board[-1]))])
        
    boards.append(new_board)
    marked_boards.append(new_marked_board)

boards = numpy.array(boards)
marked_boards = numpy.array(marked_boards)

score = 0
for number in numbers_to_draw:
    coords = numpy.where(boards == number)
    for board_idx, row_idx, col_idx in zip(*coords):
        marked_boards[board_idx][row_idx][col_idx] = True

        if all(marked_boards[board_idx][row_idx]) or all(marked_boards[board_idx].T[col_idx]):
            score = calc_score(boards[board_idx], marked_boards[board_idx], number)
            break

    if score > 0: break

print("Score is: {}".format(score))