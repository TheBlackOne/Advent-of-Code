import numpy

numbers_to_draw = []
boards = []

with open('input.txt', 'r') as file:
    input = file.read().split('\n\n')

    numbers_to_draw = [int(_) for _ in input[0].split(',')]

    for board in input[1:]:
        new_board = [[int(number) for number in row.split()] for row in board.split('\n')]
        boards.append(new_board)

# array needs to be of type float in order to use numpy.nan later
boards = numpy.array(boards).astype('float')

score = None

for number in numbers_to_draw:
    coords = numpy.where(boards == number)
    for board_idx, row_idx, col_idx in zip(*coords):

        # numpy.nan is used to mark a cell
        boards[board_idx][row_idx][col_idx] = numpy.nan

        if numpy.isnan(boards[board_idx][row_idx]).all() or numpy.isnan(boards[board_idx].T[col_idx]).all():
            # the nansum() variant counts numpy.nan values as 0, thus skipping marked cells
            score = numpy.nansum(boards[board_idx]) * number
            break

    if score is not None: break

print("Score is: {}".format(int(score)))