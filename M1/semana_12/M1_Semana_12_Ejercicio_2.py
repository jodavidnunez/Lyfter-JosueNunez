"""2. Cree una clase abstracta de `Shape` que:
    a. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
    b. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
    c. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro."""


import math


class Shape():
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = round((math.pi)*((self.radius)**2), 3)    
        print(f'-I-: Circle area for radius = \'{self.radius}\' is: {area}')

    def calculate_perimeter(self):
        perimeter = round(2*(math.pi)*(self.radius), 3)   
        print(f'-I-: Circle perimeter for radius = \'{self.radius}\' is: {perimeter}')


class Parallelograms90DegreesAngles(Shape):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def calculate_area(self):
        return(round((self.side_1)*(self.side_2), 3))    

    def calculate_perimeter(self):
        return(round((2*self.side_1 + 2*self.side_2), 3))


class Square(Parallelograms90DegreesAngles):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
    
    def calculate_area(self):
        area = super().calculate_area()    
        print(f'-I-: Square area for side_1 = \'{self.side_1}\' and side_2 = \'{self.side_2}\' is: {area}')

    def calculate_perimeter(self):
        perimeter = super().calculate_perimeter()
        print(f'-I-: Square perimeter for side_1 = \'{self.side_1}\' and side_2 = \'{self.side_2}\' is: {perimeter}')


class Rectangle(Parallelograms90DegreesAngles):
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2
    
    def calculate_area(self):
        area = super().calculate_area()    
        print(f'-I-: Rectangle area for side_1 = \'{self.side_1}\' and side_2 = \'{self.side_2}\' is: {area}')

    def calculate_perimeter(self):
        perimeter = super().calculate_perimeter()
        print(f'-I-: Rectangle perimeter for side_1 = \'{self.side_1}\' and side_2 = \'{self.side_2}\' is: {perimeter}')


circle_1 = Circle(radius=3)
circle_1.calculate_area()
circle_1.calculate_perimeter()

square_1 = Square(side_1=2,side_2=2)
square_1.calculate_area()
square_1.calculate_perimeter()

rectangle_1 = Rectangle(side_1=2,side_2=3)
rectangle_1.calculate_area()
rectangle_1.calculate_perimeter()