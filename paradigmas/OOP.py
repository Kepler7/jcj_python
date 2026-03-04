# Programación Imperativa

x = 5
y = 3
resultado = x + y
print(resultado)

# Programación Procedimental


def sumar(a, b):
    return a + b


print(sumar(5, 3))


# Programación Orientada a Objetos (POO)
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola soy", self.nombre)


p = Persona("Juan")
p.saludar()

# Programación Funcional
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)


"""
Resumen:
Paradigma	                Idea principal
Imperativo	       ->         Instrucciones paso a paso
Procedimental	     ->       Usar funciones
Orientado a objetos	   ->     Modelar objetos
Funcional	                ->     Usar funciones matemáticas
"""
