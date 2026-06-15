kb = {
    "is_penguin": ["is_bird", "cannot_fly", "swims"],
    "is_bird": ["has_feathers", "lays_eggs"]
}
facts = {"has_feathers", "lays_eggs", "cannot_fly", "swims"}

def backward_chain(goal, kb, facts, visited=None):
    if visited is None:
        visited = set()
    if goal in facts:
        return True
    if goal not in kb or goal in visited:
        return False

    visited.add(goal)
    return all(backward_chain(premise, kb, facts, visited) for premise in kb[goal])

print("Is it a penguin?", backward_chain("is_penguin", kb, facts))
