def dfs(graph, vertex, visited=None, order=None):
    if visited is None: visited = set()
    if order is None: order = []
    visited.add(vertex)
    order.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
print(dfs(graph, 'A'))
