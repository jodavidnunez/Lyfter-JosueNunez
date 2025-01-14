"""1. Investigue cómo leer y escribir archivos `JSON` en Python [aquí](https://www.w3schools.com/python/python_json.asp).
      Cree un programa que permita agregar un Pokémon nuevo al archivo de arriba.
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo."""


import json


def read_json_data_from_file(json_path):
    try:
        processed_json_data = {}
        with open(json_path, 'r', encoding='utf-8') as file:
            unprocessed_json_data = file.read()
            if (not unprocessed_json_data.strip()):
                raise ValueError(f'-E-(read_json_data_from_file): JSON file is empty: {json_path}')
                exit(1)
            processed_json_data = json.loads(unprocessed_json_data)
        print(f'-I-(read_json_data_from_file): JSON file is valid: {json_path}')
        return processed_json_data
    except json.JSONDecodeError:
        print(f'-E-(read_json_data_from_file): Invalid JSON data: {json_path}')
    except FileNotFoundError:
        print(f'-E-(read_json_data_from_file): File not found: {json_path}')
    except ValueError as e:
        print(f'-E-(read_json_data_from_file): Value error occured {e}: {json_path}')
    except Exception as e:
        print(f'-E-(read_json_data_from_file): An error occured {e}: {json_path}')
    exit(1)


def add_new_data_from_user_to_current_json_data(current_data):
    if (not isinstance(current_data, list)):
        raise ValueError(f'-E-(add_new_data_from_user_to_current_json_data): Current JSON data is not a list.')
        exit(1)
    counter = 1
    num_pokemon = input("-I-: Please introduce the total number of pokemon you intend to provide : ")
    try: 
        num_pokemon = int(num_pokemon)
    except ValueError:
        print(f'-E-(add_new_data_from_user_to_current_json_data): Number of pokemon must be an integer number.')
        print(f'-I-(add_new_data_from_user_to_current_json_data): Please rerun the program and provide an integer number of pokemon.')
        exit(1)
    new_data_list = []
    while (counter <= num_pokemon):
        pokemon_data_dict={}
        name = input(f'-I-: Please provide the name of the pokemon # {counter} : ')
        pokemon_type = input(f'-I-: Please provide the type of the pokemon # {counter} : ')
        HP_stat = input(f'-I-: For base stats, please provide the pokemon\'s # {counter} HP_stat : ')
        Attack_stat = input(f'-I-: For base stats, please provide the pokemon\'s # {counter} Attack_stat : ')
        Defense_stat = input(f'-I-: For base stats, please provide the pokemon\'s # {counter} Defense_stat : ')
        Sp_attack_stat = input(f'-I-: For base stats, please provide the pokemon\'s # {counter} Sp_attack_stat : ')
        Sp_defense_stat = input(f'-I-: For base stats, please provide the pokemon\'s # {counter} Sp_defense_stat : ')
        Speed_stat = input(f'-I-: For base stats, please provide the pokemon\'s # {counter} Speed_stat : ')
        pokemon_data_dict ["name"] = {"english":name}
        pokemon_data_dict ["type"] = [pokemon_type]
        pokemon_data_dict ["base"] = {
            "HP":HP_stat,
            "Attack":Attack_stat,
            "Defense":Defense_stat,
            "Sp. Attack":Sp_attack_stat,
            "Sp. Defense":Sp_defense_stat,
            "Speed":Speed_stat
        }
        new_data_list.append(pokemon_data_dict)
        counter += 1    
    final_data = []
    final_data.append(current_data)
    final_data.append(new_data_list)
    return final_data


def add_new_pokemon_to_json(): 
    output_dir = r'C:\Users\jodav\Documents\Curso_Progra_Lyfter\Semana_8\Ejercicios_Manejo_de_archivos'
    json_file = output_dir + "\\pokemon.txt"
    current_data = read_json_data_from_file(json_file)
    final_data = add_new_data_from_user_to_current_json_data(current_data)
    try:
        with open(json_file, 'w', encoding='utf-8') as file:
            json.dump(final_data, file, indent=4)
        print(f'-I-(add_new_pokemon_to_json): New pokemon(s) added successfully to JSON file: {json_file}')
    except IOError:
        print(f'-E-(add_new_pokemon_to_json): JSON file is not writable: {json_file}')


try:
    if __name__ == "__main__":
        add_new_pokemon_to_json()
except KeyboardInterrupt:
    print(f'\n-E-(add_new_pokemon_to_json): Manual interruption by user.')