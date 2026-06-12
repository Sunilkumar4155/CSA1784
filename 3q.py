from collections import deque

def water_jug_bfs(X, Y, target):
    queue = deque([(0, 0, [])]) # (jug1, jug2, path_taken)
    visited = set([(0, 0)])

    while queue:
        j1, j2, path = queue.popleft()
        current_path = path + [(j1, j2)]

        if j1 == target or j2 == target:
            return current_path

        # Possible states: Fill J1, Fill J2, Empty J1, Empty J2, Pour J1->J2, Pour J2->J1
        states = [
            (X, j2), (j1, Y), (0, j2), (j1, 0),
            (j1 - min(j1, Y - j2), j2 + min(j1, Y - j2)),
            (j1 + min(j2, X - j1), j2 - min(j2, X - j1))
        ]

        for s in states:
            if s not in visited:
                visited.add(s)
                queue.append((s[0], s[1], current_path))
                
    return "No solution possible"

# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
print("Water Jug Solution Path:")
print(water_jug_bfs(4, 3, 2))
