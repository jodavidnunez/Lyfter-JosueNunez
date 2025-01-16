"""3. Cree una función que retorne la suma de todos los números de una lista.
    a. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    b. [4, 6, 2, 29] → 41"""


def add_up_list_elements(input_list):
    result = 0
    for elem in input_list:
        result += elem
    return result


input_list = [4, 6, 2, 29] 
result = add_up_list_elements(input_list)
print (result)