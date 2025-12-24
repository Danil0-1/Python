# Ejercicio 4

class Curso:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
    
    def info(self):
        print(f"Nombre :{self.nombre} | Profesor: {self.profesor}")

class CursoPresencial(Curso):
    def __init__(self, nombre, profesor, salon , horario):
        super().__init__(nombre, profesor)
        self.salon = salon
        self.horario = horario
    
    def info(self):
        print(f"Nombre :{self.nombre} | Profesor : {self.profesor} | Salon : {self.salon} | Horario : {self.horario}")

class CursoVirtual(Curso):
    def __init__(self, nombre, profesor, plataforma, enlace):
        super().__init__(nombre, profesor)
        self.plataforma = plataforma
        self.enlace = enlace
    
    def info(self):
        print(f"Nombre :{self.nombre} | Profesor : {self.profesor} | Plataforma : {self.plataforma} | Enlace : {self.enlace} ")

class Academia:
    def __init__(self):
        self.cursos = []
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def mostrar_cursos(self):
        for curso in self.cursos:
            curso.info()

# Crear cursos
c1 = CursoPresencial("Matemáticas", "Danilo Muskus", "Salon 28", "8:28 AM")
c2 = CursoVirtual("Python Básico", "Sara Hernandez", "Zoom", "zoom.com/py")

# Crear academia
academia = Academia()

# Agregar cursos
academia.agregar_curso(c1)
academia.agregar_curso(c2)

# Mostrar info (polimorfismo)
academia.mostrar_cursos()
