"""1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `tsv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB"""


import csv

def collect_user_inputs():
    counter = 1
    num_games = input("-I-: Please introduce the total number of games you intend to provide : ")
    try: 
        num_games = int(num_games)
    except ValueError:
        print(f'-E-(collect_inputs) Number of games must be an integer number.')
        print(f'-I-(collect_inputs) Please rerun the program and provide an integer number of games.')
        exit(1)
    dict_list = []
    while (counter <= num_games):
        games_data_dict={}
        name = input(f'-I-: Please provide the name of video game # {counter} : ')
        genera = input(f'-I-: Please provide the genera of video game # {counter} : ')
        developers = input(f'-I-: Please provide the developers of video game # {counter} : ')
        classification = input(f'-I-: Please provide the classification of video game # {counter} : ')
        games_data_dict ["nombre"] = name
        games_data_dict ["genero"] = genera
        games_data_dict ["desarrollador"] = developers
        games_data_dict ["clasificacion"] = classification
        dict_list.append(games_data_dict)
        counter += 1    
    return dict_list


def write_tsv_file(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)


def build_games_tsv():
    output_dir = r'C:\Users\jodav\Documents\Curso_Progra_Lyfter\Semana_8\Ejercicios_Manejo_de_archivos'
    output_file  = output_dir + "/games.tsv"
    games_data_dicts_list = collect_user_inputs()
    tsv_headers = games_data_dicts_list[0].keys()
    try:
        write_tsv_file(output_file, games_data_dicts_list, tsv_headers)
        print(f'-I-(build_games_tsv) tsv with the requested information recorded in the path : {output_file}')
    except IOError:
        print(f'-E-(build_games_tsv) An error showed up while trying to write the output tsv file \'{output_file}\''
              f'-I-(build_games_tsv) Please verify the output directory \'{output_dir}\' exists,' 
              f'and also check that the path for the file \'{output_file}\' has write permissions.\n' 
              f'HINT: Write permissions can be affected if you are trying to write the file while'
              f'its already open by dome other program.'
        )
        exit(1)


try:
    if __name__ == "__main__":
        build_games_tsv()
except KeyboardInterrupt:
    print(f'\n-E-(build_games_tsv): Manual interruption by user.')