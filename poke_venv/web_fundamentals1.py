# Exploring Web Technologies and Python Programming

# Task 1: Setting Up a Python Virtual Environment and Installing Packages

# Successfully set up Python Virtual Environment: "poke_venv" and Installed Packages "requests"


# Task 2: Fetching Data from the Pokémon API

import requests
from termcolor import colored

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)
pokemon_data = response.json()
name = pokemon_data["name"]
abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
print(colored(f"\nPokèmon:", "green", attrs=["bold"]))
print(colored(f"{name}", "white"))
print(colored("\nAbilities:", "green", attrs=["bold"]))
for ability in abilities:
    print(ability)
print("")


# Task 3: Analyzing and Displaying Data

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        pokemon_data = response.json()
        name = pokemon_data["name"]
        abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
        weight = pokemon_data["weight"]
        pokemon_details = {
            "Pokèmon": name,
            "Abilities": abilities,
            "Weight": weight
        }
        pokemon_details_output = ", ".join(f"\n{key}: \n{value}" for key, value in pokemon_details.items()).replace(", ", "").replace("[", "").replace("]", "").replace("'", " ")
        return pokemon_details_output, weight  
    except Exception as e:
        print(f"Error: {e}")
        return None, 0  

def calculate_average_weight(pokemon_weights):
    if len(pokemon_weights) == 0: 
        return 0
    average_weight = sum(pokemon_weights) / len(pokemon_weights)
    return average_weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_weights = []  

for pokemon_name in pokemon_names:
    details_output, weight = fetch_pokemon_data(pokemon_name)  
    print(details_output)  
    pokemon_weights.append(weight)  


average_weight = calculate_average_weight(pokemon_weights)
print(colored(f"\nAverage Weight: {average_weight}", "blue", attrs=["bold"]))