"""4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(my_list) - 1, -1, -1):
    elem = my_list[index]
    res = elem%2
    if (res != 0):
        my_list.pop(index)
print(my_list)