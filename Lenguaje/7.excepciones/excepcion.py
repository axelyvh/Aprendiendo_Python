# ZeroDivisionError
try:
    resultado = 10 * (1 / 0)
    print(resultado)
except:
    print("Error de ZeroDivisionError")

# TypeError
try:
    resultado = '2' + 2
    print(resultado)
except:
    print("Error de TypeError")