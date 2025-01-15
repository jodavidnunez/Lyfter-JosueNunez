# 2. Cree un programa que le pida al usuario su nombre, apellido, y edad, 
# y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.

# 1. Inicializacion de variables
parametro_bebe = 3
parametro_nino = 10
parametro_preadolecente = 14
parametro_adolecente = 18
parametro_adulto_joven = 30
parametro_adulto = 65
respuesta = ""
parametro_escogido = ""
categoria = ""

# 2. Solicitud de entradas al usuario
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
edad = int(input("Ingrese su edad: "))

# 3. Evaluacion de las entradas
if (edad <= parametro_bebe):
    categoria = "bebe"
    parametro_escogido = f'Edad <= {parametro_bebe} años'
elif (edad <= parametro_nino):
    categoria = "nino"
    parametro_escogido = f'Edad <= {parametro_nino} años'
elif (edad <= parametro_preadolecente):
    categoria = "preadolecente"
    parametro_escogido = f'Edad <= {parametro_preadolecente} años'
elif (edad <= parametro_adolecente):
    categoria = "adolecente"
    parametro_escogido = f'Edad <= {parametro_adolecente} años'
elif (edad <= parametro_adulto_joven):
    categoria = "adulto_joven"
    parametro_escogido = f'Edad <= {parametro_adulto_joven} años'
elif (edad <= parametro_adulto):
    categoria = "adulto"
    parametro_escogido = f'Edad <= {parametro_adulto} años'
else:
    categoria = "adulto_mayor"
    parametro_escogido = f'Edad > {parametro_adulto} años'

# 4. Imprimir resultado de la evaluacion
respuesta = f'La persona \'{nombre} {apellido}\' se clasifica como \'{categoria}\''
respuesta = f'{respuesta} deacuerdo al parametro {parametro_escogido}'
print(respuesta)