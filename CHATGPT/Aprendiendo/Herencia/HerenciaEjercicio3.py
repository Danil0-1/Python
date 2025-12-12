# Ejercicio 3 

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        print(f"Nombre : {self.nombre} | Salario : {self.salario}")

class Obrero(Empleado):
    def __init__(self, nombre, salario, turno):
        super().__init__(nombre, salario)
        self.turno = turno
    
    def trabajar(self):
        print(f"El obrero {self.nombre} esta trabajando en el turno {self.turno}")

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def dirigir(self):
        print(f"El/La gerente {self.nombre} esta dirigiendo el departamento {self.departamento}")

e1 = Obrero("Danilo", 1999, "noche")
e1.mostrar_info()
e1.trabajar()
e2 = Gerente("Sara", 2000, "torre 2")
e2.mostrar_info()
e2.dirigir()