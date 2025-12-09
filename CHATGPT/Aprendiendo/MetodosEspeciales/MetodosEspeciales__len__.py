# __len__ método especial que le dice a Python cómo calcular la longitud de tu objeto.

# Ejemplo

class Playlist:
    def __init__(self, canciones):
        self.canciones = canciones
    
    def __len__(self):
        return len(self.canciones)

p = Playlist(["A", "B", "C"])
print(len(p))  # 3

# Ejercicio 1

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def info(self):
        print("Lista de libros:")
        for libro in self.libros:
            print(f"- {libro}")

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def __len__(self):
        return len(self.libros)

b = Biblioteca()
b.agregar_libro("La Ciencia del Amor")
b.agregar_libro("La Divina Comedia")
b.agregar_libro("Harry Poter ")
b.info()
print(len(b))

# Ejercicio 2 

class Playlist:
    def __init__(self):
        self.__canciones = []
    
    def agregar_canciones(self, cancion):
        self.__canciones.append(cancion)
    
    def mostrar_canciones(self):
        if len(self.__canciones) == 0:
            print("Playlist Vacia")
            return
        
        print("Lista de Canciones")
        for cancion in self.__canciones:
            print(f"- {cancion}") 
    
    def __len__(self):
        return len(self.__canciones)

p = Playlist()
p.agregar_canciones("True Love")
p.agregar_canciones("Sexto Sentido")
p.mostrar_canciones()
print(len(p))

# Ejercicio 3 

class ListaTareas:
    def __init__(self):
        self.__tareas = []
    
    def agregar_tareas(self, tarea):
        self.__tareas.append(tarea)

    def mostrar_tareas(self):
        print("Lista de Tareas:")
        if len(self.__tareas) == 0 :
            print("No hay tareas")
            return

        for tareas in self.__tareas:
            print(f"- {tareas}")
    
    def __len__(self):
        return len(self.__tareas)

t = ListaTareas()
t.agregar_tareas("Aprender Python")
t.agregar_tareas("Comer")
t.agregar_tareas("Salir")
t.mostrar_tareas()
print(len(t))