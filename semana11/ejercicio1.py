class Circle:

    def __init__(self, radius):
        self.radius = radius

    def GetArea(self):
        area = 3.14 * self.radius ** 2
        print(f'El area del circulo es {area}.')

my_circule = Circle(5)
my_circule.GetArea()