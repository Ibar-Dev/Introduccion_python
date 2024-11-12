# Calculadora de interés compuesto

# Ejercicio
def interes_compuesto(pv, tasa, n):
    return pv * (1 + tasa)**n

valor_presente = float(input("Ingrese el valor presente: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (en decimal): "))
años = int(input("Ingrese el número de años: "))

valor_futuro = interes_compuesto(valor_presente, tasa_interes, años)
print("El valor futuro de la inversión es:", valor_futuro)
