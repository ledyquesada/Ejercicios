# Algortimo de Kruskal


def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        rank[root_y] += 1

def kruskal(graph):
    edges = []
    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((weight, node, neighbor))

    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}
    minimum_spanning_tree = {}

    for edge in edges:
        weight, node1, node2 = edge
        if find(parent, node1) != find(parent, node2):
            union(parent, rank, node1, node2)
            if node1 not in minimum_spanning_tree:
                minimum_spanning_tree[node1] = {}
            minimum_spanning_tree[node1][node2] = weight

    return minimum_spanning_tree

# Uso
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'D': 3, 'E': 10},
    'C': {'E': 5},
    'D': {'A': 1, 'B': 3, 'E': 7},
    'E': {'B': 10, 'C': 5, 'D': 7}
}

result = kruskal(graph)
print(result)
