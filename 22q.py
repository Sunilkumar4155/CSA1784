birds = {
    "sparrow": True,
    "pigeon": True,
    "penguin": False,
    "ostrich": False
}

def check_fly(bird_name):
    can_fly = birds.get(bird_name.lower())
    if can_fly is True:
        return f"{bird_name} can fly."
    elif can_fly is False:
        return f"{bird_name} cannot fly."
    return "Unknown bird"

print(check_fly("penguin"))
