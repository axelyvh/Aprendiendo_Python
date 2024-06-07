# IF
edad = int(input("Ingresar edad: "))
if edad >= 18:
  print("Mayor de edad")

# IF ELSE
edad2 = int(input("Ingresar edad 2: "))
if edad2 >= 18:
  print("Mayor de edad")
else:
  print("menor de edad")

# ELIF
n = int(input("Ingresar numero: "))
if n > 0:
  print("Ingresaste un numero positivo")
elif n < 0:
  print("Ingresaste un numero negativo")
else:
  print("Ingresaste cero 1")

# ANIDADOS
edad3 = int(input("Ingresar edad 3: "))
if edad3 >= 18:
  print("Mayor de edad")
else:
  if edad3 > 0:
    print("Menor de edad")
  else:
    print("Edad no correcta")