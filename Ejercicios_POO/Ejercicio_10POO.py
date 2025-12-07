class CajaFuerte():
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__dinero = 0
    
    def depositar(self,cantidad):
        self.__dinero += cantidad
        
    def retirar(self, cantidad, codigo):
        if codigo !=self.__codigo:
            print("Codigo Incorrecto")
            return
        
        if cantidad > self.__dinero:
            print("No tienes suficiente dinero")
            return
        
        self.__dinero -= cantidad
        
    def ver_dinero(self, codigo):
        if codigo !=self.__codigo:
            print("Codigo Incorrecto")
            return   
        else:
            print(f"Tiene un saldo de {self.__dinero}")

caja = CajaFuerte(1234)
caja.depositar(500)
caja.retirar(100, 9999)  
caja.ver_dinero(1234)    
