# Creación de diccionarios
persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Acceso a elementos del diccionario
nombre = persona["nombre"]
edad = persona.get("edad")

# Modificación de diccionarios
persona["edad"] = 26
persona["profesion"] = "Ingeniero"

# Métodos de diccionario
claves = persona.keys()
valores = persona.values()
