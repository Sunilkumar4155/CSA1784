def color_map(neighbors, colors, assignment={}):
    if len(assignment) == len(neighbors):
        return assignment
    var = next(n for n in neighbors if n not in assignment)
    for color in colors:
        if all(assignment.get(nb) != color for nb in neighbors[var]):
            assignment[var] = color
            result = color_map(neighbors, colors, assignment)
            if result:
                return result
            del assignment[var]
    return None

graph = {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
print(color_map(graph, ['Red', 'Green', 'Blue']))
