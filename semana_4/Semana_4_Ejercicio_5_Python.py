"""5. Dada `n` cantidad de notas de un estudiante, calcular:
    1. Cuantas notas tiene aprobadas (mayor a 70).
    2. Cuantas notas tiene desaprobadas (menor a 70).
    3. El promedio de todas.
    4. El promedio de las aprobadas.
    5. El promedio de las desaprobadas."""

valor_total_de_notas = 0
valor_notas_aprobadas = 0
valor_notas_desaprobadas = 0
numero_de_notas_aprobadas = 0
numero_de_notas_desaprobadas = 0
total_de_notas = int(input("Por favor provea el numero total de notas a ingresar: "))
contador = 1
while (contador <= total_de_notas):
    nota = int(input("Por favor ingrese la siguiente nota:  "))
    if(nota < 70):
        valor_notas_desaprobadas += nota
        numero_de_notas_desaprobadas += 1
    else:
        valor_notas_aprobadas += nota
        numero_de_notas_aprobadas += 1
    valor_total_de_notas += nota
    contador += 1
promedio_general = round((valor_total_de_notas/total_de_notas), 2) 
promedio_aprobadas = round((valor_notas_aprobadas/numero_de_notas_aprobadas), 2) 
promedio_desaprobadas = round((valor_notas_desaprobadas/numero_de_notas_desaprobadas), 2)
print(f'1. Numero de notas aprobadas (>=70): {numero_de_notas_aprobadas}') 
print(f'2. Numero de notas desaprobadas (<70): {numero_de_notas_desaprobadas}')
print(f'3. Promedio general: {promedio_general}')
print(f'4. Promedio aprobadas: {promedio_aprobadas}')
print(f'5. Promedio desaprobadas: {promedio_desaprobadas}')  