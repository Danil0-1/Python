class Auto():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        print(f"el auto {self.marca} {self.modelo} esta encendido.")

carro =Auto("BMW", 17)
carro.arrancar()