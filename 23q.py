parent = {
    "john": "jack",
    "mary": "jack",
    "tom": "john"
}

def is_sibling(x, y):
    return parent.get(x) == parent.get(y) and x != y

def grandfather(x):
    father = parent.get(x)
    return parent.get(father) if father else None

print("Are john and mary siblings?", is_sibling("john", "mary"))
print("Grandfather of tom:", grandfather("tom"))
