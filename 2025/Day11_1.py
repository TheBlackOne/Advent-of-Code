import networkx as nx

input = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

#with open("input.txt") as f:
#   input = f.read()

if __name__ == "__main__":
    graph = nx.DiGraph()

    for line in input.splitlines():
        src, dest = line.split(': ')
        dest = dest.split()
        for d in dest:
            graph.add_edge(src, d)
    
    answer = len(list(nx.all_simple_paths(graph, "you", "out")))
    print(answer)