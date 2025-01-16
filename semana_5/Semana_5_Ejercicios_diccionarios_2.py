"""2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, 
usando una para sus keys, y la otra para sus values.
    Ejemplos:
    `list_a = ["first_name", "last_name", "role"]`
    `list_b = ["Alek", "Castillo", "Software Engineer"]`
    → `{"first_name": "Alek", "last_name": "Castillo", "role": "Software Engineer"}`"""

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
output_dict = {}
for index in range(len(list_a)):
    elem_a = list_a[index]
    elem_b = list_b[index]
    output_dict[elem_a] = elem_b

import pprint
pprint.pprint(output_dict)
