fruit_colors = [
    ("apple", "red"),
    ("banana", "yellow"),
    ("grape", "purple"),
    ("apple", "green")
]

def find_fruits_by_color(target_color):
    results = []
    for fruit, color in fruit_colors:
        if color == target_color.lower():
            results.append(fruit)
    return results

print(find_fruits_by_color("red"))
