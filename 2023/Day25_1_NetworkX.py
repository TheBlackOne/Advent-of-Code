from os import path
import networkx as nx
import math

input = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr"""

dir = path.dirname(__file__)
input_path = path.join(dir, "input.txt")
# with open(input_path) as f:
#    input = f.read()


if __name__ == "__main__":
    G = nx.Graph()

    for line in input.splitlines():
        comp_name, conn = line.split(": ")
        connections = conn.split()
        edges = list(zip([comp_name] * len(connections), connections))
        G.add_edges_from(edges, capacity=1)

    bridges = nx.minimum_edge_cut(G)
    G.remove_edges_from(bridges)

    groups = nx.connected_components(G)
    result = math.prod([len(g) for g in groups])

    print(result)
