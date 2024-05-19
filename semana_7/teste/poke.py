import requests
import json

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    """
    This function is the entry point of the Pokemon Info program.
    It prompts the user to enter a Pokemon name and displays its information.
    """

    print("Welcome to Pokemon Info!")
    pokemon_name = input("Enter a Pokemon name: ").lower()

    pokemon_info = get_pokemon_info(pokemon_name)
    print(f"Name: {pokemon_info['name']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Type: {pokemon_info['types'][0]['type']['name']}")
    print("Abilities:")
    for ability in pokemon_info["abilities"]:
        print(f"- {ability['ability']['name']}")

if __name__ == "__main__":
    main()