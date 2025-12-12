# Este metodo es similar al operador " in "

# Ejemplo :

class Caja:
    def __init__(self):
        self.objetos = []

    def agregar(self, item):
        self.objetos.append(item)

    def __contains__(self, item):
        return item in self.objetos


caja = Caja()
caja.agregar("Lapiz")

print("Lapiz" in caja)   # True
print("Borrador" in caja) # False

# Ejercicio 1 

class AgendaContactos:
    def __init__(self):
        self.__contactos = []
    
    def agregar_contacto(self, nombre):
        self.__contactos.append(nombre)
    
    def __contains__(self, contacto):
        return contacto in self.__contactos

agenda = AgendaContactos()
agenda.agregar_contacto("Danilo")
agenda.agregar_contacto("Sara")

print("Danilo" in agenda)   # True
print("Pedro" in agenda)  # False

# Ejercicio 2 

class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_item(self, nombre, precio ):
        self.__productos.append({"nombre": nombre, "precio": precio})
    
    def __contains__(self, producto):
        return any (p["nombre"] == producto for p in self.__productos)

inv = Inventario()
inv.agregar_item("Pan", 1500)
inv.agregar_item("Leche", 3000)

print("Pan" in inv)     # True
print("Arequipe" in inv) # False

# Ejercicio 3 

class Biblioteca:
    def __init__(self):
        self.__libros = []
    
    def agregar_libro(self, titulo, autor):
        self.__libros.append({"titulo": titulo, "autor": autor})
    
    def __contains__(self, titulo):
        return any (l["titulo"] == titulo for l in self.__libros)

biblioteca = Biblioteca()
biblioteca.agregar_libro("El Principito", "Saint-Exupéry")
biblioteca.agregar_libro("1984", "George Orwell")
print("El Principito" in biblioteca)
print("Harry Potter" in biblioteca)
