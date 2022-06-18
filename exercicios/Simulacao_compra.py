print('》》》LOJAS MELK.py 《《《')


compras = float(input('\nDigite o valor das compras: R$'))
avista = compras - (compras * 10 / 100)
cartao = compras - (compras * 5 / 100)
juros = compras / 0.80


print('''\nFORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opcao = int(input('Digite a opção: '))


if opcao == 1:
    print(f'\nSua compra teve um desconto de 10% e o total é  R${avista:.2f}.')
elif opcao == 2:
    print(f'Sua compra teve um desconto de 5% e o total é R${cartao:.2f}')
elif opcao == 3:
    print(f'sua compra será parcelada em 2x de R${compras/2:.2f} ')
elif opcao == 4:
    parcela = int(input('Quantas parcelas: '))
    print(
        f'''Sua compra será parcelada em {parcela}x de {juros / parcela:.2f} COM JUROS.
Sua compra de R${compras:.2f} vai custar R${juros:.2f} no final.''')
else:
    print('\nOpção invalida, por favor tente outra vez!')
