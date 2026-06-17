def count_vowels(input_string):
    """
    Counts and returns the number of vowels in a given string.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    
    for char in input_string:
        if char in vowels:
            vowel_count += 1
            
    return vowel_count

# --- Example Usage ---
user_text = "Artificial Intelligence"
total_vowels = count_vowels(user_text)

print(f"The text: '{user_text}'")
print(f"Number of vowels: {total_vowels}")
