import numpy as np

segment_frequency_lookup = {
    6: 'b',
    4: 'e',
    9: 'f'
}

display_length_lookup = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

output_numbers = []

with open('input.txt', 'r') as file:
    for line in file.readlines():
        display_lookup = {}
        segment_lookup = {}
        first, second = line.split('|')
        first = [''.join(sorted(_)) for _ in first.strip().split()]
        second = [''.join(sorted(_)) for _ in second.strip().split()]

        for display in first:
            length_candidate = display_length_lookup.get(len(display))
            if length_candidate != None:
                display_lookup[display] = length_candidate
                display_lookup[length_candidate] = display
        one = display_lookup[1]

        all_letters = [_ for _ in ''.join(first)]
        segments, counts = np.unique(np.asarray(all_letters), return_counts=True)
        for segment, count in zip(segments, counts):
            key = segment_frequency_lookup.get(count)
            if key != None:
                segment_lookup[key] = segment
            elif count == 8 and segment in one: segment_lookup['c'] = segment

        
        b = segment_lookup['b']
        c = segment_lookup['c']
        e = segment_lookup['e']
        f = segment_lookup['f']
        for display in first:
            if display in display_lookup.keys(): continue
            # 2, 3, 5
            if len(display) == 5:
                if b not in display and c in display and e in display and f not in display:
                    display_lookup[display] = 2
                elif b not in display and c in display and e not in display and f in display:
                    display_lookup[display] = 3
                else: display_lookup[display] = 5

            # 0, 6, 9
            elif len(display) == 6:
                if b in display and c not in display and e in display and f in display:
                    display_lookup[display] = 6
                elif b in display and c in display and e not in display and f in display:
                    display_lookup[display] = 9
                else:
                    display_lookup[display] = 0

        output_number = ""
        for display in second:
            number = display_lookup[display]
            output_number += str(number)
        output_numbers.append(int(output_number))

    print(sum(output_numbers))