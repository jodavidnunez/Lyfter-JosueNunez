"""Cree un diagrama de flujo que le pida n números al usuario y
 muestre el mayor de todos.
 Ejemplos:
 4, 76, 43, 6, 8 → 76"""

total_de_numeros = int(input("Por favor provea el numero total de numeros a ingresar: "))
contador = 1
numero_mayor = 0
while (contador <= total_de_numeros):
    numero = int(input("Por favor ingrese el siguiente numero: "))
    if(numero > numero_mayor):
        numero_mayor = numero
    contador += 1
print(f'{numero_mayor}')
