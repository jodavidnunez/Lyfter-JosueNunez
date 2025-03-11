"""Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (exceptuando el 1 y 2)."""



"""3. Cree una función que retorne la suma de todos los números de una lista.
    a. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    b. [4, 6, 2, 29] → 41"""


def is_list_all_numbers(input_list):
    return all(isinstance(item, (int, float)) for item in input_list)


def add_up_list_elements(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if len(input_list) == 0:
        raise ValueError("List is empty")
    if is_list_all_numbers(input_list) is False:
        raise ValueError("List must contain only numbers")  
    result = 0
    for elem in input_list:
        result += elem
    return result

input_list = [4, 6, 2, 29] 
result = add_up_list_elements(input_list)
print (result)



"""4. Cree una función que le de la vuelta a un string y lo retorne.
    a. Esto ya lo hicimos en iterables.
    b. “Hola mundo” → “odnum aloH”"""

def reverse_string(input_string):
    if len(input_string) == 0:
        raise ValueError("String is empty")
    result_string = ""
    for index in range(len(input_string) -1, -1, -1):
        result_string += input_string[index]
    return result_string

input_string = "Hola Mundo"
reversed_string = reverse_string(input_string)
print(reversed_string)



"""5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    “I love Nación Sushi” → “There are 3 upper cases and 13 lower cases”"""


def count_lower_and_upper_case_characters(input_string):
    if len(input_string) == 0:
        raise ValueError("String is empty")
    count_upper = 0
    count_lower = 0
    for char in input_string:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
    return(f'There are {count_upper} upper cases and {count_lower} lower cases')


input_string = "I love Nación Sushi"
text = count_lower_and_upper_case_characters(input_string)
print(text)



"""6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    a. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    b. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”"""


def get_sorted_string(input_string):
    if len(input_string) == 0:
        raise ValueError("String is empty")
    input_list = input_string.split("-")
    input_list.sort()
    output_string = "-".join(map(str,input_list))
    return output_string


input_string = "python-variable-funcion-computadora-monitor"
output_string = get_sorted_string(input_string)
print(output_string)



"""7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    a. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    b. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, 
    eso no ayudaria.
    c. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
    Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*"""

def get_single_prime_number(num):
    result = True
    if (num) <= 1:
        result = False  
    else:
        range_start = 2 
        range_end = int((num)**0.5) + 1
        for i in range(range_start, range_end):
            if (num % i == 0):
                result = False
                break
        return result
    

def get_prime_numbers_list(input_list):
    if len(input_list) == 0:
        raise ValueError("List is empty")
    output_list = []
    for num in input_list:
        if(get_single_prime_number(num) is True):
            output_list.append(num)
    return output_list


input_list = [1, 4, 6, 7, 13, 9, 67]
prime_numbers_list = get_prime_numbers_list(input_list)
print(prime_numbers_list)