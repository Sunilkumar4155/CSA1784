import itertools

def tsp(graph, start):
    vertices = [v for v in graph if v != start]
    min_path_weight = float('inf')
    best_path = []
    for permutation in itertools.permutations(vertices):
        current_weight = 0
        k = start
        current_path = [start]
        for next_vertex in permutation:
            current_weight += graph[k][next_vertex]
            k = next_vertex
            current_path.append(k)
        current_weight += graph[k][start]
        current_path.append(start)
        if current_weight < min_path_weight:
            min_path_weight = current_weight
            best_path = current_path
    return best_path, min_path_weight

graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}
print(tsp(graph, 'A'))
