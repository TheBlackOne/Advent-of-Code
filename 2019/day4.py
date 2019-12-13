start = 147981
end = 691423

def are_rising_numbers(i):
    pairs = False

    first = i % 10
    i = i // 10
    
    while i:
        digit = i % 10
        if first < digit: return False
        elif digit == first: pairs = True

        first = digit
        i = i // 10

    return pairs

def has_pairs(i):
    adjadent_digits = 0
    pairs = {}

    first = i % 10
    i = i // 10
    
    while i:
        
        digit = i % 10
        if digit == first: 
            adjadent_digits += 1
            pairs[digit] = adjadent_digits
        else : adjadent_digits = 0

        first = digit
        i = i // 10

    for digit, n in pairs.items():
        if n == 1: return True

    return False

test1 = has_pairs(123444)
test2 = has_pairs(111122)

candidates = []

candidate = 147981
while candidate < end:
    rising = are_rising_numbers(candidate)
    if rising:
        candidates.append(candidate)
        #print("{}: {}".format(candidate, rising))
    candidate += 1

print(len(candidates))

# part 2

candidates_with_pairs = []
for candidate in candidates:
    two_pairs = has_pairs(candidate)
    if two_pairs:
        candidates_with_pairs.append(candidate)
        #print("{}: {}".format(candidate, two_pairs))

print(len(candidates_with_pairs))