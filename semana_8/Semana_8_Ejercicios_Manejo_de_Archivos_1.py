"""Cree un programa que lea nombres de canciones de un archivo (línea por línea) 
y guarde en otro archivo los mismos nombres ordenados alfabéticamente."""


def obtener_lista_de_canciones_de_archivo(direccion_de_archivo_de_entrada):
    lista_de_canciones_de_archivo = []
    with open(direccion_de_archivo_de_entrada, 'r') as manejador_de_archivo:
        for linea in manejador_de_archivo:
            lista_de_canciones_de_archivo.append(linea)
    return lista_de_canciones_de_archivo


def escribir_lista_de_canciones_ordenadas_en_archivo(lista_de_canciones, direccion_de_archivo_de_salida):
    with open(direccion_de_archivo_de_salida, 'w') as manejador_de_archivo:
        for cancion in sorted(lista_de_canciones):
            manejador_de_archivo.write(cancion)


def principal():
    directorio_de_trabajo = r'C:\Users\jodav\Documents\Curso_Progra_Lyfter\Semana_8\Ejercicios_Manejo_de_archivos'
    archivo_de_entrada = directorio_de_trabajo + "/Canciones_entrada.txt"
    archivo_de_salida  = directorio_de_trabajo + "/Canciones_salida.txt"
    lista_de_canciones_entrada = obtener_lista_de_canciones_de_archivo(archivo_de_entrada)
    escribir_lista_de_canciones_ordenadas_en_archivo(lista_de_canciones_entrada, archivo_de_salida)


if __name__ == "__main__":
    principal()