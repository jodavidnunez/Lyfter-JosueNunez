import csv
from actions import validate_Y_N_question

def validate_name_from_csv(name):
    import re
    try:
        is_alpha_space_chk = bool(re.fullmatch(r'[A-Za-z\s]+', str(name)))
        if (is_alpha_space_chk is False):
            raise ValueError
    except ValueError:
        print(f'-E-(data.py:validate_name_from_csv): Provided name \'{name}\' in CSV is invalid. Valid names are strings that contains only alphabet characters and spaces.')
        print(f'-I-(data.py:validate_name_from_csv): Please review and fix the CSV file before trying to importing it.')
        exit(1)
    return str(name.strip())


def validate_grade_from_csv(grade):
    try:
        if (int(grade) < 0 or int(grade) > 100):
            raise ValueError
    except ValueError:
        print(f'-E-(data.py:validate_grade_from_csv): Provided grade \'{grade}\' in CSV is invalid. Valid grades are integers in the range of [0-100].')
        print(f'-I-(data.py:validate_grade_from_csv): Please review and fix the CSV file before trying to importing it.')
        exit(1)
    return int(grade.strip())


def validate_data_from_CSV(existing_list_of_student_data_dicts):
    validated_list_of_student_data_dicts = []
    for student_dict in existing_list_of_student_data_dicts:
        new_student_dict = {}
        new_student_dict['name'] = validate_name_from_csv(student_dict['name'])
        new_student_dict['group'] = student_dict['group']
        new_student_dict['spanish_grade'] = validate_grade_from_csv(student_dict['spanish_grade'])
        new_student_dict['english_grade'] = validate_grade_from_csv(student_dict['english_grade'])
        new_student_dict['social_studies_grade'] = validate_grade_from_csv(student_dict['social_studies_grade'])
        new_student_dict['science_grade'] = validate_grade_from_csv(student_dict['science_grade'])
        new_student_dict['average_grade'] = validate_grade_from_csv(student_dict['average_grade'])
        validated_list_of_student_data_dicts.append(new_student_dict)
    return validated_list_of_student_data_dicts


def export_current_data_to_output_CSV(list_of_student_data_dicts, csv_path, imported_csv_flag):
    from pathlib import Path
    import os
    file_path = Path(csv_path)
    user_opt = "Y"
    if (imported_csv_flag == 0 and file_path.exists() and os.path.getsize(csv_path) > 0):
        user_opt = input(f'-W-(data.py:export_current_data_to_output_CSV): You are going to overwrite the csv {csv_path} which already'
                         f'has previous content. Do you want to proceed with the override? (Y/N) : ')
        user_opt = validate_Y_N_question(user_opt)
    if (user_opt == "Y"): 
        if(len(list_of_student_data_dicts)):
            try:
                with open(csv_path, 'w', encoding='utf-8', newline='') as file:
                    headers = list_of_student_data_dicts[0].keys()
                    writer = csv.DictWriter(file, headers)
                    writer.writeheader()
                    writer.writerows(list_of_student_data_dicts)
            except IOError:
                print(f'-E-(data.py:export_current_data_to_output_CSV): An error showed up while trying to write the csv file \'{csv_path}\''
                    f'-I-(data.py:export_current_data_to_output_CSV): Please verify the output directory exists,' 
                    f'and also check that the path for the file \'{csv_path}\' has write permissions.\n' 
                    f'HINT: Write permissions can be affected if you are trying to write the file while'
                    f'its already open by dome other program.'
                )
        else:
            print(f'-E-(data.py:export_current_data_to_output_CSV): No available students data yet. Please introduce manually one or more students, or import a CSV file before running this function.\n')
    else:
        print(f'-I-(data.py:export_current_data_to_output_CSV): User decided to not proceed with the override of the existing csv.') 


def import_existing_data_from_CSV(csv_path):
    existing_list_of_student_data_dicts = []
    try: 
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            existing_list_of_student_data_dicts = [row for row in reader]
        return validate_data_from_CSV(existing_list_of_student_data_dicts)
    except IOError:
        print(f'-E-(data.py:export_current_data_to_output_CSV): An error showed up while trying to read the csv file \'{csv_path}\''
              f'-I-(data.py:export_current_data_to_output_CSV): Please verify that \'{csv_path}\' exists and is readable.\n'
        )
        exit(1) 