input = """2333133121414131402"""

# with open("input.txt") as f:
#    input = f.read()


def get_flat_file_map(file_map):
    result = []

    for file in file_map:
        file_id, file_size = file
        if file_id is None:
            file_id = "."
        for n in range(file_size):
            result.append(file_id)

    return result


def print_file_map(file_map):
    print("".join(map(str, get_flat_file_map(file_map))))


def get_destination_index_free_size(file_id, file_size, max_index):
    global file_map
    result = (None, None)

    for i, entry in enumerate(file_map):
        if i > max_index:
            break
        free_file_id, free_size = entry
        if free_file_id is None:
            if free_size >= file_size:
                result = (i, free_size)
                break

    return result


if __name__ == "__main__":
    input = list(map(int, list(input)))
    is_file = True
    index = 0
    file_map = []

    for file_size in input:
        file_id = None
        if is_file:
            file_id = index
            index += 1

        file_map.append((file_id, file_size))
        is_file = not is_file

    # print("".join(map(str, file_map)))

    i = len(file_map) - 1

    while i >= 0:
        file_id, file_size = file_map[i]
        if file_id is not None:
            dest_index, dest_free_size = get_destination_index_free_size(
                file_id, file_size, i
            )
            if dest_index is not None:
                # print_file_map(file_map)
                new_entry = (file_id, file_size)
                file_map[dest_index] = new_entry

                new_free_entry = (None, file_size)
                file_map[i] = new_free_entry

                new_free_size = dest_free_size - file_size
                if new_free_size > 0:
                    new_free_entry = (None, new_free_size)
                    file_map.insert(dest_index + 1, new_free_entry)
                    i += 1
        i -= 1

    # print_file_map(file_map)

    flat_file_map = get_flat_file_map(file_map)
    sum = sum(i * id for i, id in enumerate(flat_file_map) if id != ".")
    print(sum)
