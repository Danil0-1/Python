class vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def encender(self):
        print("Esta encendido")

class carro(vehiculo):
    def __init__(self, marca, velocidad):
        super().__init__(marca)
        self.velocidad = velocidad
    
    def tocar_bocina(self):
        print("¡BEEP BEEP!")

mi_carro = carro("BMW", 100)    
mi_carro.encender()
mi_carro.tocar_bocina()