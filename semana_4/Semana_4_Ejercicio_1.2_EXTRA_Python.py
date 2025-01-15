"""2. Cree un pseudocódigo que le pida un `tiempo en segundos` al usuario y calcule si
 es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para
 llegar a 10 minutos. Si es mayor, muestre “*Mayor*”"""

tiempo_usuario = int(input("Cual es el tiempo en segundos a consultar? : "))
tiempo_referencia = 10*60
if (tiempo_usuario > tiempo_referencia):
    resultado = "*Mayor*"
else:
    resultado = tiempo_referencia - tiempo_usuario
print(f'{str(resultado)}')