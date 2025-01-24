"""Cree un decorador que se encargue de revisar si todos los parámetros de la función que decore son números, 
y arroje una excepción de no ser así."""


def decorator_validate_numbers(func):
    def wrapper(numbers_list):
        all_numbers_chk = all(isinstance(i, (int, float)) for i in numbers_list)
        if (all_numbers_chk is False): 
            raise ValueError(f'-E-(decorator_validate_numbers): Non numerical values found on the input list: \n{numbers_list}\n')
        func(numbers_list)
    return wrapper


@decorator_validate_numbers
def transform_numbers_to_string(numbers_list):
    final_string = "".join(str([num for num in numbers_list]))
    print(f'-I-(transform_numbers_to_string): Final string: {final_string}')


numbers_list_good = [1, 2, 3, 4, 5, 6, 7, 1.5]
numbers_list_bad = [1, 2, 3, 4, 5, 6, 7, 1.5, "TEST"]
transform_numbers_to_string(numbers_list_good)
transform_numbers_to_string(numbers_list_bad)