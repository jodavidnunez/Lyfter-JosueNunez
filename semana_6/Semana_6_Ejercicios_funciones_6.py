"""6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    a. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    b. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”"""


def get_sorted_string(input_string):
    input_list = input_string.split("-")
    input_list.sort()
    output_string = "-".join(map(str,input_list))
    return output_string


input_string = "python-variable-funcion-computadora-monitor"
output_string = get_sorted_string(input_string)
print(output_string)