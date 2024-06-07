# Tupla vacia
# x = ()
# print(x)

# Tupla con elementos - Modo 1
# x = (1, 2, 3, 5, 10, "Hola", 10.4)
# print(x)

# Tupla con elementos - Modo 2
# x = 1, 2, 3, 7
# print(x)

# No esta permitido la modificación porque es INMUTABLE
# tupla = (1, 2, 3)
# tupla[0] = 5 # Error! TypeError

# Acceso
# tupla = 1, 2, ('a', 'b'), 3
# print(tupla)
# print(tupla[2][0])

# Convertir
# lista = [1, 2, 3]
# tupla = tuple(lista)
# print(type(tupla))
# print(tupla)

# Asignación
# l = (1, 2, 3)
# x, y, z = l
# print(x, y, z)

# Recorrido
# tupla = (1, 2, 3)
# for item in tupla:
#     print(item)

# Count - Cuenta la cantidad de registros que tiene el valor en el parametro
# tupla = (1, 1, 1, 4, 5)
# print(tupla.count(1))

# Index
# tupla = (7, 7, 7, 3, 5)
# print(tupla.index(3))
# print(tupla.index(7, 2)) # el segundo parametro indica el indice partir la busqueda