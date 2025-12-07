class Cancion:
    def __init__(self,nombre, autor):
        self.nombre = nombre
        self.autor = autor
        
    def reproducir(self):
        print(f"Reproduciendo: {self.nombre} - {self.autor}")

musica = Cancion("True Love", "Saske")
musica.reproducir()