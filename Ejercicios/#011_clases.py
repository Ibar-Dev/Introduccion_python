class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def obtener_nombre(self):
        return self.nombre

    def actualizar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def obtener_edad(self):
        return self.edad
