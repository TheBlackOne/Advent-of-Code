from binarytree import Node, get_parent, tree
import math
import copy
from tqdm import tqdm
from itertools import permutations

def add(left, right):
    return Node(-1, copy.deepcopy(left), copy.deepcopy(right))

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

def calc_magnitude(root):
    while len(root.levels) > 1:
        for node in root.levels[-2]:
            if node.value == -1:
                node.value = (node.left.value) * 3 + (node.right.value * 2)
                node.left = None
                node.right = None
    return root.value

def find_next_left(root, node):
    index = list(reversed(root.postorder)).index(node)
    for next_left in list(reversed(root.postorder))[index + 1:]:
        if next_left.value > -1:
            return next_left    
    return None

def find_next_right(root, node):
    index = root.preorder.index(node)
    for next_right in root.preorder[index + 1:]:
        if next_right.value > -1:
            return next_right
    
    return None

def reduce_tree(root):
    reduce = True
    while reduce:
        if len(root.levels) > 5:
            did_explode = False
            for node in root.levels[-2]:
                if node.left != None:
                    left = node.left
                    next_left = find_next_left(root, left)
                    if next_left != None:
                        next_left.value += left.value
                    
                    node.left = None
                    did_explode = True
                    node.value = 0
                
                if node.right != None:
                    right = node.right
                    next_right = find_next_right(root, right)
                    if next_right != None:
                        next_right.value += right.value
                    
                    node.right = None
                    did_explode = True
                    node.value = 0

                if did_explode: break
            if did_explode: continue

        did_split = False
        for node in root.preorder:
            if node.value > 9:
                node.left = Node(int(math.floor(node.value / 2)))
                node.right = Node(int(math.ceil(node.value / 2)))
                node.value = -1
                did_split = True

            if did_split: break
        if did_split: continue

        reduce = False
    return root

with open('input.txt', 'r') as file:
    trees = [parse_number(line.strip()) for line in file.readlines()]

magnitudes = []
for left, right in tqdm(list(permutations(trees, 2))):
    sum = calc_magnitude(reduce_tree(add(left, right)))
    magnitudes.append(sum)

print(max(magnitudes))