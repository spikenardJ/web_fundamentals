# Question 2: Exploring the Digital Cosmos with Python and the Web

# Task 1: Set up a Python Virtual Environment and Install Required Packages

# Successfully set up Python Virtual Environment: "space_venv" and Installed Packages "requests"

# Task 2: Fetch Data from a Space API

import requests
from termcolor import colored

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()["bodies"]

    #process each planet info
    for planet in planets:
        if planet["isPlanet"]:
            name = planet["englishName"] #get planet English name
            mass = planet["mass"]["massValue"] #get planet mass
            orbit_period = planet["sideralOrbit"] #get planet orbit period
            print(f"\nPlanet: {name}\nMass: {mass}\nOrbit Period: {orbit_period} days\n")

fetch_planet_data()

# Task 3: Data Presentation and Analysis

def fetch_planet_data():
    # Enhance format the output in a more readable manner
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()["bodies"]
    try:
        list_of_planets = []
        #process each planet info
        for planet in planets:
            planet_dict = {}
            if planet["isPlanet"]:
                name = planet["englishName"] #get planet English name
                mass = planet["mass"]["massValue"] #get planet mass
                orbit_period = planet["sideralOrbit"] #get planet orbit period
                planet_dict = {
                    "name": name,
                    "mass": mass,
                    "orbit_period": orbit_period
                }
                list_of_planets.append(planet_dict)
                print(colored(f"Planet:", "grey"))
                print(colored(f"{name}", "blue"))
                print(colored(f"Mass:", "grey"))
                print(colored(f"{mass}", "blue"))
                print(colored(f"Orbit Period:", "grey"))
                print(colored(f"{orbit_period}\n", "blue"))
                print(colored(f"-------------\n", "grey"))
        return list_of_planets #list of planets
    except Exception as e:
        print(f"Error: {e}")
        return None, 0
    
def find_heaviest_planet(planets):
    
    if len(planets) == 0:
        return 0
    mass_values = []
    for planet in planets:
        print(planet)
        for k, v in planet.items():
            if k == "mass":
                mass_values.append(v)
        heaviest_planet = max(mass_values)  
        for k, v in planet.items():
            if v == heaviest_planet:
                return planet
list_of_planets = fetch_planet_data()

planets = fetch_planet_data()
heaviest_planet = find_heaviest_planet(planets)
print(" ")
print(colored(f"Heaviest Planet: {heaviest_planet["name"]} \nHeaviest Planet Mass: {heaviest_planet["mass"]}", "blue", attrs=["bold"]))
print(" ")
