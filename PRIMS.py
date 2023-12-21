import networkx as nx
import matplotlib.pyplot as plt
import heapq

class MinimumSpanningTreeSolver:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

    def visualize_graph(self, tree_edges=None):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

        if tree_edges:
            tree_edges_graph = nx.Graph()
            tree_edges_graph.add_weighted_edges_from(tree_edges)
            nx.draw_networkx_edges(tree_edges_graph, pos, edge_color='red', width=2)

        plt.title("Graph Visualization")
        plt.show()

    def solve_minimum_spanning_tree(self):
        mst_edges = []
        visited = set()
        start_node = list(self.graph.nodes)[0]  # Start from any node
        pq = [(0, start_node, None)]

        while pq:
            weight, current_node, parent_node = heapq.heappop(pq)

            if current_node not in visited:
                visited.add(current_node)
                if parent_node is not None:
                    mst_edges.append((parent_node, current_node, weight))

                for neighbor, edge_data in self.graph[current_node].items():
                    if neighbor not in visited:
                        heapq.heappush(pq, (edge_data['weight'], neighbor, current_node))

        return mst_edges

# Test Case 1
solver_case1 = MinimumSpanningTreeSolver()
solver_case1.add_node("A")
solver_case1.add_node("B")
solver_case1.add_node("C")
solver_case1.add_edge("A", "B", 3)
solver_case1.add_edge("B", "C", 1)
solver_case1.add_edge("A", "C", 2)

solver_case1.visualize_graph()
minimum_spanning_tree_edges_case1 = solver_case1.solve_minimum_spanning_tree()
print("Minimum Spanning Tree Edges (Test Case 1):", minimum_spanning_tree_edges_case1)
solver_case1.visualize_graph(minimum_spanning_tree_edges_case1)

# Test Case 2
solver_case2 = MinimumSpanningTreeSolver()
solver_case2.add_node("A")
solver_case2.add_node("B")
solver_case2.add_node("C")
solver_case2.add_node("D")
solver_case2.add_edge("A", "B", 1)
solver_case2.add_edge("B", "C", 2)
solver_case2.add_edge("C", "D", 1)
solver_case2.add_edge("A", "C", 4)
solver_case2.add_edge("B", "D", 7)

solver_case2.visualize_graph()
minimum_spanning_tree_edges_case2 = solver_case2.solve_minimum_spanning_tree()
print("Minimum Spanning Tree Edges (Test Case 2):", minimum_spanning_tree_edges_case2)
solver_case2.visualize_graph(minimum_spanning_tree_edges_case2)

# Test Case 3
solver_case3 = MinimumSpanningTreeSolver()
solver_case3.add_node("X")
solver_case3.add_node("Y")
solver_case3.add_node("Z")
solver_case3.add_node("W")
solver_case3.add_node("V")
solver_case3.add_edge("X", "Y", 2)
solver_case3.add_edge("Y", "Z", 3)
solver_case3.add_edge("Z", "W", 1)
solver_case3.add_edge("W", "V", 4)
solver_case3.add_edge("V", "X", 5)

solver_case3.visualize_graph()
minimum_spanning_tree_edges_case3 = solver_case3.solve_minimum_spanning_tree()
print("Minimum Spanning Tree Edges (Test Case 3):", minimum_spanning_tree_edges_case3)
solver_case3.visualize_graph(minimum_spanning_tree_edges_case3)
