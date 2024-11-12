# Conversor de temperatura

# Ejercicio
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temperatura = float(input("Ingrese una temperatura: "))
print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(temperatura))
print("Temperatura en Celsius:", fahrenheit_a_celsius(temperatura))

