from random import randint
from time import sleep

print('-=--' * 5)
print('Vamos jogar jokenpô')
print('-=--' * 5)

print('')

pont_c = 0
pont_j = 0
rodada = 0

while rodada < 3:
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
    else:
        print('Jogada inválida')
        break

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')

    print(
        f'\nComputador escolheu {computador} e Jogador escolheu {jogador}.\n')
    if computador == jogador:
        print('Poxa deu empate, que tal outra vez ?\n')
    elif computador == 'PEDRA' and jogador == 'TESOURA':
        print('Computador venceu a rodada.\n')
        rodada += 1
        pont_c += 1
    elif computador == 'PAPEL' and jogador == 'PEDRA':
        print('Computador venceu a rodada.\n')
        pont_c += 1
    elif computador == 'TESOURA' and jogador == 'PAPEL':
        print('Computador venceu a rodada.\n')
        rodada += 1
        pont_c += 1
    else:
        print('Jogador venceu a rodada.\n')
        rodada += 1
        pont_j += 1

print(f'O resultado foi computador {pont_c} vs {pont_j} jogador.\n')
if pont_c > pont_j:
    print('Computador ganhou!')
elif pont_j > pont_c:
    print('Parabéns jogador ganhou!')
else:
    print('Não houve ganhadores!')
