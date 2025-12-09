class Estudiante():
    def __init__(self, nombre, edad , grado):
        self.nombre= nombre
        self.edad= edad        
        self.grado= grado
    
    def estudiar(self):
        print("Esta estudiando")

nombre = input("Nombre: ")
edad = input("Edad: ")
grado = input("Grado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"Nombre {estudiante.nombre}, Edad {estudiante.edad}, Grado {estudiante.grado}")

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()