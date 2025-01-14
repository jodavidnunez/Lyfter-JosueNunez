"""Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30, o si los 3
 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
Ejemplos:
 23, 30, 768 → Correcto (hay un 30)
 10, 15, 5 → Correcto (10 + 15 + 5 = 30)
 35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30"""

num_usuario_1 = int(input("Ingrese el primer numero a procesar : "))
num_usuario_2 = int(input("Ingrese el segundo numero a procesar : "))
num_usuario_3 = int(input("Ingrese el tercer numero a procesar : "))
if(num_usuario_1 == 30 or num_usuario_2 == 30 or num_usuario_3 == 30): 
    resultado = "Correcto"
elif(num_usuario_1 + num_usuario_2 + num_usuario_3 == 30):
    resultado = "Correcto"
else:
    resultado = "Incorrecto"
print(f'{resultado}')