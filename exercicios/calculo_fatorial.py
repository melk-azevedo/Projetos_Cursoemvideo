num = int(input('Digite um número para ver o seu fatorial: '))
cont = num
fator = 1
print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fator *= cont
    cont -= 1
print(f'{fator}')
