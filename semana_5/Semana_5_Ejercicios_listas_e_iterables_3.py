"""3. Cree un programa que intercambie el primer y ultimo elemento de una lista. 
    Debe funcionar con listas de cualquier tamaño.
    Ejemplos:
    `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`"""

my_list = [4, 3, 6, 1, 7]
first_elem = my_list.pop(0)
last_elem = my_list.pop(-1)
my_list.insert(0, last_elem)
my_list.insert(-1, first_elem)
print(my_list)