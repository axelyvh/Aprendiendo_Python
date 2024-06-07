# EJERCICIO 1
# elementos = [1,2,3,4,5]
# for item in elementos:
#     print(item)

# EJERCICIO 2
# for item in range(10):
#     print(item)

# EJERCICIO 3
# for item in range(5, 10):
#   print(item)

# EJERCICIO 4
# for item in range(10, 100, 10):
#   print(item)

# EJERCICIO 5
# A = int(input("Ingresar cantidad de alumnos: "))
# for a in range(A):
#     alumno = input("Alumno {}: ".format(a))
#     C = int(input("Ingresar cantidad de cursos: "))
#     for c in range(C):
#         curso = input("Cursos {}: ".format(c))

numero = 10 
i = 1 
for item in range(10): 
    print(item) 
    while item > i: 
        i += 1 
        print(i)