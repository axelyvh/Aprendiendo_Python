dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("UTILIZANDO FOR")
for item in dias:
    print(item)

print("UTILIZANDO RANGE")
for item in range(len(dias)):
    print(dias[item])

print("UTILIZANDO ENUMERATE")
for i, item in enumerate(dias):
    print(i, item)