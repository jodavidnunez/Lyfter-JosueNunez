"""Modifica el bubble_sort para que funciones de derecha a izquierda, ordenado los números menores primero."""


def my_bubble_sort_left_to_right(input_list):
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

def my_bubble_sort_right_to_left(input_list):
    input_list_size = len(input_list)
    for outer_index in range(input_list_size):
        already_sorted_flag = True
        for inner_index in range(input_list_size - 1,  outer_index, -1):
            if input_list[inner_index] < input_list[inner_index - 1]:
                input_list[inner_index], input_list[inner_index - 1] = input_list[inner_index - 1], input_list[inner_index]
                already_sorted_flag = False
        if already_sorted_flag is True:
            break
    return input_list

input_list_1 = [1000, -9, 3, 6, -2 , 100, 0, -1000]
input_list_2 = [1000, -9, 3, 6, -2 , 100, 0, -1000]

my_bubble_sort_left_to_right(input_list_1)
my_bubble_sort_right_to_left(input_list_2)

print(input_list_1)
print(input_list_2)