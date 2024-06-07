# VARIABLE GLOBAL
PI = 3.1415

def area_circulo(radio):
    # VARIABLE LOCAL
    area = PI * pow(radio, 2)
    return area

print(area_circulo(2))