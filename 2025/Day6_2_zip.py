import math

input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

#with open("input.txt") as f:
#   input = f.read()


if __name__ == "__main__":
    answer = 0
    operator = None
    operands = []

    lines = [l[::-1] for l in input.splitlines()]
    for col in zip(*lines):
        number_characters = col[:-1]
        number = ''.join(number_characters).strip()
        if number != '':
            operands.append(number)
        
        operator = col[-1]
        if operator != ' ':
            expression = operator.join(operands)
            answer += eval(expression)
            operands.clear()
    
    print(answer)