import networkx as nx
import matplotlib.pyplot as plt

class CustomGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_custom_node(self, value):
        self.graph.add_node(value)

    def add_custom_edge(self, from_node, to_node, custom_weight):
        self.graph.add_edge(from_node, to_node, custom_weight=custom_weight)

    def visualize_custom_graph(self, tree_edges=None):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

        if tree_edges:
            tree_edges_graph = nx.Graph()
            tree_edges_graph.add_weighted_edges_from(tree_edges)
            nx.draw_networkx_edges(tree_edges_graph, pos, edge_color='red', width=2)

        plt.title("Custom Graph Visualization")
        plt.show()

def custom_kruskal(custom_graph):
    mst_edges = []
    edge_list = [(edge[2]['custom_weight'], edge) for edge in custom_graph.graph.edges(data=True)]
    edge_list.sort()

    custom_union_find = {node: node for node in custom_graph.graph.nodes}

    for weight, edge in edge_list:
        node1, node2 = edge[0], edge[1]
        root1 = custom_find(custom_union_find, node1)
        root2 = custom_find(custom_union_find, node2)

        if root1 != root2:
            mst_edges.append((node1, node2, weight))
            custom_union(custom_union_find, root1, root2)

    return mst_edges

def custom_find(custom_union_find, node):
    if custom_union_find[node] != node:
        custom_union_find[node] = custom_find(custom_union_find, custom_union_find[node])
    return custom_union_find[node]

def custom_union(custom_union_find, root1, root2):
    custom_union_find[root1] = root2

# Test Case 1
custom_graph1 = CustomGraph()
custom_graph1.add_custom_node("A")
custom_graph1.add_custom_node("B")
custom_graph1.add_custom_node("C")
custom_graph1.add_custom_edge("A", "B", 3)
custom_graph1.add_custom_edge("B", "C", 1)
custom_graph1.add_custom_edge("A", "C", 2)

custom_graph1.visualize_custom_graph()
minimum_spanning_tree_edges_custom1 = custom_kruskal(custom_graph1)
print("Minimum Spanning Tree Edges (Test Case 1):", minimum_spanning_tree_edges_custom1)
custom_graph1.visualize_custom_graph(minimum_spanning_tree_edges_custom1)

# Test Case 2
custom_graph2 = CustomGraph()
custom_graph2.add_custom_node("A")
custom_graph2.add_custom_node("B")
custom_graph2.add_custom_node("C")
custom_graph2.add_custom_node("D")
custom_graph2.add_custom_edge("A", "B", 1)
custom_graph2.add_custom_edge("B", "C", 2)
custom_graph2.add_custom_edge("C", "D", 1)
custom_graph2.add_custom_edge("A", "C", 4)
custom_graph2.add_custom_edge("B", "D", 7)

custom_graph2.visualize_custom_graph()
minimum_spanning_tree_edges_custom2 = custom_kruskal(custom_graph2)
print("Minimum Spanning Tree Edges (Test Case 2):", minimum_spanning_tree_edges_custom2)
custom_graph2.visualize_custom_graph(minimum_spanning_tree_edges_custom2)

# Test Case 3
custom_graph3 = CustomGraph()
custom_graph3.add_custom_node("X")
custom_graph3.add_custom_node("Y")
custom_graph3.add_custom_node("Z")
custom_graph3.add_custom_edge("X", "Y", 2)
custom_graph3.add_custom_edge("Y", "Z", 3)
custom_graph3.add_custom_edge("X", "Z", 1)

custom_graph3.visualize_custom_graph()
minimum_spanning_tree_edges_custom3 = custom_kruskal(custom_graph3)
print("Minimum Spanning Tree Edges (Test Case 3):", minimum_spanning_tree_edges_custom3)
custom_graph3.visualize_custom_graph(minimum_spanning_tree_edges_custom3)
