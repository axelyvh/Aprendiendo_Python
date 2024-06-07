dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# POSITIVOS
print("valor que se encuentra en el indice 1: ", dias[1])
print("valores que se encuentran desde el indice inicial 0 hasta 2", dias[:3])
print("valores que se encuentran desde el indice 3 hasta 6 que es el indice final", dias[3:])
print("valores desde el indice 3 hasta el indice 4", dias[3:5])

# NEGATIVOS
print("valor que se encuentre en el indice ultimo 6: ", dias[-1])
print("valor que se encuentra en el indice ultimo 6: ", dias[-5])
print("valor que se encuentra en el indice 4: ", dias[-3])
print("valores que se encuentran desde el indice 4 hasta 6 que es el indice final: ", dias[-3:])

# UTILIZANDO LEN
print("Cantidad de elementos: ", len(dias))
print(dias[len(dias) - 1])
