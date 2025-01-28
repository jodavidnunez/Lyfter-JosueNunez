"""3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar 
    si el `User` es mayor de edad y arroje una excepción de no ser así."""


from datetime import date


class AgeLessThan18Exception(Exception):
    "Will raise an error if a provided lists has non-numeric values"
    pass


def decorator_validate_age(func):
    def wrapper(*args):
        acceptable_age = 18
        age = func(*args) 
        try: 
            if (age.age < acceptable_age):
                raise AgeLessThan18Exception
        except:
            print(f'-E-(decorator_validate_age): Provided invalid age {age.age}. Only ages >={acceptable_age} are acceptable.')
        else:
            print(f'-I-(decorator_validate_age): Provided valid age: {age.age}')
            return age 
    return wrapper


@decorator_validate_age 
class User:    
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    def age(self):
        # Debemos calcular la edad cada vez que la usemos
        # ya que va a variar dependiendo de la fecha actual
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )

good_user = User(date(1990, 1, 1))
bad_user = User(date(2020, 1, 1))