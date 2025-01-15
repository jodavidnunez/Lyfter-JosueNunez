"""1. Cree un programa que itere e imprima los valores
de dos listas del mismo tamaño al mismo tiempo."""

first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]
for index in range(len(first_list)):
    val_1 = first_list[index]
    val_2 = second_list[index]
    print(f'{val_1} {val_2}')