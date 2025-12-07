class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        print(self.base * self.altura)

cuadrado = Rectangulo(11, 10)
cuadrado.area()