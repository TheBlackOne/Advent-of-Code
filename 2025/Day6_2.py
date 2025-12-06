import numpy as np

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

#with open("input.txt") as f:
#   input = f.read()

answer = 0

if __name__ == "__main__":
    # create 2d array of single chars from the input    
    numbers = np.array([np.array(list(line)) for line in input.splitlines()])

    # the positions of * and + indicate where to split the cols
    # the last row in numbers contains all the operators
    col_split_indices = [i for i, c in enumerate(numbers[-1]) if c != ' ']

    # split the 2d array by the list of col indices
    # do not use the first element (it is 0)
    numbers = np.hsplit(numbers, col_split_indices[1:])

    # swap rows and cols of the inner arrays
    numbers = [np.transpose(n) for n in numbers]

    for line in numbers:
        # create string from single character in inner array
        # do not use the last element in the array (it is the delimiter whitespace or operator)
        # strip away leading and trailing whitespaces
        operands = [''.join(n[:-1]).strip() for n in line]
        # transform number strings to integers, except when the string is empty
        operands = np.array([int(o) for o in operands if o != ''])

        # the operator is always at the first element of lines, at the last position
        operator = line[0][-1]
        if operator == '*':
            answer += np.prod(operands)
        else:
            answer += np.sum(operands)
    
    print(answer)