"""Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es
 divisible entre 3, “Buzz” si es divisible entre 5, y “FizzBuzz” si es divisible entre
 ambos.
 Ejemplos: 
 33 → Fizz
 25 → Buzz
 30 → FizzBuzz"""

num_usuario = int(input("Ingrese el numero a procesar : "))
res_3 = num_usuario%3
res_5 = num_usuario%5
if (res_3 == 0 and res_5==0):
    result = "FizzBuzz"
elif(res_3 == 0):
    result = "Fizz"
elif(res_5 == 0):
    result = "Buzz"
else: 
    result = ""
print(f'{result}')
