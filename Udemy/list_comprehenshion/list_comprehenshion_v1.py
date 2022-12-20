triplo = [i * 3 for i in range(10)]
print(triplo)

# [ expressão for item in list if condicional ]

dobro = [d * 2 for d in range(10) if d % 2 == 0]
print(dobro)

# Versão "Normal"
dobro = []
for i in range(10):
    if i % 2 == 0:
        dobro.append(i * 2)
print(dobro)
