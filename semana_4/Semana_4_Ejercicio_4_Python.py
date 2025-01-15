# 4. Cree un programa que le pida tres números al usuario y muestre el mayor.
list_numeros_a_evaluar = []
list_numeros_a_evaluar.append(int(input("Por favor ingrese el primer numero: ")))
list_numeros_a_evaluar.append(int(input("Por favor ingrese el segundo numero: ")))
list_numeros_a_evaluar.append(int(input("Por favor ingrese el tercer numero: ")))
list_numeros_ordenados = sorted(list_numeros_a_evaluar, reverse=True)
numero_mayor = list_numeros_ordenados[0]
print(f'El numero mayor es: {numero_mayor}')