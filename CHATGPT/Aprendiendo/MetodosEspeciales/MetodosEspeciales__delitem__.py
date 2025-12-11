# Este método sirve para borrar un elemento usando del objeto[indice].

# Ejemplo

class CarritoCompras:
    def __init__(self):
        self.__producto = []

    def agregar_producto(self, nombre, precio, cantidad):
        self.__producto.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

    def __delitem__(self, index):
        print(f"Eliminando: {self.__producto[index]['nombre']}")
        del self.__producto[index]

    def mostrar(self):
        for p in self.__producto:
            print(f"Producto: {p['nombre']}  | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


# Ejemplo de uso
carrito = CarritoCompras()

carrito.agregar_producto("Mouse", 50, 1)
carrito.agregar_producto("Teclado", 80, 2)
carrito.agregar_producto("Monitor", 400, 1)
carrito.mostrar()

del carrito[1]   # → Eliminando: Teclado

carrito.mostrar()

# Ejercicio 1 

class ListaTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tareas(self, tarea):
        self.__tareas.append({"tarea":tarea})
    
    def __delitem__(self, index):
        print(f"Se elimino la tarea : {self.__tareas[index]['tarea']}")
        del self.__tareas[index]

    def mostrar(self):
        print("Tareas:")
        for i, t in enumerate(self.__tareas, start=1):
            print(f"{i}. {t['tarea']}")

lt = ListaTareas()
lt.agregar_tareas("Python")
lt.agregar_tareas("JavaScript")
lt.agregar_tareas("Salir a caminar")
lt.mostrar()
del lt[2]
lt.mostrar()