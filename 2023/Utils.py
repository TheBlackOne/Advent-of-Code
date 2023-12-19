# Multiplies all numbers in the list
def prod(numbers):
    result = 1
    for n in numbers:
        result *= int(n)
    return result
