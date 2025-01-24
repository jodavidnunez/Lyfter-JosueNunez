"""3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar 
    si el `User` es mayor de edad y arroje una excepción de no ser así."""


from datetime import date


def decorator_validate_user_age(func):
    def wrapper(*args):
        age = func(*args)
        if (age < 18):
            raise ValueError(f'-E-(decorator_user_age): User is under 18!')
        return age
    return wrapper


class User:    
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth
    
    @property
    @decorator_validate_user_age 
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
print(f"Age: {good_user.age}")

bad_user = User(date(2020, 1, 1))
print(f"Age: {bad_user.age}")