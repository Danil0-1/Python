class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

class Alumno(Persona):
    def __init__(self, nombre, edad, ciudad):
        super().__init__(nombre, edad, ciudad)
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} tengo {self.edad} anios y soy de {self.ciudad}")

danilo= Alumno("Danilo", 17, "Bucaramanga")
danilo.presentarse()