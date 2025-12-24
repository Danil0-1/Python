# Ejercicio 5

""" 🧠 Ejercicio 5: Sistema de Usuarios

Vas a crear un sistema donde una plataforma tiene distintos tipos de usuarios:

⭐ 1. Clase base: Usuario

Debe tener:

Atributos privados: __nombre, __correo

Propiedades (@property y setters)

Validar que el correo contenga @

Método info() (será polimórfico)

⭐ 2. Subclases:
👤 UsuarioNormal(Usuario)

Atributo: nivel (ej: "Básico", "Premium")

Método extra: usar_plataforma()

🧑‍💼 Administrador(Usuario)

Atributo: area

Método extra: administrar()

Cada uno debe sobrescribir info() mostrando su información personalizada.

⭐ 3. Clase Plataforma

Debe tener una lista privada: __usuarios

Métodos:

agregar_usuario(usuario)

valida que sea instancia de Usuario

mostrar_usuarios()

llama a info() de cada usuario

(polimorfismo) """

# ---------- CLASE BASE ----------
class Usuario:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.correo = correo   # pasa por el setter
    
    # --- PROPIEDAD NOMBRE (solo lectura) ---
    @property
    def nombre(self):
        return self.__nombre
    
    # --- PROPIEDAD CORREO (lectura y escritura) ---
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, nuevo_correo):
        if "@" not in nuevo_correo:
            raise ValueError("El correo debe contener '@'")
        self.__correo = nuevo_correo

    # Método polimórfico
    def info(self):
        print(f"Usuario: {self.nombre} | Correo: {self.correo}")


# ---------- SUBCLASE 1 ----------
class UsuarioNormal(Usuario):
    def __init__(self, nombre, correo, nivel):
        super().__init__(nombre, correo)
        self.nivel = nivel

    def usar_plataforma(self):
        print(f"{self.nombre} está usando la plataforma en nivel {self.nivel}")

    # Sobrescribe info()
    def info(self):
        print(f"Usuario Normal: {self.nombre} | Email: {self.correo} | Nivel: {self.nivel}")


# ---------- SUBCLASE 2 ----------
class Administrador(Usuario):
    def __init__(self, nombre, correo, area):
        super().__init__(nombre, correo)
        self.area = area

    def administrar(self):
        print(f"{self.nombre} está administrando el área {self.area}")

    # Sobrescribe info()
    def info(self):
        print(f"Administrador: {self.nombre} | Email: {self.correo} | Área: {self.area}")


# ---------- CLASE PLATAFORMA ----------
class Plataforma:
    def __init__(self):
        self.__usuarios = []   # lista privada

    def agregar_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            raise TypeError("Solo se pueden agregar objetos de tipo Usuario")
        self.__usuarios.append(usuario)

    def mostrar_usuarios(self):
        for u in self.__usuarios:
            u.info()  # POLIMORFISMO: Python decide qué info() ejecutar

p = Plataforma()

u1 = UsuarioNormal("Danilo", "danilo@gmail.com", "Premium")
u2 = Administrador("Sara", "sara@empresa.com", "Sistemas")

p.agregar_usuario(u1)
p.agregar_usuario(u2)

p.mostrar_usuarios()
