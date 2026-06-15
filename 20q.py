planets = {
    "mercury": {"distance": 0.39, "moons": 0},
    "venus": {"distance": 0.72, "moons": 0},
    "earth": {"distance": 1.00, "moons": 1},
    "mars": {"distance": 1.52, "moons": 2}
}

def get_moons(planet_name):
    planet = planets.get(planet_name.lower())
    return planet["moons"] if planet else "Unknown planet"

print(get_moons("mars"))
