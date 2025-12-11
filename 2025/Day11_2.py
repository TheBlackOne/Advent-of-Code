import networkx as nx
import math
from tqdm import tqdm

input = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""

#with open("input.txt") as f:
#   input = f.read()

def search(graph, start, end):
    num_found = 0
    to_remove = set()
    simple_paths = nx.all_simple_paths(graph, start, end)

    for nodes in tqdm(simple_paths):
        num_found += 1
        for node in nodes:
            to_remove.add(node)
    to_remove.remove(start)
    graph.remove_nodes_from(to_remove)

    while True:
        no_outgoing = list(node for node, out_degree in graph.out_degree() if out_degree == 0 and node != start)
        if len(no_outgoing) == 0: break
        else:
            for node in no_outgoing:
                graph.remove_node(node)

    return num_found


if __name__ == "__main__":
    graph = nx.DiGraph()

    for line in input.splitlines():
        src, dest = line.split(': ')
        dest = dest.split()
        for d in dest:
            graph.add_edge(src, d)

    dac_out = search(graph, "dac", "out")
    fft_dac = search(graph, "fft", "dac")
    svr_fft = search(graph, "svr", "fft")   

    answer = math.prod([dac_out, fft_dac, svr_fft])

    print(answer)