"""Crea un bubble_sort por tu cuenta sin revisar el codigo de la lección."""


import random


def generate_random_numbers_list(size, start, end):
    return [random.randint(start, end) for _ in range(size)]


def my_bubble_sort(input_list):
    input_list_size = len(input_list)
    boundary_index = input_list_size
    for outer_index in range(input_list_size):
        already_sorted_flag = True
        for inner_index in range(0, boundary_index):
            next_index = inner_index + 1
            if 0 <= next_index < input_list_size:
                if input_list[inner_index] > input_list[next_index]:
                    input_list[inner_index], input_list[next_index] = input_list[next_index], input_list[inner_index]
                    already_sorted_flag = False
        if already_sorted_flag is True:
            break
        boundary_index = input_list_size - outer_index - 1


input_list = [-9, 3, 6, -2 , 100, 0]
input_list = generate_random_numbers_list(10, -30, 30)

my_bubble_sort(input_list)
print(input_list)