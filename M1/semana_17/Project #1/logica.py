class Rubro:


    def __init__(self, nombre="", tipo="", categoria="", monto=0):
        self.nombre = nombre
        self.tipo = tipo
        self.categoria = categoria
        self.monto = monto


    def __str__(self):
        return f"{self.nombre} ({self.tipo}): {self.categoria} - ${self.monto:.2f}"


    def validar_rubro(self):
        if not self.nombre:
            return False, "El nombre del rubro no puede estar vacio."
        if self.tipo not in ['Gasto', 'Ingreso']:
            return False, "El tipo debe ser 'Gasto' o 'Ingreso'."
        if not self.categoria:
            return False, "La categoria no puede estar vacia."
        if self.monto <= 0: 
            return False, "El monto debe ser mayor a 0."
        return True, "Rubro valido."
    

    def actualizar_monto(self, nuevo_monto):
        if nuevo_monto > 0:
            old_monto = self.monto
            self.monto = nuevo_monto
            return True, f"Monto actualizado correctamente de '{old_monto}' a '{nuevo_monto}'."
        else:
            return False, f"El monto debe ser mayor a 0."


    def actualizar_categoria(self, nueva_categoria):
        if nueva_categoria:
            old_category = nueva_categoria
            self.categoria = nueva_categoria
            return True, f"Categoria actualizada correctamente de {old_category} a {nueva_categoria}."
        else:
            return False, "La categoria no puede estar vacia."
    

    def es_gasto(self):
        return self.tipo == 'Gasto'


    def es_ingreso(self):
        return self.tipo == 'Ingreso'


def transform_objects_list_to_table_data(data_obj_list):
    return [[obj.categoria, obj.tipo, obj.nombre, obj.monto] for obj in data_obj_list]

"""
obj_list = [Rubro("Comida", "Gasto", "Cena", 30000),
            Rubro("Transporte", "Gasto", "Uber", 5000),
            Rubro("Entretenimiento", "Gasto", "Cine", 15000),
            Rubro("Salario", "Ingreso", "My_company", 1500000),
            Rubro("Web_freelance", "Ingreso", "First_page", 1500000)]


transform_objects_list_to_table_data(obj_list)
"""