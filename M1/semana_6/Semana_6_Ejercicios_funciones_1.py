"""1. Cree dos funciones que impriman dos cosas distintas, 
y haga que la primera llame la segunda."""


def sumar_cuadrados(c1, c2):
    resultado = (c1**2) + (c2**2)
    return resultado


def calcular_hipotenusa(c1, c2):
    hipotenusa = (sumar_cuadrados(c1, c2))**(1/2) 
    return hipotenusa


cateto_1 = 2
cateto_2 = 3
hipotenusa = round(calcular_hipotenusa(cateto_1, cateto_2), 3)
print(f'Si "C1 = {cateto_1}" y "C2 = {cateto_2}", H = {hipotenusa}' )