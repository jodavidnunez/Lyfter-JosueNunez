"""Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. 
El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora 
de hacer la operación."""


def suma(num_1, num_2):
    result = round((num_1+num_2), 3)
    print(f'-I-(suma-resultado): {result}')
    return result


def resta(num_1, num_2):
    result = round((num_1-num_2), 3)
    print(f'-I-(resta-resultado): {result}')
    return result


def multiplicacion(num_1, num_2):
    result = round((num_1*num_2), 3)
    print(f'-I-(multiplicacion-resultado): {result}')
    return result


def division(num_1, num_2):
    try:
        result = round((num_1/num_2), 3)
    except ZeroDivisionError:
        print(f'-E-(calculadora): La division entre cero no es una operacion matematica valida.')
        print(f'-I-(calculadora): Por favor vuelva a correr el programa utilizando un divisor diferente de cero.')
        exit(1)
    print(f'-I-(division-resultado): {result}')
    return result


def recolectar_entradas(num_1 = "NEED_TO_ASK_FOR_IT"):
    entradas = []
    if (num_1 == "NEED_TO_ASK_FOR_IT"):
        num_1 = input("-I-(calculadora): Introduzca el primer numero: ")
    operacion = input("-I-(calculadora): Seleccione la operacion a ejecutar: \n\
                1. Suma \n\
                2. Resta \n\
                3. Multiplicacion \n\
                4. Division \n\
                5. Reset \n\
                6. Salir del programa \n")
    if (operacion == "5"):
        return(operacion)
    elif (operacion == "6"):
        return(operacion)
    else:
        num_2 = input("-I-(calculadora): Introduzca el segundo numero: ")
        entradas.append(operacion)
        entradas.append(num_1)
        entradas.append(num_2)
    return entradas


def validacion_de_entradas(operacion, num_1, num_2):
    try:
        num_1 = int(num_1)
        operacion = int(operacion)
        num_2 = int(num_2)
    except ValueError:
        print(f'-E-(calculadora): Todos los parametros de la funcion \'calculadora\' deben ser numeros enteros')
        print(f'-E-(calculadora): Por favor revise sus entradas:\n num_1 -> \'{num_1}\' \n operacion -> \'{operacion}\' \n num_2 -> \'{num_2}\'')
        print(f'-I-(calculadora): Por favor vuelva a correr el programa usando solamente numeros enteros como entradas.')
        exit(1)
    
    class RangoInvalidoDeOpccionesDeMenu(Exception):
        "Se dispara si el usuario al momento de escoger la operacion provee un numero menor a 1 o mayor a 6"
        pass
    try:
        if (operacion < 1 or operacion > 6):
            raise RangoInvalidoDeOpccionesDeMenu
    except RangoInvalidoDeOpccionesDeMenu:
        print(f'-E-(calculadora): Todas las operaciones posibles de la funcion \'calculadora\' son numeros enteros en el rango 1-6.')
        print(f'-I-(calculadora): Por favor vuelva a correr el programa seleccionando una operacion valida.')
        exit(1)
    return operacion, num_1, num_2


def calculadora():
    entradas = recolectar_entradas()
    operacion = entradas[0]
    while (operacion != "6"):
        if (operacion == "5"):
            entradas = recolectar_entradas()
            operacion = entradas[0]
        elif (operacion != "6"):
            num_1 = entradas[1]
            num_2 = entradas[2]
            operacion, num_1, num_2 = validacion_de_entradas(operacion,num_1,num_2)
            if (operacion == 1):
                num_1 = suma(num_1, num_2)
            elif (operacion == 2):
                num_1 = resta(num_1, num_2)
            elif (operacion == 3):
                num_1 = multiplicacion(num_1, num_2)
            elif (operacion == 4):
                num_1 = division(num_1, num_2) 
            elif (operacion == 5):
                print(f'-I-(calculadora): Reset requested by user.')
                num_1 = "NEED_TO_ASK_FOR_IT"
            entradas = recolectar_entradas(num_1)
            operacion = entradas[0]

try:
    calculadora()
except KeyboardInterrupt:
    print(f'\n-E-(calculadora): Programa interrumpido manualmente por el usuario.')