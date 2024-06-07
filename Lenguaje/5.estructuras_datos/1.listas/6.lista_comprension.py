numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista por comprension
r2 = [e * 2 for e in numeros]

# Lista por comprension y condicional
r3 = [e * 2 for e in numeros if e > 4]

print(numeros)
print(r2)
print(r3)
