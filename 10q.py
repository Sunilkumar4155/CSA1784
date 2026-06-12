import heapq

def a_star(graph, heuristics, start, goal):
    pq = [(heuristics[start], start, [start], 0)]
    visited = set()
    while pq:
        f, current, path, g = heapq.heappop(pq)
        if current == goal: return path, g
        if current in visited: continue
        visited.add(current)
        for neighbor, edge_cost in graph.get(current, []):
            if neighbor not in visited:
                next_g = g + edge_cost
                next_f = next_g + heuristics.get(neighbor, 0)
                heapq.heappush(pq, (next_f, neighbor, path + [neighbor], next_g))
    return None, float('inf')

graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 5)], 'C': [('D', 1)], 'D': []}
heuristics = {'A': 5, 'B': 3, 'C': 2, 'D': 0}
print(a_star(graph, heuristics, 'A', 'D'))
