"""4. Cree una función que le de la vuelta a un string y lo retorne.
    a. Esto ya lo hicimos en iterables.
    b. “Hola mundo” → “odnum aloH”"""

def reverse_string(input_string):
    result_string = ""
    for index in range(len(input_string) -1, -1, -1):
        result_string += input_string[index]
    return result_string

input_string = "Hola Mundo"
reversed_string = reverse_string(input_string)
print(reversed_string)