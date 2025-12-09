class Vehiculo():
    def sonido(self):
        pass

class Carro (Vehiculo):
    def sonido(self):
        return "BIP BIP"
    
class Moto (Vehiculo):
    def sonido(self):
        return "BOP BOP"
    
class Bicicleta (Vehiculo):
    def sonido(self):
        return "BUP BUP"
    
vehiculos = [Carro(), Moto(), Bicicleta()]

for v in vehiculos:
    print(v.sonido())