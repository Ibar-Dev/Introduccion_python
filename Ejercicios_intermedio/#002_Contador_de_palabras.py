# Contador de palabras

def contador_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

cadena = input("Ingrese una cadena de texto: ")
print("Número de palabras:", contador_palabras(cadena))
