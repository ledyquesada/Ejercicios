
# Implementación en Python
def has_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False

# Uso
graph_with_cycle = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['A'],
    'E': []
}

graph_without_cycle = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

print(has_cycle(graph_with_cycle))  # True
print(has_cycle(graph_without_cycle))  # False
