"""Modifica el bubble_sort para que funciones de derecha a izquierda, ordenado los números menores primero."""


def my_bubble_sort(input_list):
    input_list_size = len(input_list)
    boundary_index = 0
    for outer_index in range(input_list_size):
        already_sorted_flag = True
        for inner_index in range(boundary_index, input_list_size):
            prev_index = inner_index - 1
            if 0 <= prev_index < input_list_size:
                if input_list[inner_index] < input_list[prev_index]:
                    input_list[prev_index], input_list[inner_index] = input_list[inner_index], input_list[prev_index]
                    already_sorted_flag = False
        if already_sorted_flag is True:
            break
        boundary_index = outer_index + 1


input_list = [-9, 3, 6, -2 , 100, 0]

my_bubble_sort(input_list)
print(input_list)