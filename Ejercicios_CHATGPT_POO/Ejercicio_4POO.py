import math

class Circulo :
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        print(math.pi * self.radio ** 2)

llanta = Circulo(20)
llanta.area()