# Definición de clase
class Animal:
    # Atributo de clase
    especie = "Animal"

    # Método de clase
    def sonido(self):
        raise NotImplementedError("La subclase debe implementar este método")

# Subclase que hereda de la clase Animal
class Perro(Animal):
    # Atributo de clase
    especie = "Canino"

    # Método de instancia
    def __init__(self, nombre):
        self.nombre = nombre

    # Método de instancia
    def sonido(self):
        return "Guau!"

# Subclase que hereda de la clase Animal
class Gato(Animal):
    # Atributo de clase
    especie = "Felino"

    # Método de instancia
    def __init__(self, nombre):
        self.nombre = nombre

    # Método de instancia
    def sonido(self):
        return "Miau!"

# Instanciación de objetos
perro1 = Perro("Buddy")
gato1 = Gato("Luna")

# Polimorfismo
def hacer_sonar(animal):
    print(animal.sonido())

# Llamada a función con diferentes tipos de objetos
hacer_sonar(perro1)  # Output: Guau!
hacer_sonar(gato1)   # Output: Miau!
