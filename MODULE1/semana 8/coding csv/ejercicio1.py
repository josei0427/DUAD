import csv

def enter_game():
    nombre = input("Ingrese el nombre del videojuego: ")
    genero = input("Ingrese el género del videojuego: ")
    desarrollador = input("Ingrese el desarrollador del videojuego: ")
    clasificacion = input("Ingrese la clasificación ESRB del videojuego: ")
    games_dict = {
        "Nombre": nombre,
        "Genero": genero,
        "Desarrollador": desarrollador,
        "Clasificacion": clasificacion
    }
    return games_dict


def save_game(games_info, filee, headers):
    with open(filee, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = headers)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerows(games_info)


headers = ('Nombre', 'Genero', 'Desarrollador', 'Clasificacion')
games_info = []

condi = True
while condi:
    game_data = enter_game()
    games_info.append(game_data)
    save_game(games_info, 'videojuegos.csv', headers)

    option = input("Quiere ingresar otro video juego? ( 'si' o 'no'): ")
    option = option.lower()
    if option == "si":
        continue
    elif option == "no":
        print(f"Se han guardado los datos de los videojuegos.")
        break