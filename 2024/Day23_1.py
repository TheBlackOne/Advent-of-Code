from itertools import combinations

import networkx as nx

input = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

# with open("input.txt") as f:
#    input = f.read()

if __name__ == "__main__":
    G = nx.Graph()
    for line in input.splitlines():
        n2, n3 = line.split("-")
        G.add_edge(n2, n3)

    threes = set()

    all_cliques = nx.find_cliques(G)
    for clique in all_cliques:
        for nodes in combinations(clique, 3):
            if any(n.startswith("t") for n in nodes):
                threes.add(",".join(sorted(nodes)))

    print(len(threes))
