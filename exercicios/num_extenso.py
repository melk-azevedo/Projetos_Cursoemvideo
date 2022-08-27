cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Voce escolheu o número {cont[num]}')
        resposta = str(input('Voce quer continuar? [S/N] ')).strip().upper()[0]
        if resposta == 'S':
            continue
        else:
            break
    print('Tente novamente.', end=' ')
