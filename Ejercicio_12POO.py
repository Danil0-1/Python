class Producto():
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
    
    def ver_precio(self):
        print(f"El nombre del producto es {self.__nombre} y su precio es {self.__precio}")

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            print("Precio inválido")
            return
    
        self.__precio = nuevo_precio


p1 = Producto("Laptop", 2000)
p1.ver_precio()
p1.cambiar_precio(-50)   
p1.ver_precio()
