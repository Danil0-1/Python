# Composicion , Objetos dentro de objetos

class Libro ():
    def __init__(self, titulo, autor ):
        self.__titulo = titulo
        self.__autor = autor

    def info(self):
        print(f"Título: {self.__titulo} | Autor: {self.__autor}")

class Biblioteca():
    def __init__(self):
        self.__libros = []

    def agregar_libro(self, libro):
        self.__libros.append(libro)
    
    def mostrar_libros(self):
        if len(self.__libros) == 0:
            print("La biblioteca está vacía.")
            return
        
        for libro in self.__libros:
            libro.info()

l1 = Libro("El principito", "Antoine")
l2 = Libro("IT", "Stephen King")

b = Biblioteca()
b.agregar_libro(l1)
b.agregar_libro(l2)

b.mostrar_libros()
