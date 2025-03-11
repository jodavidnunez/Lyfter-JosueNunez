"""Cree unit tests para probar 3 casos de éxito distintos de cada uno de los ejercicios de semana 6 (exceptuando el 1 y 2)."""

import unittest
from M1_Semana_16_Ejercicios_de_unit_testing_2 import (
    add_up_list_elements,
    reverse_string,
    count_lower_and_upper_case_characters,
    get_sorted_string,
    get_prime_numbers_list
)



class TestAddUpListElements(unittest.TestCase):


    def test_add_up_list_elements_small_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [4444, 0, -99 , 7, 3, -1000]
        
        # Act: Ejecutar la función a probar
        actual_result = add_up_list_elements(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = 3355
        self.assertEqual(actual_result, expected_result)


    def test_add_up_list_elements_big_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [-48, -43, -42, -54, -1, 92, 62, 99, -91, 70, 40, -16, 55, -80, 
                        -57, 2, -21, -73, 27, -79, 58, -92, 6, 64, -38, -6, 67, 75, -76, 
                        -85, -28, -93, 76, -65, 39, -68, 57, -7, -86, -24, 94, 17, -44, 
                        56, -94, -15, 10, -35, 21, 15, -39, -47, 43, -17, -13, 30, 52, 
                        -82, -66, 8, -81, 37, 69, -37, -75, 44, 74, 96, -52, -33, -69, 
                        26, -50, 9, -59, -100, -14, 100, 36, 18, 81, 16, 90, -10, 66, 
                        -18, -64, 45, 84, 38, 28, -90, 73, -58, 86, -11, 54, 63, -46, 144]
    
        # Act: Ejecutar la función a probar
        actual_result = add_up_list_elements(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = 20
        self.assertEqual(actual_result, expected_result)


    def test_add_up_list_elements_input_is_an_empty_list(self):
        # Arrange: Preparamos los datos de entrada
    
        # Act: Ejecutar la función a probar
        input_list = []
        with self.assertRaises(ValueError) as context: 
            add_up_list_elements(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "List is empty"
        self.assertEqual(str(context.exception), expected_result)



class TestReverseString(unittest.TestCase):


    def test_reverse_string_small_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = "Josue David Nunez Elizondo"
        
        # Act: Ejecutar la función a probar
        actual_result = reverse_string(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "odnozilE zenuN divaD eusoJ"
        self.assertEqual(actual_result, expected_result)


    def test_reverse_string_big_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = "A10B12C13D14e15f16g17h18i19J20K21L22M23n24ñ25o26p27Q28R29S30T31U32v33w34x35y36ZJOSUEdavidNUNEZelizondoSANTIAGOnunezPEREZgriseldaMariaPerez" 
        # Act: Ejecutar la función a probar
        actual_result = reverse_string(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "zerePairaMadlesirgZEREPzenunOGAITNASodnozileZENUNdivadEUSOJZ63y53x43w33v23U13T03S92R82Q72p62o52ñ42n32M22L12K02J91i81h71g61f51e41D31C21B01A"
        self.assertEqual(actual_result, expected_result)


    def test_reverse_string_input_is_an_empty_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = ""
    
        # Act: Ejecutar la función a probar
        with self.assertRaises(ValueError) as context: 
            reverse_string(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "String is empty"
        self.assertEqual(str(context.exception), expected_result)



class TestCountLowerAndUpperCaseCharacters(unittest.TestCase):


    def test_count_lower_and_upper_case_characters_small_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = "Josue David Nunez Elizondo"
        
        # Act: Ejecutar la función a probar
        actual_result = count_lower_and_upper_case_characters(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "There are 4 upper cases and 19 lower cases"
        self.assertEqual(actual_result, expected_result)


    def test_count_lower_and_upper_case_characters_big_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = "A10B12C13D14e15f16g17h18i19J20K21L22M23n24ñ25o26p27Q28R29S30T31U32v33w34x35y36ZJOSUEdavidNUNEZelizondoSANTIAGOnunezPEREZgriseldaMariaPerez" 
        
        # Act: Ejecutar la función a probar
        actual_result = count_lower_and_upper_case_characters(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "There are 39 upper cases and 47 lower cases"
        self.assertEqual(actual_result, expected_result)


    def test_count_lower_and_upper_case_characters_input_is_an_empty_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = ""
    
        # Act: Ejecutar la función a probar
        with self.assertRaises(ValueError) as context: 
            count_lower_and_upper_case_characters(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "String is empty"
        self.assertEqual(str(context.exception), expected_result)



class TestGetSortedString(unittest.TestCase):


    def test_get_sorted_string_small_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = "Josue-David-Nunez-Elizondo"
        
        # Act: Ejecutar la función a probar
        actual_result = get_sorted_string(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "David-Elizondo-Josue-Nunez"
        self.assertEqual(actual_result, expected_result)


    def test_get_sorted_string_big_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = "A10B-12C1-3D14-e15f1-6g17-h18i-19J2-0K21-L22M-23n2-4ñ25-o26p2-7Q28-R29S-30T3-1U32-v33w-34x3-5y36-ZJOSUE-david-NUNEZ-elizondo-SANTIAGO-nunez-PEREZ-griselda-Maria-Perez" 
        # Act: Ejecutar la función a probar
        actual_result = get_sorted_string(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "0K21-12C1-19J2-1U32-23n2-30T3-34x3-3D14-4ñ25-5y36-6g17-7Q28-A10B-L22M-Maria-NUNEZ-PEREZ-Perez-R29S-SANTIAGO-ZJOSUE-david-e15f1-elizondo-griselda-h18i-nunez-o26p2-v33w"
        self.assertEqual(actual_result, expected_result)


    def test_get_sorted_string_input_is_an_empty_string(self):
        # Arrange: Preparamos los datos de entrada
        input_string = ""
    
        # Act: Ejecutar la función a probar
        with self.assertRaises(ValueError) as context: 
            get_sorted_string(input_string)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "String is empty"
        self.assertEqual(str(context.exception), expected_result)



class TestGetPrimeNumberList(unittest.TestCase):


    def test_get_prime_numbers_list_small_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [79, 4444, 0, -99 , 7, 3]
        
        # Act: Ejecutar la función a probar
        actual_result = get_prime_numbers_list(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = [79, 7, 3]
        self.assertEqual(actual_result, expected_result)


    def test_get_prime_numbers_list_big_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = [-48, -43, -42, -54, -1, 92, 62, 99, -91, 70, 40, -16, 55, -80, 
                        -57, 2, -21, -73, 27, -79, 58, -92, 6, 64, -38, -6, 67, 75, -76, 
                        -85, -28, -93, 76, -65, 39, -68, 57, -7, -86, -24, 94, 17, -44, 
                        56, -94, -15, 10, -35, 21, 15, -39, -47, 43, -17, -13, 30, 52, 
                        -82, -66, 8, -81, 37, 69, -37, -75, 44, 74, 96, -52, -33, -69, 
                        26, -50, 9, -59, -100, -14, 100, 36, 18, 81, 16, 90, -10, 66, 
                        -18, -64, 45, 84, 38, 28, -90, 73, -58, 86, -11, 54, 63, -46, 144]
    
        # Act: Ejecutar la función a probar
        actual_result = get_prime_numbers_list(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = [2, 67, 17, 43, 37, 73]
        self.assertEqual(actual_result, expected_result)


    def test_get_prime_numbers_list_input_is_an_empty_list(self):
        # Arrange: Preparamos los datos de entrada
        input_list = []
        
        # Act: Ejecutar la función a probar
        with self.assertRaises(ValueError) as context: 
            get_prime_numbers_list(input_list)
        
        # Assert: Verificamos que el actual_result sea el esperado
        expected_result = "List is empty"
        self.assertEqual(str(context.exception), expected_result)



if __name__ == '__main__':
    unittest.main()