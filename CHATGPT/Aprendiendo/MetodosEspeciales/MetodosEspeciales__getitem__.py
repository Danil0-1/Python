# __getitem__ decides qué devolver cuando acceden a tu objeto con corchetes.

# Ejemplo 

class Caja:
    def __init__(self):
        self.objetos = ["lapiz", "borrador", "regla"]
    
    def __getitem__(self, indice):
        return self.objetos[indice]

c = Caja()
print(c[0])
print(c[1])

# Ejercicio 1

class AgendaTelefonica:
    def __init__(self):
        self.__contactos = []
    
    def agregar_contacto(self, nombre):
        self.__contactos.append(nombre)
    
    def __getitem__(self, index):
        return self.__contactos[index]

a = AgendaTelefonica()
a.agregar_contacto("Danilo")
a.agregar_contacto("Sara")

print(a[0])
print(a[1])

# Ejercicio 2

class Supermercado:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, nombre, precio):
        self.__productos.append({"Nombre": nombre, "Precio": precio})
    
    def __getitem__(self, index):
        producto = self.__productos[index]
        return f"{producto['Nombre']} cuesta {producto['Precio']} pesos"
    
s = Supermercado()
s.agregar_producto("Pan", 1700)
s.agregar_producto("Tres Leches", 1500)

print(s[0])
print(s[1])

# Ejercicio 3

class Clase:
    def __init__(self):
        self.__estudiantes = []
    
    def agregar_estudiante(self, nombre, edad):
        self.__estudiantes.append({"nombre": nombre, "edad": edad})

    def __getitem__(self, index):
        estudiante = self.__estudiantes[index]
        return f"Nombre del estudiante : {estudiante['nombre']}"

c = Clase()
c.agregar_estudiante("Danilo", 17)
c.agregar_estudiante("Sara", 18)

print(c[0])   
print(c[1])   

# Ejercicio 4

class Inventario:
    def __init__(self):
        self.__productos = []
    
    def agregar_producto(self, nombre, cantidad, precio):
        self.__productos.append({"Nombre": nombre, "Cantidad": cantidad, "Precio": precio})
    
    def __getitem__(self, index):
        producto = self.__productos[index]
        return f"Producto: {producto['Nombre']} | Cantidad: {producto['Cantidad']} | Precio: {producto['Precio']}"
 
inv = Inventario()
inv.agregar_producto("Pan", 5, 1500)
inv.agregar_producto("Leche", 2, 3000)

print(inv[0])
print(inv[1])

# Ejercicio 5 

class Biblioteca:
    def __init__(self):
        self.__libros = []
    
    def agregar_libro(self, titulo, autor, año):
        self.__libros.append({"Titulo": titulo, "Autor": autor, "Año": año})
    
    def __getitem__(self, index):
        if index < 0 or index >= len(self.__libros):
            return "Índice inválido"
        
        libro = self.__libros[index]
        return f"Titulo: {libro['Titulo']} | Autor: {libro['Autor']} Año: {libro['Año']}"
    
b = Biblioteca()
b.agregar_libro("La Divina Comedia", "Dante", 1900)
b.agregar_libro("Sara", "Sara", 2028)
print(b[0])
print(b[1])