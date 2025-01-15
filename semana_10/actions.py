def validate_user_opt(user_opt, menu_options):
    while True:
        try:
            if (int(user_opt) < 0 or int(user_opt) > 7):
                raise ValueError
        except ValueError:
            print(f'-E-(actions.py:validate_user_opt): Provided user option is invalid. Valid options are integers in the range of [1-7].')
            user_opt = input(f'-I-(actions.py:validate_user_opt): Please provide a valid option : {menu_options}')
        else:
            user_opt = int(user_opt)
            break
    return user_opt


def validate_Y_N_question(y_n_usr_input):
    while True:
        try:
            is_Y_or_N_chk = set(y_n_usr_input).issubset({'Y', 'N'})
            if (is_Y_or_N_chk is False):
                raise ValueError
        except ValueError:
            print(f'-E-(actions.py:validate_name): Provided answer is invalid. Valid answers are only \'Y\' or \'N\'.')
            y_n_usr_input = input(f'-I-(actions.py:validate_name): Please provide a valid answer : ')
        else:
            y_n_usr_input = str(y_n_usr_input)
            break
    return y_n_usr_input


def validate_name(name):
    import re
    while True:
        try:
            is_alpha_space_chk = bool(re.fullmatch(r'[A-Za-z\s]+', str(name)))
            if (is_alpha_space_chk is False):
                raise ValueError
        except ValueError:
            print(f'-E-(actions.py:validate_name): Provided name is invalid. Valid names are strings that contains only alphabet characters and spaces.')
            name = input(f'-I-(actions.py:validate_name): Please provide a valid name : ')
        else:
            name = str(name)
            break
    return name


def validate_grade(grade):
    while True:
        try:
            if (int(grade) < 0 or int(grade) > 100):
                raise ValueError
        except ValueError:
            print(f'-E-(actions.py:validate_grade): Provided grade is invalid. Valid grades are integers in the range of [0-100].')
            grade = input(f'-I-(actions.py:validate_grade): Please provide a valid grade : ')
        else:
            grade = int(grade)
            break
    return grade


def get_students_from_user():
    end_of_user_inputs_flag = 0
    counter = 1
    list_of_student_data_dicts = []
    while(end_of_user_inputs_flag != 1):
        single_student_dict = {}
        total_grade = 0
        num_of_grades = 0
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the name of student # {counter}: ')
        single_student_dict['name'] = user_input
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the group of student # {counter}: ')
        single_student_dict['group'] = user_input
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the grade of the \'Spanish\' signature of student # {counter}: ')
        user_input = validate_grade(user_input)
        single_student_dict['spanish_grade'] = user_input
        total_grade += user_input
        num_of_grades += 1
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the grade of the \'English\' signature of student # {counter}: ')
        user_input = validate_grade(user_input)
        single_student_dict['english_grade'] = user_input
        total_grade += user_input
        num_of_grades += 1
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the grade of the \'Social studies\' signature of student # {counter}: ')
        user_input = validate_grade(user_input)
        single_student_dict['social_studies_grade'] = user_input
        total_grade += user_input
        num_of_grades += 1
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the grade of the \'Science\' signature of student # {counter}: ')
        user_input = validate_grade(user_input)
        single_student_dict['science_grade'] = user_input
        total_grade += user_input
        num_of_grades += 1
        average_grade = round(total_grade/num_of_grades) 
        single_student_dict['average_grade'] = average_grade
        list_of_student_data_dicts.append(single_student_dict)
        user_input = input(f'-I-(actions.py:get_students_from_user): Do you want to provide another student? (Y/N) ')
        user_input = validate_Y_N_question(user_input)
        if (user_input == "N"):
            end_of_user_inputs_flag = 1
        else:
            counter += 1
    return list_of_student_data_dicts


def print_all_students_data(list_of_student_data_dicts):
    # Extract the keys (column names) from the first dictionary
    headers = list_of_student_data_dicts[0].keys()
    
    # Calculate the width of each column
    col_widths = {header: max(len(header), max(len(str(row[header])) for row in list_of_student_data_dicts)) for header in headers}
    
    # Print the header row
    header_row = " | ".join(f"{header:<{col_widths[header]}}" for header in headers)
    print(header_row)
    print("-" * len(header_row))
    
    # Print each row of list_of_student_data_dicts
    for row in list_of_student_data_dicts:
        print(" | ".join(f"{str(row[header]):<{col_widths[header]}}" for header in headers))
    print("\n")


def print_top_3_students(list_of_student_data_dicts):
    sorted_list_of_student_data_dicts = sorted(list_of_student_data_dicts, key=lambda x:x['average_grade'], reverse=True)
    list_of_top_3_students_data_dicts = sorted_list_of_student_data_dicts[:3]
    counter = 1
    for student_dict in list_of_top_3_students_data_dicts:
        print(f'-I-(actions.py:print_top_3_students): Top {counter} student: {student_dict['name']} -average grade {student_dict['average_grade']}-')
    print("\n")


def print_average_of_all_students(list_of_student_data_dicts):
    total_grades = 0
    counter = 0
    for student_dict in list_of_student_data_dicts:
        total_grades += student_dict['average_grade']
        counter += 1
    total_average = round(total_grades/counter,3)
    print(f'-I-(actions.py:print_average_of_all_students): The total grades average for all the students is: {total_average}')
    print("\n")