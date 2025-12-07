class Cuenta():
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, cantidad):
        self.saldo += cantidad

    def mostar_saldo(self):
        print(f"Saldo actular {self.saldo}")

tarjeta = Cuenta("Danilo")
tarjeta.depositar(10)
tarjeta.depositar(200)
tarjeta.mostar_saldo()