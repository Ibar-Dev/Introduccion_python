class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Las matrices deben tener la misma dimensión")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    # Implementar __sub__ y __mul__ de manera similar

# Ejemplo de uso:
matriz1 = Matrix(2, 2)
matriz1.data = [[1, 2], [3, 4]]

matriz2 = Matrix(2, 2)
matriz2.data = [[5, 6], [7, 8]]

resultado_suma = matriz1 + matriz2
print("Suma de matrices:")
for row in resultado_suma.data:
    print(row)
