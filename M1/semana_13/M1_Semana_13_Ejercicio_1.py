"""Cree un decorador que haga print de los parámetros y retorno de la función que decore."""


def decorator_print_input_parameters(func):
    def wrapper(parameters):
        print(f'-I-(decorator_print_input_parameters):These are the original input parameters: \n{parameters}\n')
        func_result = func(parameters)
        return func_result
    return wrapper


@decorator_print_input_parameters
def get_sorted_parameters(parameters):
    sorted_parameters = sorted(parameters)
    return sorted_parameters


my_parameters = ["si", "quieres", "puedes", "leer", "esto", "mientras", "tenga", "un", "poco", "de", "sentido", "!"]
my_sorted_parameters = get_sorted_parameters(my_parameters)
print(f'-I-(get_sorted_parameters):These are the sorted parameters: \n{my_sorted_parameters}\n')