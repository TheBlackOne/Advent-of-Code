input = """2333133121414131402"""

# with open("input.txt") as f:
#    input = f.read()


if __name__ == "__main__":
    input = list(map(int, list(input)))
    filemap_size = sum(input)
    file_map = ["."] * filemap_size
    file_id = 0
    index = 0
    is_file = True

    for num in input:
        if is_file:
            for i in range(index, index + num):
                file_map[i] = file_id
            file_id += 1

        index += num
        is_file = not is_file

    # print("".join(map(str, file_map)))

    i = len(file_map) - 1
    for file_id in file_map[::-1]:
        if file_id != ".":
            first_free_index = file_map.index(".")
            if first_free_index < i:
                file_map[first_free_index], file_map[i] = (
                    file_map[i],
                    file_map[first_free_index],
                )
            else:
                break
        i -= 1

        # print("".join(map(str, file_map)))

    sum = sum(i * id for i, id in enumerate(file_map) if id != ".")
    print(sum)
