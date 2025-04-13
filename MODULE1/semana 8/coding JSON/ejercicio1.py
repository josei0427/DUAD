import json

def convert_file(pokemon_file):
    with open(pokemon_file, 'r') as file:
        data_result = json.load(file)
    return data_result


def add_pokemon(json_file):
    print("Ingrese la información del nuevo Pokémon:")
    english_name = input("Name: ")
    type_input = input("Tipo: ") 
    base_hp = int(input("HP: "))
    base_attack = int(input("Attack: "))
    base_defense = int(input("Defense: "))
    base_sp_attack = int(input("Sp. Attack: "))
    base_sp_defense = int(input("Sp. Defense: "))
    base_speed = int(input("Speed: "))

    new_pokemon = {
        "name": {
            "english": english_name
        },
        "type": [
            type_input
        ],
        "base": {
            "HP": base_hp,
            "Attack": base_attack,
            "Defense": base_defense,
            "Sp. Attack": base_sp_attack,
            "Sp. Defense": base_sp_defense,
            "Speed": base_speed
        }
    }
    json_file.append(new_pokemon)
    return json_file


def save_file(pokemon_file, update_file):
    with open(pokemon_file, 'w') as file:
        json.dump(update_file, file, indent=4)


json_file = convert_file("pokemon_data.json")
update_file = add_pokemon(json_file)
result_file = save_file("pokemon_data.json", update_file)

print("Data saved successfully.")