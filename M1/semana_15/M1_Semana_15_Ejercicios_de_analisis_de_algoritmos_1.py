"""Analice el algoritmo de bubble_sort usando la Big O Notation."""

def my_bubble_sort(input_list):
    input_list_size = len(input_list) # O(1)
    boundary_index = input_list_size  # O(1)
    for outer_index in range(input_list_size): # O(n)
        already_sorted_flag = True # O(1)
        for inner_index in range(0, boundary_index): # O(n^2)
            next_index = inner_index + 1 # O(1)
            if 0 <= next_index < input_list_size: # O(1)
                if input_list[inner_index] > input_list[next_index]: # O(1)
                    input_list[inner_index], input_list[next_index] = input_list[next_index], input_list[inner_index] # O(1)
                    already_sorted_flag = False # O(1)
        if already_sorted_flag is True: # O(1)
            break # O(1)
        boundary_index = input_list_size - outer_index - 1 # O(1)


input_list = [-9, 3, 6, -2 , 100, 0] 

my_bubble_sort(input_list) # O(n^2)
print(input_list)

"""R/ O(n^2)"""