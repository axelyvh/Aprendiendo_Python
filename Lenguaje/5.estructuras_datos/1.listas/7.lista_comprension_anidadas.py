# Matriz: Lista de Lista
C = [
    [2, 3, 4],
    [40, 50, 60],
    [100, 200, 300]
]

# Lista por comprension anidad
r1 = [i for item in C for i in item]
print(r1)
print(sum(r1))