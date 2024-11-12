def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: División por cero")
        return None

# Ejemplo de uso
print(dividir(10, 2))  # Output: 5.0
print(dividir(10, 0))  # Output: Error: División por cero
                       #         None
# En este ejemplo, la función dividir(a, b) intenta dividir a por b. Si se produce una excepción ZeroDivisionError (división por cero),
# se maneja con un bloque except, que imprime un mensaje de error y devuelve None.

def leer_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'r')
        contenido = archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
    else:
        print("Contenido del archivo:")
        print(contenido)
    finally:
        if 'archivo' in locals():
            archivo.close()

# Ejemplo de uso
leer_archivo("archivo_existente.txt")  # Output: Contenido del archivo: [contenido del archivo]
leer_archivo("archivo_no_existente.txt")  # Output: Error: El archivo 'archivo_no_existente.txt' no se encontró.

# En este ejemplo, la función leer_archivo(nombre_archivo) intenta abrir un archivo para lectura. 
# Si se produce una excepción FileNotFoundError, se maneja con un bloque except que imprime un mensaje de error. 
# Si no hay excepciones, se ejecuta un bloque else, que imprime el contenido del archivo. Finalmente, 
# se utiliza un bloque finally para cerrar el archivo abierto, independientemente de si ocurrió una excepción o no. 
# Esto garantiza que el archivo se cierre correctamente al finalizar la operación.