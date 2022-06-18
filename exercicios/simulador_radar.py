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

if vel > limite:
    multa = (vel - limite) * multa
    print(f'''Você estava acima do limite de velocidade
e foi multado no valor de R${multa:.2f}''')
else:
    print('Continue respeitando os limites de velocidade.')
print('Bom dia, Dirija com segurança.')
