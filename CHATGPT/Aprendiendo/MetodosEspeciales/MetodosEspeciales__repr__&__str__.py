# __repr__ & __str__ , repr es para programadores, str es para el usuario

# Ejercicio 1

class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __repr__(self):
        return f"Producto({self.nombre!r}, {self.precio!r})"
    
    def __str__(self):
        return f"{self.nombre} cuesta {self.precio} pesos"

p = Producto("Pan", 1500)
print(p)
print(repr(p))

# Ejercicio 2

class Cancion():
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion_segundos}s)"
        
    def __repr__(self):
        return f"Cancion({self.titulo!r}, {self.artista!r}, {self.duracion_segundos!r})"
    
c = Cancion("True Love", "Saske", 180)
print(c)
print(repr(c))

# Ejercicio 3

class Punto2D():
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
    
    def __str__(self):
        return f"Punto: ({self.x, self.y})"
    
    def __repr__(self):
        return f"Punto2D({self.x!r}, {self.y!r})"

p = Punto2D(2, 8)
print(p)
print([p])