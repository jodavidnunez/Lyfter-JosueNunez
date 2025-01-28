"""Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
y arroje una excepción de no ser así."""


class NonNumericValuesInList(Exception):
    "Will raise an error if a provided lists has non-numeric values"
    pass


def decorator_validate_numbers(func):
    def wrapper(*args):
        for arg_list in (args):
            try:
                all_numbers_chk = all(isinstance(i, (int, float)) for i in arg_list)
                if (all_numbers_chk is False):
                    raise NonNumericValuesInList 
            except NonNumericValuesInList:
                print(f'-E-(decorator_validate_numbers): Non numerical values found on the input list: \n{arg_list}\n')
            else: 
                return func(arg_list)
    return wrapper


@decorator_validate_numbers
def transform_numbers_to_string(numbers_list):
    final_string = "".join(str([num for num in numbers_list]))
    print(f'\n-I-(transform_numbers_to_string): Final string: {final_string}\n')


numbers_list_good = [1, 2, 3, 4, 5, 6, 7, 1.5]
numbers_list_bad = [1, 2, 3, 4, 5, 6, 7, 1.5, "TEST"]
transform_numbers_to_string(numbers_list_good)
transform_numbers_to_string(numbers_list_bad)