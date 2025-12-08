class Producto():
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    def info(self):
        print(f"Nombre del producto {self.__nombre} | Precio : {self.__precio}")

class Tienda(): 
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)
    
    def mostrar_productos(self):
        if len(self.__productos) == 0:
            print("NO HAY PRODUCTOS")
            return

        for producto in self.__productos:
            producto.info()
        
    def total_productos(self):
        print(f"Hay {len(self.__productos)} productos")           

pan = Producto("Pan", 1600)
leche = Producto("leche", 600)
arequipe = Producto("arequipe", 100)

t = Tienda()
t.agregar_producto(pan)
t.agregar_producto(leche)
t.agregar_producto(arequipe)

t.mostrar_productos()
t.total_productos()