# Generador de números primos

# Ejercicio
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

limite = int(input("Ingrese un número límite: "))
print("Números primos hasta", limite, ":")
for num in range(2, limite + 1):
    if es_primo(num):
        print(num)
