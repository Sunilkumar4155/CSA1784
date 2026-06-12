def vacuum_cleaner(location, status_A, status_B):
    rooms = {'A': status_A, 'B': status_B}
    print(f"Initial State: Location={location}, Rooms={rooms}")
    for _ in range(2):
        if rooms[location] == "Dirty":
            print(f"Room {location} is Dirty. Sucking dirt...")
            rooms[location] = "Clean"
            print(f"Room {location} is now Clean.")
        else:
            print(f"Room {location} is already Clean.")
        location = 'B' if location == 'A' else 'A'
        print(f"Moving to Room {location}...\n")

vacuum_cleaner('A', 'Dirty', 'Dirty')
