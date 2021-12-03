import numpy

input = []
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file.readlines()]

input_array = []

for line in input:
    row = [int(number) for number in line]
    input_array.append(row)

gamma_rate = ""
epsilon_rate = ""

input_array = numpy.array(input_array)
for column in input_array.T:
    num_zeroes_ones = numpy.bincount(column)

    index_max = numpy.where(num_zeroes_ones==num_zeroes_ones.max())[0][0]
    gamma_rate += str(index_max)

    index_min = numpy.where(num_zeroes_ones==num_zeroes_ones.min())[0][0]
    epsilon_rate += str(index_min)
    print()

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

result = gamma_rate * epsilon_rate

print(result)