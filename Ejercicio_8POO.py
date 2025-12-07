class Jugador ():
    def __init__(self, nombre):
        self.nombre = nombre 
        self.vida = 100
        
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
    
    def mostrar_vida(self):
        if self.vida < 0:
             self.vida = 0
        print(f"La vida de {self.nombre} es de {self.vida}")

player = Jugador("Danilo")
player.recibir_daño(20)
player.recibir_daño(30)
player.mostrar_vida()