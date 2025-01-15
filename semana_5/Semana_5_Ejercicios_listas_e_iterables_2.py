"""2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    Pista: investigue de que otras maneras se puede usar el `range`.
    Ejemplos:
    `my_string = 'Pizza con piña`"""

my_string = 'Pizza con piña'
range_start = len(my_string) - 1 # Ultimo caracter del string -se le quita 1 porque arranca en 0-
range_stop = -1 # Este es primer caracter del string -indice 0, se le quita 1 porque arranca en 0-
range_step = -1 # Decrementa de derecha a izquierda de un en un caracter
for i in range(range_start, range_stop, range_step):
    print(my_string[i])