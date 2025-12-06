import numpy as np

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

#with open("input.txt") as f:
#   input = f.read()

array = []
answer = 0

if __name__ == "__main__":
    for line in input.splitlines():
        elements = line.split()
        array.append(elements)

    array = np.array(array)
    array = np.transpose(array)

    for line in array:
        elements = [int(e) for e in line[:-1]]
        operator = line[-1]
        if operator == '*':
            answer += np.prod(elements)
        else:
            answer += np.sum(elements)

    
    print(answer)