import networkx as nx
import matplotlib.pyplot as plt

class CustomGraph:
    def __init__(self):
        self.graph = nx.DiGraph()  # DiGraph for directed edges

    def add_custom_node(self, value):
        self.graph.add_node(value)

    def add_custom_edge(self, from_custom_node, to_custom_node, custom_weight):
        self.graph.add_edge(from_custom_node, to_custom_node, weight=custom_weight)

def custom_dynamic_programming_shortest_path(graph, source, destination):
    nodes = list(graph.nodes)
    custom_costs = {node: float('inf') for node in nodes}
    custom_costs[source] = 0

    for _ in range(len(nodes)):
        changed = False

        for node in nodes:
            for successor in graph.successors(node):
                custom_cost = graph[node][successor]['weight']
                if custom_costs[successor] > custom_cost + custom_costs[node]:
                    custom_costs[successor] = custom_cost + custom_costs[node]
                    changed = True

    return custom_costs[destination]

def visualize_custom_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    custom_edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=custom_edge_labels)
    plt.title("Visualizing Custom Graph")
    plt.show()

# Test Case 1
custom_graph1 = CustomGraph()
custom_graph1.add_custom_node("A")
custom_graph1.add_custom_node("B")
custom_graph1.add_custom_node("C")
custom_graph1.add_custom_node("D")
custom_graph1.add_custom_edge("A", "B", 3)
custom_graph1.add_custom_edge("B", "C", 2)
custom_graph1.add_custom_edge("A", "C", 4)
custom_graph1.add_custom_edge("C", "D", 3)
custom_graph1.add_custom_edge("B", "D", 1)

visualize_custom_graph(custom_graph1)
source_custom_node1 = "A"
destination_custom_node1 = "D"
custom_optimal_cost1 = custom_dynamic_programming_shortest_path(custom_graph1.graph, source_custom_node1, destination_custom_node1)
print("Optimal cost from {source_custom_node1} to {destination_custom_node1}: {custom_optimal_cost1}")

# Additional paths
print("Optimal cost from B to D: {custom_dynamic_programming_shortest_path(custom_graph1.graph, 'B', 'D')}")
print("Optimal cost from C to D: {custom_dynamic_programming_shortest_path(custom_graph1.graph, 'C', 'D')}")
print("Optimal cost from D to D: {custom_dynamic_programming_shortest_path(custom_graph1.graph, 'D', 'D')}")
# Test Case 2
custom_graph2 = CustomGraph()
custom_graph2.add_custom_node("A")
custom_graph2.add_custom_node("B")
custom_graph2.add_custom_node("C")
custom_graph2.add_custom_node("D")
custom_graph2.add_custom_edge("A", "B", 6)
custom_graph2.add_custom_edge("B", "C", 4)
custom_graph2.add_custom_edge("A", "C", 2)
custom_graph2.add_custom_edge("C", "D", 3)
custom_graph2.add_custom_edge("B", "D", 2)
custom_graph2.add_custom_edge("A", "D", 1)
visualize_custom_graph(custom_graph2)
source_custom_node2 = "A"
destination_custom_node2 = "D"
custom_optimal_cost2 = custom_dynamic_programming_shortest_path(custom_graph2.graph, source_custom_node2, destination_custom_node2)
print("Optimal cost from {source_custom_node2} to {destination_custom_node2}: {custom_optimal_cost2}")
# Additional paths
print("Optimal cost from B to D: {custom_dynamic_programming_shortest_path(custom_graph2.graph, 'B', 'D')}")
print("Optimal cost from C to D: {custom_dynamic_programming_shortest_path(custom_graph2.graph, 'C', 'D')}")
print("Optimal cost from D to D: {custom_dynamic_programming_shortest_path(custom_graph2.graph, 'D', 'D')}")
# Test Case 3
custom_graph3 = CustomGraph()
custom_graph3.add_custom_node("A")
custom_graph3.add_custom_node("B")
custom_graph3.add_custom_node("C")
custom_graph3.add_custom_node("D")
custom_graph3.add_custom_edge("A", "B", 2)
custom_graph3.add_custom_edge("B", "C", 5)
custom_graph3.add_custom_edge("C", "D", 4)
custom_graph3.add_custom_edge("A", "C", 7)
custom_graph3.add_custom_edge("B", "D", 1)
visualize_custom_graph(custom_graph3)
source_custom_node3 = "A"
destination_custom_node3 = "D"
custom_optimal_cost3 = custom_dynamic_programming_shortest_path(custom_graph3.graph, source_custom_node3, destination_custom_node3)
print("Optimal cost from {source_custom_node3} to {destination_custom_node3}: {custom_optimal_cost3}")
# Additional paths
print("Optimal cost from B to D: {custom_dynamic_programming_shortest_path(custom_graph3.graph, 'B', 'D')}")
print("Optimal cost from C to D: {custom_dynamic_programming_shortest_path(custom_graph3.graph, 'C', 'D')}")
print("Optimal cost from D to D: {custom_dynamic_programming_shortest_path(custom_graph3.graph, 'D', 'D')}")
