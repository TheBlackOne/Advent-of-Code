import networkx as nx
import itertools
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
    lights = [tuple([int(c) for c in line.split(',')]) for line in input.splitlines()]

    G = nx.Graph()
    edges = [(pos1, pos2, math.dist(pos1, pos2)) for pos1, pos2 in itertools.combinations(lights, 2)]
    G.add_weighted_edges_from(edges)

    # a Minimum Spanning Tree / MST creates a tree with the connections (=edges)
    # with the least weight (=distance)
    mst = nx.minimum_spanning_tree(G)
    # data=True to return weight data of the edges
    edges = mst.edges(data=True)

    # the connection (=edge) with the highest distance (=weight) is the one added last
    # last element of the 3-tuple contains a dict of edge data
    last_connection = max(edges, key=lambda edge: edge[-1]["weight"])

    pos1, pos2, _ = last_connection
    answer = pos1[0] * pos2[0]        
    print(answer)
    