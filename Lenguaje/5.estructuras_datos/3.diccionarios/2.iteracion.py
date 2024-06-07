d1 = {
    "Nombre": "Axel",
    "Edad": 25,
    "Documento": 12345678
}
print(d1)

# Obteniendo las claves
for item in d1:
    print(item)

# Obteniendo los valores
for item in d1:
    print(d1[item])

# Obteniendo clave y valor
for x, y in d1.items():
    print(x, y)