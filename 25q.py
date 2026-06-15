def solve_monkey_banana(state):
    monkey, box, banana, has_banana = state
    if has_banana:
        return ["Grasp banana"]
    
    if monkey != box:
        return [f"Walk to {box}"] + solve_monkey_banana((box, box, banana, has_banana))
    elif box != banana:
        return [f"Drag box to {banana}"] + solve_monkey_banana((banana, banana, banana, has_banana))
    else:
        return ["Climb box"] + solve_monkey_banana((monkey, box, banana, True))

initial_state = ("door", "window", "middle", False)
print("\n".join(solve_monkey_banana(initial_state)))
