# Adivina el número

# Ejercicio
import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        intento = int(input("Adivina el número secreto (entre 1 y 100): "))
        intentos += 1
        if intento < numero_secreto:
            print("Más alto. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("Más bajo. Intenta de nuevo.")
        else:
            print("¡Correcto! El número secreto era", numero_secreto)
            print("¡Lo lograste en", intentos, "intentos!")
            break

adivina_el_numero()
