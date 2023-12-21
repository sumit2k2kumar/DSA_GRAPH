import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Use DiGraph for directed edges

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.graph.nodes}
    previous_nodes = {node: None for node in graph.graph.nodes}
    distances[start] = 0

    unvisited_nodes = set(graph.graph.nodes)

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)

        for neighbor, edge_data in graph.graph[current_node].items():
            distance_to_neighbor = distances[current_node] + edge_data['weight']
            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                previous_nodes[neighbor] = current_node

    return distances, previous_nodes

def drawing_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

# Test Case 1
graph1 = Graph()
graph1.add_node("A")
graph1.add_node("B")
graph1.add_node("C")
graph1.add_node("D")
graph1.add_edge("A", "B", 6)
graph1.add_edge("B", "C", 4)
graph1.add_edge("C", "D", 2)
graph1.add_edge("A", "C", 3)
graph1.add_edge("B", "D", 1)
graph1.add_edge("D", "A", 1)
print("Test Case 1:")
drawing_graph(graph1)
shortest_distances_1, previous_nodes_1 = dijkstra(graph1, "A")
print("Shortest Distances from A:", shortest_distances_1)
print("Previous Nodes:", previous_nodes_1)

# Test Case 2
graph2 = Graph()
graph2.add_node("A")
graph2.add_node("B")
graph2.add_node("C")
graph2.add_node("D")
graph2.add_edge("A", "B", 1)
graph2.add_edge("B", "C", 2)
graph2.add_edge("C", "D", 3)
graph2.add_edge("A", "C", 1)
graph2.add_edge("B", "D", 5)
print("Test Case 2:")
drawing_graph(graph2)
shortest_distances_2, previous_nodes_2 = dijkstra(graph2, "B")
print("Shortest Distances from B:", shortest_distances_2)
print("Previous Nodes:", previous_nodes_2)

# Test Case 3
graph3 = Graph()
graph3.add_node("A")
graph3.add_node("B")
graph3.add_node("C")
graph3.add_node("D")
graph3.add_edge("A", "B", 3)
graph3.add_edge("B", "C", 1)
graph3.add_edge("C", "D", 5)
graph3.add_edge("A", "C", 2)
graph3.add_edge("B", "D", 2)
print("Test Case 3:")
drawing_graph(graph3)
shortest_distances_3, previous_nodes_3 = dijkstra(graph3, "A")
print("Shortest Distances from A:", shortest_distances_3)
print("Previous Nodes:", previous_nodes_3)
