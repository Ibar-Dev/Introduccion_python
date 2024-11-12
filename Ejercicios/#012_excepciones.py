# División por cero
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")

# Conversión de cadena no numérica a entero
try:
    entero = int("abc")
except ValueError:
    print("Error: No se puede convertir la cadena a entero")
