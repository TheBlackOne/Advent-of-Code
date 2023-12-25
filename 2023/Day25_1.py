from os import path
import graphviz

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

components = {}


class Component:
    def __init__(self, name):
        self.name = name
        self.connections = set()

    def add_connection(self, other_component):
        self.connections.add(other_component)

    def remove_connection(self, other_component):
        self.connections.remove(other_component)


def visit_connections(component_name, visited_components):
    component = components[component_name]
    for other_comp_name in component.connections:
        if other_comp_name not in visited_components:
            visited_components.add(other_comp_name)
            visit_connections(other_comp_name, visited_components)

    return visited_components


def count_group(start_component_name):
    visited_components = set()
    visited_components = visit_connections(start_component_name, visited_components)

    return len(visited_components)


if __name__ == "__main__":
    for line in input.splitlines():
        comp_name, conn = line.split(": ")
        new_comp = Component(comp_name)
        for other_comp_name in conn.split():
            new_comp.add_connection(other_comp_name)
        components[comp_name] = new_comp

    for line in input.splitlines():
        comp_name, conn = line.split(": ")
        for other_comp_name in conn.split():
            if other_comp_name not in components.keys():
                new_comp = Component(other_comp_name)
                components[other_comp_name] = new_comp
            components[other_comp_name].add_connection(comp_name)

    dot = graphviz.Graph(engine="neato", strict=True)
    for component in components.values():
        dot.node(component.name)
        for other_component_name in component.connections:
            dot.edge(component.name, other_component_name)
    dot.render("graph.gv")

    remove_edges = [("nvd", "jqt"), ("cmg", "bvb"), ("pzl", "hfx")]
    for comp1, comp2 in remove_edges:
        components[comp1].remove_connection(comp2)
        components[comp2].remove_connection(comp1)

    cluster_sizes = [count_group(c) for c in remove_edges[0]]

    result = cluster_sizes[0] * cluster_sizes[1]

    print(result)
