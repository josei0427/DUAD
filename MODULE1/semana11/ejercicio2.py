class Person():
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name


class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) == self.max_passengers:
            print(f'Ya hay {self.max_passengers} pasajeros abordo, no pueden subir mas!')
        else: 
            self.passengers.append(person)
            print(f'El pasajero {person} se ha subido al bus.')

    
    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f'El pasajero {person} se ha bajado del bus.')
        else:
            print(f'El pasajero {person} no está en el bus.')


the_bus = Bus(6)

person_1 = Person("Joey")
person_2 = Person("Rachel")
person_3 = Person("Monica")
person_4 = Person("Ross")
person_5 = Person("Phoebe")
person_6 = Person("Chandler")
person_7 = Person("Gunther")

the_bus.add_passenger(person_1)
the_bus.add_passenger(person_2)
the_bus.add_passenger(person_3)
the_bus.add_passenger(person_4)
the_bus.add_passenger(person_5)
the_bus.add_passenger(person_6)
the_bus.add_passenger(person_7)

the_bus.remove_passenger(person_4)
the_bus.remove_passenger(person_3)