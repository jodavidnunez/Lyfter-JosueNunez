"""5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    “I love Nación Sushi” → “There are 3 upper cases and 13 lower cases”"""


def count_lower_and_upper_case_characters(input_string):
    count_upper = 0
    count_lower = 0
    for char in input_string:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
    print(f'There are {count_upper} upper cases and {count_lower} lower cases')


input_string = "I love Nación Sushi"
count_lower_and_upper_case_characters(input_string) 