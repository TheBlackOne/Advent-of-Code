import networkx as nx
import tqdm
import itertools
from sortedcontainers import SortedDict
import math

input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

#with open("input.txt") as f:
#   input = f.read()

if __name__ == "__main__":
    distances = SortedDict()
    lights = [tuple([int(c) for c in line.split(',')]) for line in input.splitlines()]

    G = nx.Graph()
    G.add_nodes_from(lights)

    for pos1, pos2 in tqdm.tqdm(list(itertools.combinations(lights, 2))):
        distance = math.dist(pos1, pos2)
        distances[distance] = (pos1, pos2)

    for pos1, pos2 in tqdm.tqdm(distances.values()):
        G.add_edge(pos1, pos2)
        if nx.is_connected(G):
            answer = pos1[0] * pos2[0]
            break
        
    print(answer)
    