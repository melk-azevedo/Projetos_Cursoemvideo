from time import sleep
from random import randint


print('Devagar Radar a frente!')
sleep(3)

print('Você passou no radar.\n')
sleep(2)

vel = randint(35, 190)
print(f'Você estava a {vel}km/h\n')

multa = 7
limite = 120
minima = 40

if vel > limite:
    multa = (vel - limite) * multa
    print(f'''Você estava acima do limite de velocidade
e foi multado no valor de R${multa:.2f}''')
elif vel < minima:
    multa = (minima - vel) * multa
    print(f'''Você estava abaixo da velocidade minima da vai
e foi multado no valor de R${multa}''')
else:
    print('Continue respeitando os limites de velocidade.')
print('Bom dia, Dirija com segurança.')
