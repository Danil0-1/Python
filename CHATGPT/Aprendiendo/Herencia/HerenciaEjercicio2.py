# Ejercicio 2

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} esta estudiando en el grado : {self.grado}")

p = Estudiante("Danilo", 17, "Once")
p.presentarse()
p.estudiar()