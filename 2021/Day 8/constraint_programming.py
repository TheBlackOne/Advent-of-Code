from constraint import *

number_length = [
    (0, 6),
    (1, 2),
    (2, 5),
    (3, 5),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 3),
    (8, 7),
    (9, 6)
]

segment_frequency = [
    ('b', 6),
    ('c', 8),
    ('e', 4),
    ('f', 9)
]

result = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        first, second = line.split('|')
        first = [''.join(sorted(_)) for _ in first.strip().split()]
        second = [''.join(sorted(_)) for _ in second.strip().split()]

        all_letters = [_ for _ in ''.join(first)]
        unique_segments = list(set(all_letters))

        problem = Problem()

        for number, length in number_length:
            problem.addVariable(str(number), first)
            # each number has the constraint of having a certain number of segments
            problem.addConstraint(lambda display, length=length: len(display) == length, [str(number)])

        for original_segment, frequency in segment_frequency:
            problem.addVariable(original_segment, unique_segments)
            # each segment has the constraint of appearing at a certain frequency across all possible segments
            problem.addConstraint(lambda segment, frequency=frequency: all_letters.count(segment) == frequency, [original_segment])

        # two segments have he frequency 8: 'a' and 'c'
        # the candidate segments have the constraint of being a part of the '1' display,
        # only one remains, which identifies as the 'c' segment, the other one is the 'a' segment
        problem.addConstraint(lambda c, display: c in display, ['c', '1'])

        # with the segments 'b', 'c', 'e' and 'f' known, we can set constraints in wether or not
        # they are part of the displays '2', '3', '5', '6', '9' and '0'
        problem.addConstraint(lambda b, c, e, f, d: b not in d and c in d and e in d and f not in d, ['b', 'c', 'e', 'f', '2'])
        problem.addConstraint(lambda b, c, e, f, d: b not in d and c in d and e not in d and f in d, ['b', 'c', 'e', 'f', '3'])
        problem.addConstraint(lambda b, c, e, f, d: b in d and c not in d and e not in d and f in d, ['b', 'c', 'e', 'f', '5'])
        problem.addConstraint(lambda b, c, e, f, d: b in d and c not in d and e in d and f in d, ['b', 'c', 'e', 'f', '6'])
        problem.addConstraint(lambda b, c, e, f, d: b in d and c in d and e not in d and f in d, ['b', 'c', 'e', 'f', '9'])
        problem.addConstraint(lambda b, c, e, f, d: b in d and c in d and e in d and f in d, ['b', 'c', 'e', 'f', '0'])

        solution = problem.getSolution()
        display_lookup = {v: k for k, v in solution.items()}            

        output_number = ""
        for display in second:            
            number = display_lookup[display]
            output_number += number
        result += int(output_number)

    print(result)