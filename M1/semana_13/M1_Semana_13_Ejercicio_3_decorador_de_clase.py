"""3. Cree una clase de `User` que:
    - Tenga un atributo de `date_of_birth`.
    - Tenga un property de `age`.
    
    Luego cree un decorador para funciones que acepten un `User` como parámetro que se encargue de revisar 
    si el `User` es mayor de edad y arroje una excepción de no ser así."""


from datetime import date


class AgeLessThan18Exception(Exception):
    "Will raise an error if a provided age is less than 18."
    pass


def decorator_validate_age(func):
    def wrapper(*args):
        acceptable_age = 18
        user = func(*args) 
        try: 
            if (user.age < acceptable_age):
                raise AgeLessThan18Exception
        except:
            print(f'-E-(decorator_validate_age): Provided invalid age {user.age}. Only ages >={acceptable_age} are acceptable.')
        else:
            print(f'-I-(decorator_validate_age): Provided valid age: {user.age}')
        return user 
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

#@decorator_validate_age 
def access_restricted_area(user):
    if (user.age) > 18:
        print(f'-I-(access_restricted_area): User age is valid: {user.age}')   
    else: 
        print(f'-E-(access_restricted_area): User age is NOT valid: {user.age} must be >= 18.')   


good_user = User(date(1990, 1, 1))
#access_restricted_area(good_user)

bad_user = User(date(2020, 1, 1))
#access_restricted_area(good_user)