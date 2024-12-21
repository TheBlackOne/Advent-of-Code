import timeit
from collections import defaultdict

import networkx as nx

input = """029A
980A
179A
456A
379A"""

# with open("input.txt") as f:
#    input = f.read()

edge_up = {"direction": "^"}
edge_down = {"direction": "v"}
edge_left = {"direction": "<"}
edge_right = {"direction": ">"}


def calc_path_score(path):
    score = 0
    for first, second in zip(path[:-1], path[1:]):
        if first != second:
            score += 1
    return score


def filter_lowest_path_score(paths):
    path_scores = []
    for path in paths:
        score = calc_path_score(path)
        path_scores.append((path, score))

    min_score = min(s for _, s in path_scores)
    return [p for p, s in path_scores if s == min_score]


def build_directions_map(graph):
    paths = dict(nx.all_pairs_all_shortest_paths(graph))
    directions_map = defaultdict(lambda: [])
    for start, start_paths in paths.items():
        for end, paths in start_paths.items():
            for path in paths:
                directions = []
                for n1, n2 in zip(path[:-1], path[1:]):
                    direction = graph.edges()[(n1, n2)]["direction"]
                    directions.append(direction)
                directions_map[(start, end)].append("".join(directions))

    for key, possible_paths in directions_map.items():
        directions_map[key] = filter_lowest_path_score(possible_paths)

    return directions_map


def get_shortest_paths(start, end, direction_map):
    paths = direction_map[(start, end)]
    return paths


def get_sequences(code, direction_map):
    sequences = [""]
    start = "A"
    for end in list(code):
        new_sequences = []
        paths = get_shortest_paths(start, end, direction_map)
        for path in paths:
            for sequence in sequences:
                new_sequences.append(sequence + path + "A")
        sequences = new_sequences
        start = end

    return sequences


if __name__ == "__main__":
    numerical_edges = [
        ("0", "2", edge_up),
        ("0", "A", edge_right),
        ("A", "3", edge_up),
        ("A", "0", edge_left),
        ("1", "4", edge_up),
        ("1", "2", edge_right),
        ("2", "5", edge_up),
        ("2", "3", edge_right),
        ("2", "0", edge_down),
        ("2", "1", edge_left),
        ("3", "6", edge_up),
        ("3", "A", edge_down),
        ("3", "2", edge_left),
        ("4", "7", edge_up),
        ("4", "5", edge_right),
        ("4", "1", edge_down),
        ("5", "8", edge_up),
        ("5", "6", edge_right),
        ("5", "2", edge_down),
        ("5", "4", edge_left),
        ("6", "9", edge_up),
        ("6", "3", edge_down),
        ("6", "5", edge_left),
        ("7", "8", edge_right),
        ("7", "4", edge_down),
        ("8", "9", edge_right),
        ("8", "5", edge_down),
        ("8", "7", edge_left),
        ("9", "6", edge_down),
        ("9", "8", edge_left),
    ]
    num_G = nx.DiGraph()
    num_G.add_edges_from(numerical_edges)

    dir_edges = [
        ("<", "v", edge_right),
        ("v", "^", edge_up),
        ("v", ">", edge_right),
        ("v", "<", edge_left),
        (">", "A", edge_up),
        (">", "v", edge_left),
        ("^", "A", edge_right),
        ("^", "v", edge_down),
        ("A", ">", edge_down),
        ("A", "^", edge_left),
    ]
    dir_G = nx.DiGraph()
    dir_G.add_edges_from(dir_edges)

    numerical_directions_map = build_directions_map(num_G)
    directional_directions_map = {
        ("<", "<"): "",
        ("<", "v"): ">",
        ("<", "^"): ">^",
        ("<", ">"): ">>",
        ("<", "A"): ">>^",
        ("v", "<"): "<",
        ("v", "v"): "",
        ("v", "^"): "^",
        ("v", ">"): ">",
        ("v", "A"): "^>",
        ("^", "<"): "v<",
        ("^", "v"): "v",
        ("^", "^"): "",
        ("^", ">"): "v>",
        ("^", "A"): ">",
        (">", "<"): "<<",
        (">", "v"): "<",
        (">", "^"): "<^",
        (">", ">"): "",
        (">", "A"): "^",
        ("A", "<"): "v<<",
        ("A", "v"): "<v",
        ("A", "^"): "<",
        ("A", ">"): "v",
        ("A", "A"): "",
    }

    start = timeit.default_timer()
    code_complexities = []
    for code in input.splitlines():
        num_directional_keypads = 2
        sequences = get_sequences(code, numerical_directions_map)

        lengths = []
        for sequence in sequences:
            test = {sequence: (None, 1)}

            test_length = None
            for _ in range(num_directional_keypads):
                new_test = {}
                for key, value in test.items():
                    length, num = value
                    key = "A" + key
                    for c1, c2 in zip(key[:-1], key[1:]):
                        bla = directional_directions_map[(c1, c2)] + "A"
                        if bla not in new_test.keys():
                            new_test[bla] = (len(bla), 0)
                        new_length, new_num = new_test[bla]
                        new_test[bla] = (new_length, new_num + num)
                test_length = sum(l * n for l, n in new_test.values())
                test = new_test
            # print(test_length)
            lengths.append(test_length)
        # print(f"{code}: {min(lengths)}")
        code_complexities.append(min(lengths) * int(code[:-1]))

    print(sum(code_complexities))

    print("Execution time :", timeit.default_timer() - start)
