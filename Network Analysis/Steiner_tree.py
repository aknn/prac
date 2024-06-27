import networkx as nx
import matplotlib.pyplot as plt

# Create a graph from the adjacency matrix
G = nx.Graph()

# Define the adjacency matrix
adj_matrix = [
    [0, 3, 0, 5, 2, 0],
    [3, 0, 5, 0, 2, 0],
    [0, 5, 0, 3, 0, 2],
    [5, 0, 3, 0, 0, 2],
    [2, 2, 0, 0, 0, 2],
    [0, 0, 2, 2, 2, 0]
]

# Add nodes
for i in range(6):
    G.add_node(i + 1)

# Add edges with weights
for i in range(6):
    for j in range(i + 1, 6):
        if adj_matrix[i][j] != 0:
            G.add_edge(i + 1, j + 1, weight=adj_matrix[i][j])

# Define the terminal nodes
terminals = [1, 2, 3, 4]

# Use the approximation algorithm for the Steiner tree
steiner_tree = nx.algorithms.approximation.steiner_tree(G, terminals, weight='weight')

# Draw the original graph
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=20)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Original Graph')
plt.show()

# Draw the Steiner tree
plt.figure(figsize=(12, 8))
nx.draw(steiner_tree, pos, with_labels=True, node_color='lightgreen', edge_color='red', node_size=2000, font_size=20)
labels = nx.get_edge_attributes(steiner_tree, 'weight')
nx.draw_networkx_edge_labels(steiner_tree, pos, edge_labels=labels)
plt.title('Steiner Tree')
plt.show()

# Nodes in the Steiner tree
steiner_tree_nodes = list(steiner_tree.nodes)
steiner_tree_nodes