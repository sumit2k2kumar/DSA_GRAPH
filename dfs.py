import networkx as nx
import matplotlib.pyplot as plt

def depth_first_search(graph, start_node):
    visited = set()

    def dfs_recursive(node):
        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)
            for neighbor in graph[node]:
                dfs_recursive(neighbor)

    dfs_recursive(start_node)
    
def visualize_graph(graph):
    nx_graph = nx.Graph(graph)
    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    plt.title("Graph Visualization")
    plt.show()

# Sample Graph 1
graph_1 = {
    'S': ['A', 'B', 'C'],
    'A': ['S', 'D', 'E'],
    'B': ['S', 'F', 'G'],
    'C': ['S', 'H', 'I'],
    'D': ['A'],
    'E': ['A'],
    'F': ['B'],
    'G': ['B'],
    'H': ['C'],
    'I': ['C']
}

visualize_graph(graph_1)
print("Depth-First Search starting from node 'S' for Graph 1:")
depth_first_search(graph_1, 'S')

# Sample Graph 2
graph_2 = {
    '1': ['2', '3', '4'],
    '2': ['1', '5', '6'],
    '3': ['1', '7', '8'],
    '4': ['1', '9', '10'],
    '5': ['2'],
    '6': ['2'],
    '7': ['3'],
    '8': ['3'],
    '9': ['4'],
    '10': ['4']
}

visualize_graph(graph_2)
print("\nDepth-First Search starting from node '1' for Graph 2:")
depth_first_search(graph_2, '1')

# Sample Graph 3
graph_3 = {
    'X': ['Y', 'Z', 'W'],
    'Y': ['X', 'V', 'U'],
    'Z': ['X', 'T'],
    'W': ['X', 'S'],
    'V': ['Y'],
    'U': ['Y'],
    'T': ['Z'],
    'S': ['W']
}

visualize_graph(graph_3)
print("\nDepth-First Search starting from node 'X' for Graph 3:")
depth_first_search(graph_3, 'X')
