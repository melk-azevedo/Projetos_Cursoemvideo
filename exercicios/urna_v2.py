from time import sleep

idade = int(input('Digite a sua idade: '))
resposta = ''
if idade < 16:
    print('Você ainda não pode votar.')
    resposta = 'não'
elif 16 <= idade < 18 or idade > 65:
    print('Voto Opcional. \nDeseja votar nessa eleição ?')
    resposta = str(input('''
Digite (sim) para prosseguir ou (nao) para encerrar: ''')).strip().lower()
    if resposta == 'sim':
        print('Vamos votar!')
    else:
        print('Até a proxima eleição.')

else:
    print('Voto Obrigatório.')
    resposta = 'sim'

if resposta == 'sim':

    voto = idade

    voto_nulo = votoCand1 = votoCand2 = 0
    candidato_1 = 22
    candidato_2 = 44

    while voto != 0:
        voto = int(input('''Escolha uma opção:
[ 22 ] para Candidato_1
[ 44 ] para Candidato_2
[ 1 ] para nulo
[ 0 ] para sair
'''))
        if voto == 22:
            print('Você votou em Candidato_1')
            votoCand2 += 1
        elif voto == 44:
            print('Você votou em Candidato_2')
            votoCand1 += 1
        elif voto == 1:
            print('Voto Nulo')
            voto_nulo += 1
        elif voto == 0:
            voto = False
            print("Finalizando.")
            sleep(3)
        else:
            print('Opção inválida')

    print(f'''Votos Candidato_1: {votoCand2} \nVotos Candidato_2: {votoCand1}
Votos Nulos {voto_nulo}''')

    if votoCand2 < votoCand1:
        print('Temos para presidente o candidato Candidato_2.')
    elif votoCand1 < votoCand2:
        print('Temos para presidente o candidato Candidato_1.')
    else:
        print('Teremos um segundo turno.')
print('Obrigado por vir!')
