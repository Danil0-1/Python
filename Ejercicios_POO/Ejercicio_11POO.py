class Jugador():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__vida = 100
    
    def recibir_daño(self,cantidad):
        self.__vida -= cantidad
        if self.__vida < 0:
             self.__vida = 0

    def curar(self,cantidad):
        self.__vida += cantidad
        if self.__vida > 100:
             self.__vida = 100


    def ver_estado(self):
        print(f"La vida de {self.__nombre} es de {self.__vida}")    

player = Jugador("Danilo")
player.recibir_daño(30)
player.curar(10)
player.ver_estado()