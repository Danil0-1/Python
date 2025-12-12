# Herencia

# Herencia Basica

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    pass   # No cambia nada, hereda TODO

p = Perro("Rocky")
p.comer()   # Funciona aunque no está declarado en Perro

# Herencia con métodos propios

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print(f"{self.nombre} está comiendo.")

class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} está ladrando.")

p = Perro("Max")
p.comer()
p.ladrar()

# Sobreescritura de métodos

class Animal:
    def hacer_sonido(self):
        print("Sonido genérico...")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau guau")

p = Perro()
p.hacer_sonido()

# Super() → Llamar al método del Padre

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # trae el atributo nombre
        self.raza = raza

p = Perro("Toby", "Labrador")
print(p.nombre, p.raza)
