"""1. Cree los siguientes unit tests para el algoritmo `bubble_sort`:
    1. Funciona con una lista pequeña.
    2. Funciona con una lista grande (de más de 100 elementos.)
    3. Funciona con una lista vacía.
    4. No funciona con parámetros que no sean una lista."""



import unittest
from M1_Semana_16_Ejercicios_de_unit_testing_1 import my_bubble_sort


class TestMyBubbleSort(unittest.TestCase):

    def test_my_bubble_sort_small_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [44, 0, -99 , 7, 3, -1000]
        
        # Act: Ejecutar la función a probar
        actual_result = my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = [-1000, -99, 0, 3 , 7, 44]
        self.assertEqual(actual_result, expected_result)


    def test_my_bubble_sort_big_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [-48, -43, -42, -54, -1, 92, 62, 99, -91, 70, 40, -16, 55, -80, 
                      -57, 2, -21, -73, 27, -79, 58, -92, 6, 64, -38, -6, 67, 75, -76, 
                      -85, -28, -93, 76, -65, 39, -68, 57, -7, -86, -24, 94, 17, -44, 
                      56, -94, -15, 10, -35, 21, 15, -39, -47, 43, -17, -13, 30, 52, 
                      -82, -66, 8, -81, 37, 69, -37, -75, 44, 74, 96, -52, -33, -69, 
                      26, -50, 9, -59, -100, -14, 100, 36, 18, 81, 16, 90, -10, 66, 
                      -18, -64, 45, 84, 38, 28, -90, 73, -58, 86, -11, 54, 63, -46, 98]
    
        # Act: Ejecutar la función a probar
        #actual_result = my_bubble_sort_old(input_list)
        actual_result = my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = [-100, -94, -93, -92, -91, -90, -86, -85, -82, -81, -80, -79, 
                           -76, -75, -73, -69, -68, -66, -65, -64, -59, -58, -57, -54, 
                           -52, -50, -48, -47, -46, -44, -43, -42, -39, -38, -37, -35, 
                           -33, -28, -24, -21, -18, -17, -16, -15, -14, -13, -11, -10, 
                           -7, -6, -1, 2, 6, 8, 9, 10, 15, 16, 17, 18, 21, 26, 27, 28, 
                           30, 36, 37, 38, 39, 40, 43, 44, 45, 52, 54, 55, 56, 57, 58, 
                           62, 63, 64, 66, 67, 69, 70, 73, 74, 75, 76, 81, 84, 86, 90, 
                           92, 94, 96, 98, 99, 100]
        self.assertEqual(actual_result, expected_result)


    def test_my_bubble_sort_input_is_an_empty_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = []
    
        # Act: Ejecutar la función a probar
        with self.assertRaises(ValueError) as context: 
            my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "List is empty"
        self.assertEqual(str(context.exception), expected_result)


    def test_my_bubble_sort_input_list_is_not_a_dictionary(self):
        # Arrange: Preparamos los datos de entrada
        input_list = {"hola":"adios", "como estas":"bien y vos"}
    
        # Act: Ejecutar la función a probar
        with self.assertRaises(TypeError) as context: 
            my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "Input must be a list"
        self.assertEqual(str(context.exception), expected_result)


    def test_my_bubble_sort_input_list_is_not_a_tuple(self):
        # Arrange: Preparamos los datos de entrada
    
        # Act: Ejecutar la función a probar
        input_list = (44, 0, -99 , 7, 3, -1000)
        with self.assertRaises(TypeError) as context: 
            my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "Input must be a list"
        self.assertEqual(str(context.exception), expected_result)


    def test_my_bubble_sort_input_list_is_not_a_set(self):
        # Arrange: Preparamos los datos de entrada
    
        # Act: Ejecutar la función a probar
        input_list = {1, 100, 1000, 9, 99}
        with self.assertRaises(TypeError) as context: 
            my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "Input must be a list"
        self.assertEqual(str(context.exception), expected_result)


    def test_my_bubble_sort_input_list_is_not_all_numbers(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [-1 , 0, 1, [2, 3]]
    
        # Act: Ejecutar la función a probar
        with self.assertRaises(ValueError) as context: 
            my_bubble_sort(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "List must contain only numbers"
        self.assertEqual(str(context.exception), expected_result)



if __name__ == '__main__':
    unittest.main()