pbi = [
    [2.9, 2.5],
    [3.9, 4.0],
    [0.9, 2.2],
    [1.5, 3.3],
    [1.8, 2.6],
    [1.0, 2.0],
    [2.2, 2.3],
    [4.0, 4.0],
    [2.5, 3.5],
    [3.0, 3.0],
    [-9.5, -8.5]
]

# MODIFICACION
pbi[0][0] = "Hola"

# RECORRER
FILAS = 11
COLUMNAS = 2

for i in range(FILAS):
    for j in range(COLUMNAS):
        print(pbi[i][j], end="  ")
    print()