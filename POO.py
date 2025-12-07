class Carro:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
    
    def acelerar(self):
        self.velocidad +=10
        print(self.velocidad)
    def frenar(self):
        self.velocidad -=10
        if self.velocidad < 0:
            self.velocidad = 0
        print(self.velocidad)

mi_carro= Carro("BMW", "16", 100)
mi_carro.acelerar()
mi_carro.acelerar()
mi_carro.frenar()
print(mi_carro.velocidad)
