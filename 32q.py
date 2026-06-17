def pattern_match(text, pattern):
    """
    Checks if a pattern exists within the text.
    Returns the starting index if found, otherwise returns -1.
    """
    # Using Python's built-in 'find' method
    index = text.find(pattern)
    return index

# --- Example Usage ---
text_string = "Welcome to the world of Python programming"
search_pattern = "Python"

result = pattern_match(text_string, search_pattern)

if result != -1:
    print(f"Pattern '{search_pattern}' found at index {result}.")
else:
    print(f"Pattern '{search_pattern}' not found.")
