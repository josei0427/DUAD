from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circule(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        perimeter = 3.14 * 2 * self.radius
        print(F'El perimetro del circulo es de: {perimeter}')

    def calculate_area(self):
        area = 3.14 * self.radius ** 2
        print(F'El area del circulo es de: {area}')


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        perimeter = self.side * 4
        print(F'El perimetro del cuadrado es de: {perimeter}')

    def calculate_area(self):
        area = self.side * self.side
        print(F'El area del cuadrado es de: {area}')


class Rectangle(Shape):
    def __init__(self, side, width ):
        self.side = side
        self.width = width
    
    def calculate_perimeter(self):
        perimeter = 2 * self.side + 2 * self.width
        print(F'El perimetro del rectangulo es de: {perimeter}')


    def calculate_area(self):
        area = self.side * self.width
        print(F'El area del rectangulo es de: {area}')


circule = Circule(4)
circule.calculate_perimeter()
circule.calculate_area()

square = Square(6)
square.calculate_perimeter()
square.calculate_area()

rectangle = Rectangle(8, 2)
rectangle.calculate_perimeter()
rectangle.calculate_area()