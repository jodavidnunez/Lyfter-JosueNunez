"""1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
    1. Funciona con una lista pequeña.
    2. Funciona con una lista grande (de más de 100 elementos.)
    3. Funciona con una lista vacía.
    4. No funciona con parámetros que no sean una lista."""



def is_list_all_numbers(input_list):
    return all(isinstance(item, (int, float)) for item in input_list)


def my_bubble_sort(input_list):
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    if len(input_list) == 0:
        raise ValueError("List is empty")
    if is_list_all_numbers(input_list) is False:
        raise ValueError("List must contain only numbers")  
    input_list_size = len(input_list)
    for outer_index in range(input_list_size - 1):
        already_sorted_flag = True
        for inner_index in range(0, input_list_size - 1 - outer_index):
            if input_list[inner_index] > input_list[inner_index + 1]:
                input_list[inner_index], input_list[inner_index + 1] = input_list[inner_index + 1], input_list[inner_index]
                already_sorted_flag = False
        if already_sorted_flag is True:
            break
    return input_list


input_list_1 = [44, 0, -99 , 7, 3, -1000]

sorted_input_list_1 = my_bubble_sort(input_list_1)

print(sorted_input_list_1)