# Encapsulamiento básico

class Banco : 
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__dinero = 0
    
    def depositar(self, cantidad):
        self.__dinero += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__dinero:
            self.__dinero -= cantidad
        else:
            print("Saldo insuficiente")
    
    def ver_dinero(self):
        print(f"{self.__nombre} tiene una cantidad de dinero de {self.__dinero}")

tarjeta = Banco("Danilo")
tarjeta.depositar(100)
tarjeta.retirar(20)
tarjeta.ver_dinero()