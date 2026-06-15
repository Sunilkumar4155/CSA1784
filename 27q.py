import queue

def best_first_search(graph, start, target, heuristics):
    visited = set()
    pq = queue.PriorityQueue()
    pq.put((heuristics[start], start))
    path = []

    while not pq.empty():
        _, current = pq.get()
        path.append(current)

        if current == target:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph.get(current, []):
                if neighbor not in visited:
                    pq.put((heuristics[neighbor], neighbor))
    return None

graph = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': [], 'F': []}
heuristics = {'A': 40, 'B': 32, 'C': 25, 'D': 35, 'E': 29, 'F': 0}
print(best_first_search(graph, 'A', 'F', heuristics))
