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

# Ejercicio 2 

class RegistroEstudiantes:
    def __init__(self):
        self.__estudiantes = []

    def agregar_estudiante(self, nombre, edad, grado):
        self.__estudiantes.append({"nombre": nombre, "edad": edad, "grado": grado})

    def __delitem__(self, index):
        print(f"Se elimino el estudiante : {self.__estudiantes[index]['nombre']}")
        del self.__estudiantes[index]
    
    def mostrar(self):
        print("Estudiantes: ")
        for i, e in enumerate(self.__estudiantes, start =1):
            print(f"{i}. {e['nombre']} - {e['edad']} - {e['grado']}")

r = RegistroEstudiantes()
r.agregar_estudiante("Sara", 17, "11A")
r.agregar_estudiante("Danilo", 17, "11B")
r.mostrar()

del r[0]
r.mostrar()

# Ejercicio 3

class CarritoCompras:
    def __init__(self):
        self.__productos= []

    def agregar_producto(self, nombre, precio , cantidad):
        self.__productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    
    
    def mostrar(self,):
        print("Productos :")
        for i , p in enumerate(self.__productos, start =1):
            multiplicacion = p['precio'] * p['cantidad']
            print(f"{i}. {p['nombre']} - {p['precio']} x {p['cantidad']} = {multiplicacion} ")
        
    def __delitem__(self, index):
        print(f"Se elimino el producto : {self.__productos[index]['nombre']}")
        del self.__productos[index]
    
cc = CarritoCompras()
cc.agregar_producto("Pan", 1000, 2)
cc.agregar_producto("Pan ochon", 2000, 2)
cc.mostrar()
del cc[0]
cc.mostrar()
