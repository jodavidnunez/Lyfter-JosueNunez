"""2. Cree una clase de `Bus` con:
    a. Un atributo de `max_passengers`.
    b. Un método para agregar pasajeros uno por uno (que acepte una instancia de `Person` como parámetro). 
    **Este solo debe agregar pasajeros si lleva menos de su máximo.** Sino, debe mostrar un mensaje de que el bus está lleno.
    c. Un método para bajar pasajeros uno por uno (en cualquier orden)."""

class Person:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
        

class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers_list = []
        self.remaining_seats = max_passengers - len(self.passengers_list)

    def add_one_passenger(self, passenger):
        if(len(self.passengers_list) < self.max_passengers):
            self.passengers_list.append(passenger)
            self.remaining_seats = self.max_passengers - len(self.passengers_list)
            print(f'-I-(Bus.add_one_passenger): New passenger got in the Bus: {passenger.get_name()}')
            print(f'-I-(Bus.add_one_passenger): Number of remaining seats: {self.remaining_seats}')
        else:
            print(f'-E-(Bus.add_one_passenger): {passenger.name} cant get in. Maximum capacity reached: {self.max_passengers}')
    
    def remove_one_passenger(self):
        if(len(self.passengers_list) > 0):
            removed_passenger = self.passengers_list.pop(0)
            self.remaining_seats = self.max_passengers - len(self.passengers_list)
            print(f'-I-(Bus.add_one_passenger): Passenger got off the Bus: {removed_passenger.get_name()}')
            print(f'-I-(Bus.add_one_passenger): Number of remaining seats: {self.remaining_seats}')
        else:
            print(f'-E-(Bus.add_one_passenger): No passengers remain to get off the bus.')

person_1 = Person("Santiago")
person_2 = Person("Griselda")
person_3 = Person("Josue")
bus_1 = Bus(2)
bus_1.add_one_passenger(person_1)
bus_1.add_one_passenger(person_2)
bus_1.add_one_passenger(person_3)
bus_1.remove_one_passenger()
bus_1.remove_one_passenger()
bus_1.remove_one_passenger()