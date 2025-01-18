import csv
from actions import validate_Y_N_question
from actions import Student
from pathlib import Path
import os


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


def validate_data_from_CSV(existing_list_of_students):
    validated_list_of_students = []
    for student in existing_list_of_students:
        name = validate_name_from_csv(student.name)
        group = student.group
        spanish_grade = validate_grade_from_csv(student.spanish_grade)
        english_grade = validate_grade_from_csv(student.english_grade)
        social_studies_grade = validate_grade_from_csv(student.social_studies_grade)
        science_grade = validate_grade_from_csv(student.science_grade)
        average_grade = validate_grade_from_csv(student.average_grade)
        validated_student = Student(name, group, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade)
        validated_list_of_students.append(validated_student)
    return validated_list_of_students


def export_current_data_to_output_CSV(list_of_students, csv_path, imported_csv_flag):
    file_path = Path(csv_path)
    user_opt = "Y"
    if (imported_csv_flag == 0 and file_path.exists() and os.path.getsize(csv_path) > 0):
        user_opt = input(f'-W-(data.py:export_current_data_to_output_CSV): You are going to overwrite the csv {csv_path} which already'
                         f'has previous content. Do you want to proceed with the override? (Y/N) : ')
        user_opt = validate_Y_N_question(user_opt)
    if (user_opt == "Y"): 
        if(len(list_of_students)):
            try:
                with open(csv_path, 'w', encoding='utf-8', newline='') as file:
                    test_obj = list_of_students[0]
                    headers = test_obj.attributes_names
                    writer = csv.writer(file)
                    writer.writerow(headers)
                    for student in list_of_students:
                        tmp_attributes_list = []
                        for header in headers:
                            tmp_attributes_list.append(str(getattr(student, str(header))))
                        writer.writerow(tmp_attributes_list)
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
    existing_list_of_students = []
    try: 
        counter = 0
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if(counter == 0):
                    counter += 1
                else:
                    name = row[0]
                    group = row[1]
                    spanish_grade =  row[2]
                    english_grade =  row[3]
                    social_studies_grade =  row[4]
                    science_grade =  row[5]
                    average_grade =  row[6]
                    student = Student(name, group, spanish_grade, english_grade, social_studies_grade, science_grade, average_grade)
                    existing_list_of_students.append(student) 
        return validate_data_from_CSV(existing_list_of_students)
    except IOError:
        print(f'-E-(data.py:export_current_data_to_output_CSV): An error showed up while trying to read the csv file \'{csv_path}\''
              f'-I-(data.py:export_current_data_to_output_CSV): Please verify that \'{csv_path}\' exists and is readable.\n'
        ) 