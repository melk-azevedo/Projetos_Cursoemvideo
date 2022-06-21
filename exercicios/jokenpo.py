from random import randint
from time import sleep

print('-=--' * 5)
print('Vamos jogar jokenpô')
print('-=--' * 5)

print('')

computador = randint(1, 3)
if computador == 1:
    computador = 'PEDRA'
elif computador == 2:
    computador = 'PAPEL'
elif computador == 3:
    computador = 'TESOURA'

jogador = int(input('''Faça a sua escolha:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA\n'''))
if jogador == 1:
    jogador = 'PEDRA'
elif jogador == 2:
    jogador = 'PAPEL'
elif jogador == 3:
    jogador = 'TESOURA'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

print(f'\nComputador escolheu {computador} e Jogador escolheu {jogador}.\n')


if computador == jogador:
    print('Poxa deu empate, que tal outra vez ?')
elif computador == 'PEDRA' and jogador == 'TESOURA':
    print('Computador venceu..')
elif computador == 'PAPEL' and jogador == 'PEDRA':
    print('Computador venceu..')
elif computador == 'TESOURA' and jogador == 'PAPEL':
    print('Computador venceu..')
else:
    print('Parabéns jogador venceu!')
