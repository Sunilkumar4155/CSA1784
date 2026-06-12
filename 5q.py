from collections import deque

def is_valid(m, c):
    # Check if numbers are out of bounds
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # Check if cannibals outnumber missionaries on either bank
    if (m > 0 and m < c) or (3 - m > 0 and (3 - m) < (3 - c)):
        return False
    return True

def solve_mc():
    # State format: (missionaries_left, cannibals_left, boat_position) 
    # boat: 1 for left bank, 0 for right bank
    start = (3, 3, 1)
    queue = deque([(start, [])])
    visited = set([start])

    # Possible boat moves: (missionaries, cannibals)
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    while queue:
        (m, c, boat), path = queue.popleft()
        current_path = path + [(m, c, boat)]

        if (m, c, boat) == (0, 0, 0):
            return current_path

        for dm, dc in moves:
            if boat == 1: # Moving Left to Right
                next_state = (m - dm, c - dc, 0)
            else:         # Moving Right to Left
                next_state = (m + dm, c + dc, 1)

            if is_valid(next_state[0], next_state[1]) and next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, current_path))

    return "No solution"

print("Missionaries & Cannibals Solution Path (M, C, Boat):")
for step in solve_mc():
    print(step)
