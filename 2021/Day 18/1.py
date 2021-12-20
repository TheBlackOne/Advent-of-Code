from binarytree import Node, get_parent
import math

def parse_number(number):
    root = Node(-1)
    current = root

    for char in number:
        if char == '[':
            current.left = Node(-1)
            current = current.left
        elif char == ']':
            current = get_parent(root, current)
        elif char == ',':
            current = get_parent(root, current)
            current.right = Node(-1)
            current = current.right
        else:
            current.value = int(char)

    return root


numbers = []

with open('input.txt', 'r') as file:
    numbers = [_.strip() for _ in file.readlines()]

root = parse_number(numbers[0])

for number in numbers[1:]:
    root = Node(-1, left=root)
    root.right = parse_number(number)

    reduce = True
    while reduce:
        if len(root.levels) > 5:
            did_explode = False
            for node in root.levels[-2]:
                if not did_explode:
                    if node.left != None:
                        left = node.left
                        index = list(reversed(root.postorder)).index(left)
                        for next_left in list(reversed(root.postorder))[index + 1:]:
                            if next_left.value > -1:
                                next_left.value += left.value
                                break
                        node.left = None
                        did_explode = True
                        node.value = 0
                    
                    if node.right != None:
                        right = node.right
                        index = root.preorder.index(right)
                        for next_right in root.preorder[index + 1:]:
                            if next_right.value > -1:
                                next_right.value += right.value
                                break
                        node.right = None
                        did_explode = True
                        node.value = 0

                if did_explode:
                    #print(root)
                    break
            if did_explode: continue

        did_split = False
        for node in root.preorder:
            if node.value > 9:
                node.left = Node(int(math.floor(node.value / 2)))
                node.right = Node(int(math.ceil(node.value / 2)))
                node.value = -1
                did_split = True

            if did_split:
                #print(root)
                break
        if did_split: continue

        reduce = False

while len(root.levels) > 1:
    for node in root.levels[-2]:
        if node.value == -1:
            #print(node)
            node.value = (node.left.value) * 3 + (node.right.value * 2)
            node.left = None
            node.right = None
            

print(root)