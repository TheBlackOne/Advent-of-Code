from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder
import copy
from itertools import combinations, permutations
import os.path

pathfinding_map = []
key_locations = {}
door_locations = {}
start_location = None
path_buffer = {}

class Node:
    def __init__(self, _path, _distance, _key, _keys_to_collect):
        self.path = _path
        self.distance = _distance
        self.key = _key
        self.keys_to_collect = _keys_to_collect

f = open("input_day18.txt", "r")
y = 0
content = f.read()
#content = """#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################"""

for line in content.split('\n'):
    x = 0
    map_line = []
    for c in line:
        if c == "#": map_line.append(0)
        else:
            map_number = 1
            if ord(c) >= 65 and ord(c) <= 90:
                door_locations[c] = (x, y)
            elif ord(c) >= 97 and ord(c) <= 122: key_locations[c] = (x, y)
            elif c == "@":
                start_location = (x, y)
                key_locations["@"] = start_location
            map_line.append(map_number)
        x += 1
    pathfinding_map.append(map_line)
    y += 1
f.close()

total_lenghts = []
#min_total_length = 4189
min_total_length = 999999
key_combo_distances = {}

def fill_distances():
    if os.path.isfile('day18_distances.txt'):
        f = open("day18_distances.txt", "r")
        content = f.read()
        f.close()

        for line in content.split('\n'):
            if line != "":
                key1, key2, door, keys, distance = line.split(',')
                if door == "": door = None
                distance = int(distance)
                key_combo_distances[(key1, key2)] = (door, keys, distance)
                key_combo_distances[(key2, key1)] = (door, keys, distance)        
    else:
        f = open("day18_distances.txt", "w")

        finder = DijkstraFinder()
        key_combos = combinations(key_locations.keys(), 2)

        for key1, key2 in key_combos:
            local_map = copy.deepcopy(pathfinding_map)
            grid = Grid(matrix=local_map)
            key_location1 = key_locations[key1]
            key_location2 = key_locations[key2]
            start = grid.node(key_location1[0], key_location1[1])
            end = grid.node(key_location2[0], key_location2[1])
            path, runs = finder.find_path(start, end, grid)
            path_len = len(path)
            doors_passed = set(door_locations.values()).intersection(path)
            doors_opened = ""
            for door, door_cord in door_locations.items():
                if door_cord in doors_passed:
                    doors_opened += door
            keys_picked_up_str = ""
            keys_picked_up = set(key_locations.values()).intersection(path)
            for key, key_coord in key_locations.items():
                if key_coord in keys_picked_up and key != "@" and key != key1 and key != key2:
                    keys_picked_up_str += key
            
            print("found: {} to {} with doors {} opened and keys picked up: {}".format(key1, key2, doors_opened, keys_picked_up_str))
            f.write(','.join([key1, key2, doors_opened, keys_picked_up_str, str(path_len)]))
            f.write('\n')
        f.close()

def get_path_len(key_just_found, _key_locations, _length_so_far):
    global min_total_length
    
    #if not key_just_found is None:
    del _key_locations[key_just_found]

    if len(_key_locations) == 0:
        if _length_so_far < min_total_length:
            min_total_length = _length_so_far
        print("all keys found! total length: {}".format(_length_so_far))
        return

    for key in _key_locations.keys():
        if key_just_found == "":
            print(key)

        door_blocking, path_length = key_combo_distances[(key_just_found, key)]
        if not door_blocking is None:
            door_blocking = door_blocking.lower()
            if key == door_blocking or door_blocking in _key_locations.keys():
                continue

        path_length -= 1
        if path_length + _length_so_far < min_total_length:
            new_key_locations = copy.deepcopy(_key_locations)
            get_path_len(key, new_key_locations, path_length + _length_so_far)

def bfs2(_nodes, _step):
    global min_total_length
    for node in _nodes:
        if len(node.path) >= 26:
            if node.distance < min_total_length:
                min_total_length = node.distance
                print("\tminimum distance found: {} path: {}".format(node.distance, node.path + node.key))
    nodes = []
    skipped_distance = 0
    skipped_doors = 0
    for node in _nodes:
        for key in node.keys_to_collect:
            if node.key != key:
                distance_key = (node.key, key)
                doors, keys_picked_up, distance = key_combo_distances[distance_key]

                new_path = node.path
                keys_to_collect = node.keys_to_collect
                for c in keys_picked_up:
                    if c not in new_path: new_path += c
                    keys_to_collect = keys_to_collect.replace(c, '')
                if node.key not in new_path: new_path += node.key
                keys_to_collect = keys_to_collect.replace(node.key, '')

                new_distance = node.distance + distance - 1
                add_node = True
                if not doors is None:
                    for door in doors:
                        if not door.lower() in new_path:
                            add_node = False
                            skipped_doors += 1
                            break
                if add_node:
                    new_node = Node(new_path, new_distance, key, keys_to_collect)
                    nodes.append(new_node)

    if len(nodes) > 0:
        before = len(nodes)
        nodes = [node for node in nodes if node.distance < min_total_length]
        skipped_distance = before - len(nodes)
        nodes = sorted(nodes, key=lambda node: node.distance, reverse=False)
        chunks = [nodes[x:x + 100000] for x in range(0, len(nodes), 100000)]

        for chunk in chunks:
            for i in range(_step):
                print(' ', end="")
            print("step: {}, nodes: {}/{}, skipped di.: {} skipped do.: {} min: {}".format(_step, len(chunk), len(nodes), skipped_distance, skipped_doors, min_total_length))
            bfs2(chunk, _step + 1)

def bfs(_key, _distance, _path, _step):
    global min_total_length
    if _step >= 27:
        if _distance < min_total_length:
            min_total_length = _distance
            print("\tnew min distance: {}".format(_distance))
        return

    keys_collected = []
    path = _path
    for key in key_locations.keys():
        if _key != key and key not in path:
            distance_key = (_key, key)
            door, distance = key_combo_distances[distance_key]
            if door is None or door.lower() in path:
                keys_collected.append((key, _distance + distance - 1))
                path = path + key

    keys_collected = sorted(keys_collected, key=lambda k: k[1])
    for key, distance in keys_collected:
        if _key == "":
            print(key)
        if distance < min_total_length:
            bfs(key, distance, _path + key, _step + 1)



fill_distances()
#get_path_len("", key_locations, 0)
keys_to_collect = ''.join(key_locations.keys()).replace('@', '')
start_node = Node("", 0, "@", keys_to_collect)
#bfs("", 0, "", 1)
bfs2([start_node], 0)

print(min_total_length)