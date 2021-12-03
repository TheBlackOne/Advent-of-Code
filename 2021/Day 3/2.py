import numpy

input = []
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file.readlines()]

input_array = []

for line in input:
    row = [int(number) for number in line]
    input_array.append(row)

def get_rating(input, max = True):

    result = ""

    numbers_to_keep = numpy.array(input)

    col_idx = 0
    while len(numbers_to_keep) > 1:
        col = numbers_to_keep.T[col_idx]
        oxygen_num_zeroes_ones = numpy.bincount(col)

        interesting_bit = int(max)
        search_for = oxygen_num_zeroes_ones.min()
        if max: search_for = oxygen_num_zeroes_ones.max()

        if oxygen_num_zeroes_ones.min() != oxygen_num_zeroes_ones.max():
            interesting_bit = numpy.where(oxygen_num_zeroes_ones==search_for)[0][0]

        idx_to_keep = numpy.where(col==interesting_bit)[0]
        numbers_to_keep = numpy.array([numbers_to_keep[idx] for idx in idx_to_keep])
        
        #for number in numbers_to_keep: print(number)
        #print("=================")

        col_idx += 1

    result = ''.join([str(_) for _ in numbers_to_keep[0]])
    return result

oxxygen_rating = int(get_rating(input_array), 2)
co2_rating = int(get_rating(input_array, False), 2)

print(str(oxxygen_rating * co2_rating))