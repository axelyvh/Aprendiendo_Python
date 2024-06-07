# Modo 1
# d1 = dict()
# print(d1)

# Modo 2
d2 = {
    "Nombre": "Axel",
    "Edad": 25,
    "Documento": 12345678
}
print(d2)

# Modo 3
# d3 = {
#     "Nombre": "Axel",
#     "Edad": 25,
#     "Documento": 12345678
# }
# print(d3)

# Modo 4
# d4 = dict([
#     ("Nombre", "Axel"),
#     ("Edad", 25),
#     ("Documento", 12345678),
# ])
# print(d4)

# Modo 5
# d5 = dict(Nombre='Axel', Edad = 25, Documento=12345678)
# print(d5)

# Acceso
# print(d2["Nombre"])
# print(d2.get("Nombre"))
# print(d2.get("Profesion", "No encontrado"))

# Modificación
# d2["Nombre"] = "Axel Yoliston"
# print(d2["Nombre"])

# Agregar
# d2["Apellido"] = "Vasquez"
# print(d2["Apellido"])

# Limpiar diccionario
# d2.clear()
# print(d2)

# Convertir a lista
# it = d2.items()
# print(it)
# print(list(it))
# print(list(it)[0])

# Obtener llaves
# k = d2.keys()
# print(k)
# print(list(k))

# Obtener values
# v = d2.values()
# print(v)
# print(list(v))

# Diccionario anidado
# danidado = {
#     "1": d2,
#     "2": d2
# }
# print(danidado)