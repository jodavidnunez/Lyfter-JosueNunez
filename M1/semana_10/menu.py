import actions
import data


def menu ():
    end_program = "No"
    menu_options = """
                         1. Provide new students information one by one. 
                         2. Get the information of all added students. 
                         3. Get the top 3 best students (average grades). 
                         4. Get the average of all the students. 
                         5. Export current data to output CSV. 
                         6. Import available data from existing CSV. 
                         7. Exit program. \n"""
    list_of_student_data_dicts = []
    csv_path = r'C:\Users\jodav\Documents\Curso_Progra_Lyfter\Lyfter-JosueNunez\semana_10\students_grades.csv'
    imported_csv_flag = 0
    while (end_program != "Yes"):
        user_opt = input(f'-I-(menu.py:menu): Please choose one of the following options: {menu_options}')
        user_opt = actions.validate_user_opt(user_opt, menu_options)
        if (user_opt == 1):
            list_of_student_data_dicts.extend(actions.get_students_from_user())
        elif (user_opt == 2):
            actions.print_all_students_data(list_of_student_data_dicts)
        elif (user_opt == 3):
            actions.print_top_3_students(list_of_student_data_dicts)
        elif (user_opt == 4):
            actions.print_average_of_all_students(list_of_student_data_dicts)
        elif (user_opt == 5):
            data.export_current_data_to_output_CSV(list_of_student_data_dicts, csv_path, imported_csv_flag)
        elif (user_opt == 6):
            list_of_student_data_dicts.extend(data.import_existing_data_from_CSV(csv_path))
            imported_csv_flag = 1
        else:
            end_program = "Yes"
            break