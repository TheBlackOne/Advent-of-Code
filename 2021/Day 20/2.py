from tqdm import tqdm

enhancement_algo = []
input_picture = []
padding = 1
filling = 0

def print_picture(picture):
    for row in picture:
        line = ""
        for pixel in row:
            if pixel == 0: line += "."
            else: line += "#"
        print(line)

def create_empty(width, height):
    return [[filling for _ in range(width)] for _ in range(height)]

def pad_picture(picture):
    width = len(picture[0])

    for i in range(len(picture)):
        line = picture[i]
        for _ in range(padding):
            line.insert(0, filling)
            line.append(filling)
        picture[i] = line

    padding_line = [filling for _ in range(width + padding * 2)]
    for _ in range(padding):
        picture.insert(0, padding_line)
        picture.append(padding_line)
      
    return picture

def get_enhanced_pixel(index):
    return enhancement_algo[index]

def get_index(submatrix):
    pixel_string = ""
    for line in submatrix:
        for pixel in line:
            pixel_string += str(pixel)
    return int(pixel_string, 2)

def get_submatrix(picture, row, col):
    submatrix = []
    for y in range(row - 1, row + 2):
        line = []
        for x in range(col - 1, col + 2):
            pixel = None
            if y < 0 or y >= len(picture): pixel = filling
            elif x < 0 or x >= len(picture[0]): pixel = filling
            else: pixel = picture[y][x]
            line.append(pixel)
        submatrix.append(line)
    return submatrix

def get_new_filling(filling):
    submatrix = [[ filling for x in range(3)] for y in range(3)]
    index = get_index(submatrix)
    return get_enhanced_pixel(index)

with open('input.txt', 'r') as file:
    enhancement, picture = file.read().split('\n\n')
    for pixel in enhancement:
        if pixel == '#': enhancement_algo.append(1)
        else: enhancement_algo.append(0)

    for line in picture.split():
        picture_line = []
        for pixel in line:
            if pixel == '#': picture_line.append(1)
            else: picture_line.append(0)
        input_picture.append(picture_line)

for _ in tqdm(range(50)):
    input_picture = pad_picture(input_picture)
    width = len(input_picture[0])
    height = len(input_picture)
    output_picture = create_empty(width, height)
    for col in range(0, width):
        for row in range(0, height):
            submatrix = get_submatrix(input_picture, row, col)
            index = get_index(submatrix)
            enhanced_pixel = get_enhanced_pixel(index)
            output_picture[row][col] = enhanced_pixel
    input_picture = output_picture
    filling = get_new_filling(filling)

count = sum([i.count(1) for i in input_picture])
print(count)