import itertools

def solve_crypt():
    # Words in the equation: SEND + MORE = MONEY
    words = ["SEND", "MORE", "MONEY"]
    unique_chars = set("".join(words))
    
    assert len(unique_chars) <= 10, "Too many unique characters!"
    chars = list(unique_chars)
    
    # Try all unique digit permutations for the characters
    for perm in itertools.permutations(range(10), len(chars)):
        mapping = dict(zip(chars, perm))
        
        # Leading digits cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
            
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']
        
        if send + more == money:
            print(f"Solution Found: {mapping}")
            print(f"{send} + {more} = {money}")
            return

solve_crypt()
