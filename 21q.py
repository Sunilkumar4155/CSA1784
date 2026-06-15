def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        print(f"Move disk from {source} to {target}")
        hanoi(n - 1, auxiliary, target, source)

hanoi(3, 'A', 'B', 'C')
