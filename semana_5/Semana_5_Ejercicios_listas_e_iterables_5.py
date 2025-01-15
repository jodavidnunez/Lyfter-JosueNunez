"""5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó,
 seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [54, 86, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86."""


total_numeros = 10
contador = 1
lista_numeros = []
while (contador <= total_numeros):
    lista_numeros.append(int(input("Por favor ingrese el siguiente numero:  ")))
    contador += 1
num_mayor = max(lista_numeros)
print(f'{str(lista_numeros)}\nEl numero mayor es: {num_mayor}')