import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def explore_nodes_bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            print(f"Visited: {current_node}")
            visited.add(current_node)
            neighbors = graph[current_node]
            queue.extend(neighbors)

def visualize_graph(graph):
    nx_graph = nx.Graph(graph)
    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    plt.title("Graph Visualization")
    plt.show()

# Sample Graph 1
graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

visualize_graph(graph_1)
print("Breadth-First Search starting from node 'A' for Graph 1:")
explore_nodes_bfs(graph_1, 'A')

# Sample Graph 2
graph_2 = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2'],
    '5': ['2'],
    '6': ['3'],
    '7': ['3']
}

visualize_graph(graph_2)
print("\nBreadth-First Search starting from node '1' for Graph 2:")
explore_nodes_bfs(graph_2, '1')

# Sample Graph 3
graph_3 = {
    'M': ['N', 'O', 'P'],
    'N': ['M', 'Q'],
    'O': ['M', 'R', 'S'],
    'P': ['M', 'T'],
    'Q': ['N', 'U'],
    'R': ['O'],
    'S': ['O', 'V'],
    'T': ['P'],
    'U': ['Q', 'W'],
    'V': ['S', 'X'],
    'W': ['U'],
    'X': ['V', 'Y', 'Z'],
    'Y': ['X'],
    'Z': ['X']
}

visualize_graph(graph_3)
print("\nBreadth-First Search starting from node 'M' for Graph 3:")
explore_nodes_bfs(graph_3, 'M')
