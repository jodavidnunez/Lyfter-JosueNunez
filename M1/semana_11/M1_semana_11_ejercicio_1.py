"""1. Cree una clase de `Circle` con:
    a. Un atributo de `radius` (radio).
    b. Un método de `get_area` que retorne su área."""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = round((math.pi)*((self.radius)**2), 3)
        return area

circle_instance = Circle(2)
area = circle_instance.get_area()
print(area)