import networkx as nx
import matplotlib.pyplot as plt

class DirectedWeightedGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_vertex(self, value):
        self.graph.add_node(value)

    def add_directed_edge(self, from_vertex, to_vertex, weight):
        self.graph.add_edge(from_vertex, to_vertex, weight=weight)

def floyd_warshall(graph):
    vertices = graph.nodes
    all_shortest_paths = {vertex: {other_vertex: float('infinity') for other_vertex in vertices} for vertex in vertices}

    for vertex in vertices:
        all_shortest_paths[vertex][vertex] = 0

    for edge in graph.edges:
        all_shortest_paths[edge[0]][edge[1]] = graph[edge[0]][edge[1]]['weight']

    for intermediate_vertex in vertices:
        for source_vertex in vertices:
            for destination_vertex in vertices:
                if all_shortest_paths[source_vertex][intermediate_vertex] + all_shortest_paths[intermediate_vertex][destination_vertex] < all_shortest_paths[source_vertex][destination_vertex]:
                    all_shortest_paths[source_vertex][destination_vertex] = all_shortest_paths[source_vertex][intermediate_vertex] + all_shortest_paths[intermediate_vertex][destination_vertex]

    return all_shortest_paths

def visualize_weighted_directed_graph(graph):
    pos = nx.spring_layout(graph.graph)
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Weighted Directed Graph Visualization")
    plt.show()

# Test Case 1
graph1 = DirectedWeightedGraph()
graph1.add_vertex("A")
graph1.add_vertex("B")
graph1.add_vertex("C")
graph1.add_directed_edge("A", "B", 4)
graph1.add_directed_edge("B", "C", 2)
graph1.add_directed_edge("A", "C", 6)
print("Test Case 1:")
visualize_weighted_directed_graph(graph1)
all_shortest_paths_1 = floyd_warshall(graph1.graph)
print("All Shortest Paths:")
for source, paths in all_shortest_paths_1.items():
    print(f"From {source}:", paths)
print()

# Test Case 2
graph2 = DirectedWeightedGraph()
graph2.add_vertex("A")
graph2.add_vertex("B")
graph2.add_vertex("C")
graph2.add_vertex("D")
graph2.add_directed_edge("A", "B", 3)
graph2.add_directed_edge("B", "C", 1)
graph2.add_directed_edge("C", "D", 4)
graph2.add_directed_edge("A", "C", 1)
graph2.add_directed_edge("B", "D", 2)
print("Test Case 2:")
visualize_weighted_directed_graph(graph2)
all_shortest_paths_2 = floyd_warshall(graph2.graph)
print("All Shortest Paths:")
for source, paths in all_shortest_paths_2.items():
    print(f"From {source}:", paths)
print()

# Test Case 3
graph3 = DirectedWeightedGraph()
graph3.add_vertex("A")
graph3.add_vertex("B")
graph3.add_vertex("C")
graph3.add_vertex("D")
graph3.add_directed_edge("A", "B", 5)
graph3.add_directed_edge("B", "C", 3)
graph3.add_directed_edge("C", "D", 2)
graph3.add_directed_edge("A", "C", 1)
graph3.add_directed_edge("B", "D", 4)
print("Test Case 3:")
visualize_weighted_directed_graph(graph3)
all_shortest_paths_3 = floyd_warshall(graph3.graph)
print("All Shortest Paths:")
for source, paths in all_shortest_paths_3.items():
    print(f"From {source}:", paths)
print()
