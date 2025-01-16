"""2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2. Intente accesar a una variable global desde una función y cambiar su valor."""


def ejercicio_2_1():
    var_ejercicio_2_1 = "VARIABLE_LOCAL"

#1. Validacion ejercicio 2.1.
#print(var_ejercicio_2_1)


var_ejercicio_2_2 = "VARIABLE_GLOBAL"
def ejercicio_2_2():
    global var_ejercicio_2_2
    print(f'-I-(ejercicio_2_2): valor de "var_ejercicio_2_2" ANTES de funcion (PRINT_DENTRO_DE_FUNCION): {var_ejercicio_2_2}')
    var_ejercicio_2_2 = "MODIFICADA_DENTRO_DE_FUNCION"
    print(f'-I-(ejercicio_2_2): valor de "var_ejercicio_2_2" DESPUES de funcion (PRINT_DENTRO_DE_FUNCION): {var_ejercicio_2_2}')

#2. Validacion ejercicio 2.2.
print(f'-I-(ejercicio_2_2): valor de "var_ejercicio_2_2" ANTES de funcion (PRINT_FUERA_DE_FUNCION): {var_ejercicio_2_2}')
ejercicio_2_2()
print(f'-I-(ejercicio_2_2): valor de "var_ejercicio_2_2" DESPUES de funcion (PRINT_FUERA_DE_FUNCION): {var_ejercicio_2_2}')