# Modificar un elemento como si tu clase fuera una lista.

#Ejemplo 

class Agenda:
    def __init__(self):
        self.contactos = ["Juan", "Sara", "Danilo"]

    def __setitem__(self, index, nuevo_nombre):
        self.contactos[index] = nuevo_nombre

    def __getitem__(self, index):
        return self.contactos[index]

a = Agenda()
a[0] = "Santi"   # Cambia Juan → Santi

print(a[1])  # Santi

# Ejercicio 1 

class AgendaTelefonica:
    def __init__(self):
        self.__contactos = []

    def agregar_contactos(self, contacto):
        self.__contactos.append(contacto)
    
    def __setitem__(self, index, nuevo_nombre):
        self.__contactos[index] = nuevo_nombre

    def __getitem__(self, index):
        return self.__contactos[index]

a = AgendaTelefonica()
a.agregar_contactos("Juan")
a.agregar_contactos("Sara")
a.agregar_contactos("Luis")

a[0] = "Danilo"  # Aqui debe cambiar "Juan" por "Danilo"

print(a[0])  
print(a[1])  
print(a[2])

# Ejercicio 2

class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, nombre, precio):
        self.__productos.append({"nombre": nombre, "precio": precio})
    
    def __getitem__(self, index):
        return self.__productos[index]

    def __setitem__(self, index, nuevo_producto):
        self.__productos[index] = nuevo_producto

inv = Inventario()
inv.agregar_producto("Pan", 1500)
inv.agregar_producto("Huevos", 12000)

print(inv[0])    # Debe mostrar el diccionario del Pan

inv[1] = {"nombre": "Leche", "precio": 4000}  # Reemplaza a "Huevos"

print(inv[1])    # Debe mostrar el diccionario de Leche

# Ejercicio 3

class Curso:
    def __init__(self):
        self.__estudiantes = []
    
    def agregar_estudiante(self, nombre, edad):
        self.__estudiantes.append({"nombre": nombre, "edad": edad})

    def __getitem__(self, index):
        estudiante = self.__estudiantes[index]
        return f"Nombre {estudiante['nombre']} | Edad: {estudiante['edad']}"
    
    def __setitem__(self, index, nuevo_estudiante):
        self.__estudiantes[index] = nuevo_estudiante
    
curso = Curso()

curso.agregar_estudiante("Danilo", 17)
curso.agregar_estudiante("Sara", 17)

print(curso[0])  
# → Nombre: Danilo | Edad: 17

curso[0] = {"nombre": "Frijolito", "edad": 18}

print(curso[0])
# → Nombre: Frijolito | Edad: 18
