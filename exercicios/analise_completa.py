from time import sleep


media = 0
mulhermenor = 0
idadevelho = 0
nomevelho = ''


for p in range(1, 5):
    print(f'------{p} PESSOA------')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    media += idade
    if p == 1 and sexo == 'M':
        idadevelho = idade
        nomevelho = nome
    if idade > idadevelho and sexo == 'M':
        idadevelho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenor += 1

print('ANALISANDO...')
sleep(2)

print(f'A média do grupo é {media/p:.1f} anos.')
print(f'O homem mais velho tem {idadevelho} anos e se chama {nomevelho}.')
print(f'Ao todo são {mulhermenor} mulheres menores de 20 anos.')
