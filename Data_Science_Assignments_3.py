import pandas as pd
import requests


def download_data(url):
    response = requests.get(url)
    return response.json()


def process_data(data):
    pokemon_list = data["pokemon"]
    processed_data = []

    for pokemon in pokemon_list:
        pokemon_data = {
            "ID": pokemon["id"],
            "Number": pokemon["num"],
            "Name": pokemon["name"],
            "Image URL": pokemon["img"],
            "Type": ", ".join(pokemon["type"]),
            "Height": pokemon["height"],
            "Weight": pokemon["weight"],
            "Candy": pokemon.get("candy", ""),
            "Candy Count": pokemon.get("candy_count", ""),
            "Egg": pokemon.get("egg", ""),
            "spawn_chance": pokemon.get("spawn_chance", ""),
            "avg_spawns": pokemon.get("avg_spawns", ""), "spawn_time": pokemon.get("spawn_time", ""),
            "weakness": ", ".join(pokemon.get("weaknesses", []))
        }
        processed_data.append(pokemon_data)

    return processed_data


def export_to_excel(data, output_file):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)


# Example usage
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
output_file = "pokemon_data2.xlsx"

# Download data
data = download_data(url)
# Process data
processed_data = process_data(data)

# Export to Excel
export_to_excel(processed_data, output_file)

print(f"Data downloaded, processed, and exported to {output_file} successfully!")