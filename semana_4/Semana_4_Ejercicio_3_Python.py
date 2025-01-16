# 3. Cree un programa con un numero secreto del 1 al 10. 
# El programa no debe cerrarse hasta que el usuario adivine el numero.

import random
numero_aleatorio = random.randint(1,10)
numero_usuario = int(input("Cual es el numero?: "))
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Lo siento, no adivinaste! Por favor ingrese un nuevo numero: "))
print(f'Felicidades adivinaste! El numero secreto es {numero_aleatorio}')