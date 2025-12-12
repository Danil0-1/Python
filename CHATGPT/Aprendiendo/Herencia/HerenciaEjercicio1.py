# Ejercicio 1

class Vehiculos:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    def arrancar(self):
        print(f"Carro con marca : {self.__marca} | Modelo : {self.__modelo} esta arrancando")

class Carro(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def tocar_bocina(self):
        print("BIP BIP")

c = Carro("BMW", "M3104")
c.arrancar()
c.tocar_bocina()