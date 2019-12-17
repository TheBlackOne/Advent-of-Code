to_compress_string = "L,4,L,6,L,8,L,12,L,8,R,12,L,12,L,8,R,12,L,12,L,4,L,6,L,8,L,12,L,8,R,12,L,12,R,12,L,6,L,6,L,8,L,4,L,6,L,8,L,12,R,12,L,6,L,6,L,8,L,8,R,12,L,12,R,12,L,6,L,6,L,8"
to_compress = to_compress_string.split(',')
to_compress = [e for e in zip(to_compress[::2], to_compress[1::2])]
to_compress = [','.join(e) for e in to_compress]

words = []

i = 0
while True:
    n = 1
    prev_word = ""
    prev_count = 0
    while True:
        elements = to_compress[i:i+n]
        word = ','.join(elements)
        word_count = to_compress_string.count(word, i)
        if n > 2 and word_count < prev_count:
            if prev_word not in words:
                words.append(prev_word)
            i = i + n - 1
            break
        prev_word = word
        prev_count = word_count
        n += 1
    if i + n >= len(to_compress): break

print(words)