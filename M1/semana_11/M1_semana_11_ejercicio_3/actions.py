
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

class Student():
    def __init__(self, attributes_dict):
        self.name = attributes_dict['name']
        self.group = attributes_dict['group']
        self.spanish_grade = attributes_dict['spanish_grade']
        self.english_grade = attributes_dict['english_grade']
        self.social_studies_grade = attributes_dict['social_studies_grade']
        self.science_grade = attributes_dict['science_grade']
        self.average_grade = attributes_dict['average_grade']
        self.attributes_names = ('name', 
                                'group', 
                                'spanish_grade', 
                                'english_grade',
                                'social_studies_grade',
                                'science_grade',
                                'average_grade')              


def get_students_from_user():
    end_of_user_inputs_flag = 0
    counter = 1
    list_of_students = []
    single_student_dict = {}
    while(end_of_user_inputs_flag != 1):
        total_grade = 0
        num_of_grades = 0
        user_input = input(f'-I-(actions.py:get_students_from_user): Please provide the name of student # {counter}: ')
        user_input = validate_name(user_input)
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
        new_student = Student(single_student_dict)
        list_of_students.append(new_student)
        single_student_dict = {}
        user_input = input(f'-I-(actions.py:get_students_from_user): Do you want to provide another student? (Y/N) ')
        user_input = validate_Y_N_question(user_input)
        if (user_input == "N"):
            end_of_user_inputs_flag = 1
        else:
            counter += 1
    return list_of_students


def print_all_students_data(list_of_students):
    # Extract the keys (column names) from the first dictionary
    from tabulate import tabulate
    if(len(list_of_students)):
        import inspect
        test_obj = list_of_students[0]
        """attributes_names = [attr for attr in dir(test_obj) if not callable(getattr(test_obj, attr)) and not attr.startswith("__")]
           headers = sorted(attributes_names)"""
        headers = test_obj.attributes_names
        data_to_extract = []
        for student in list_of_students:
            tmp_list = []
            for header in headers:
                tmp_list.append(getattr(student, str(header)))
            data_to_extract.append(tmp_list)
        print(tabulate(data_to_extract, headers=headers, tablefmt="grid"))
    else:
        print(f'-E-(actions.py:print_all_students_data): No available students data yet. Please introduce manually one or more students, or import a CSV file before running this function.\n')


def print_top_3_students(list_of_students):
    if (len(list_of_students) >= 3):
        sorted_list_of_students = sorted(list_of_students, key=lambda x:x.average_grade, reverse=True)
        list_of_top_3_students = sorted_list_of_students[:3]
        counter = 1
        for student in list_of_top_3_students:
            print(f'-I-(actions.py:print_top_3_students): Top {counter} student: {student.name} -average grade {student.average_grade}-')
            counter += 1
        print("\n")
    else:
        print(f'-E-(actions.py:print_top_3_students): The available data corresponds to less than three students. Please make sure data from at least three students is available (either by manually providing it or by importing a CSV file before running this function).\n')



def print_average_of_all_students(list_of_students):
    if(len(list_of_students)):
        total_grades = 0
        counter = 0
        for student in list_of_students:
            total_grades += student.average_grade
            counter += 1
        total_average = round(total_grades/counter,3)
        print(f'-I-(actions.py:print_average_of_all_students): The total grades average for all the students is: {total_average}')
        print("\n")
    else:
        print(f'-E-(actions.py:print_average_of_all_students): No available students data yet. Please introduce manually one or more students, or import a CSV file before running this function.\n')