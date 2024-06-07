estudiantes = int(input("Ingresar cantidad de estudiantes: "))

i = 1
while estudiantes >= i:
  nombre = input("Estudiante {}: ".format(i))

  cursos = int(input("Ingresar cantidad de cursos: "))

  c = 1
  while cursos >= c:
    curso = input("Curso {}: ".format(c))
    c += 1

  i += 1