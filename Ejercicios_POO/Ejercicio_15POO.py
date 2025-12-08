class Estudiante():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def info(self):
        print(f"Nombre : {self.__nombre} | Edad : {self.__edad} anios")

class Curso():
    def __init__(self, nombre_del_curso):
        self.__nombre_del_curso = nombre_del_curso
        self.__lista_de_estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.__lista_de_estudiantes.append(estudiante)

    def info(self):
        print(f"Curso: {self.__nombre_del_curso}")

    def mostrar_estudiante(self):
        if len(self.__lista_de_estudiantes) == 0 :
            print("No hay Estudiantes")
            return

        for estudiante in self.__lista_de_estudiantes:
            estudiante.info()

class Escuela():
    def __init__(self, nombre):
        self.__nombre = nombre 
        self.__lista_de_cursos = []
    
    def agregar_curso(self, curso):
        self.__lista_de_cursos.append(curso)
    
    def mostrar_cursos(self):
        if len(self.__lista_de_cursos) == 0 :
            print("No hay Cursos")
            return

        for curso in self.__lista_de_cursos:
            curso.info()
        
    def mostrar_todo(self):
        if len(self.__lista_de_cursos) == 0 :
            print("No hay Cursos")
            return

        for curso in self.__lista_de_cursos:
            curso.info()
            curso.mostrar_estudiante()
            print()

e1 = Estudiante("Danilo", 17)
e2 = Estudiante("Sara", 17)

curso1 = Curso("Matemáticas")
curso1.agregar_estudiante(e1)
curso1.agregar_estudiante(e2)

escuela = Escuela("Campus Code")
escuela.agregar_curso(curso1)

escuela.mostrar_todo()
