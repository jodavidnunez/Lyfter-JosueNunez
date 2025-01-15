"""7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    a. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
    b. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, 
    eso no ayudaria.
    c. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). 
    Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*"""

def get_single_prime_number(num):
    result = True
    if (num) <= 1:
        """1. Por definicion, los numeros solo pueden ser primos si son mayores a 1"""
        result = False  
    else:
        """ 2. Con respecto al 'start' de 'range', Inicia en '2' porque es el primer numero entero mayor a 1"""
        range_start = 2 
        """ 3. Con respecto al 'end de 'range'. 'La raiz cuadrada del numero de entrada es el limite a partir del cual los 
        divisores con residuo '0' se empiezan a repetir, por lo tanto, todos los divisores unicos se encuentran en valores 
        iguales o menores a la raiz del numero en cuestion. Ademas, se le suma 1 ya que la funcion 'range' genera un rango 
        por defecto desde 'start' hasta 'stop - 1', y se necesita que el valor de la raiz sea incluido."""
        range_end = int((num)**0.5) + 1
        for i in range(range_start, range_end):
            if (num % i == 0):
                result = False
                break
        return result
    

def get_prime_numbers_list(input_list):
    output_list = []
    for num in input_list:
        if(get_single_prime_number(num) is True):
            output_list.append(num)
    return output_list


input_list = [1, 4, 6, 7, 13, 9, 67]
prime_numbers_list = get_prime_numbers_list(input_list)
print(prime_numbers_list)