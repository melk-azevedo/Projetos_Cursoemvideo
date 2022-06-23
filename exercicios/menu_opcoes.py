from time import sleep 


opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 5:
	print('''
	[ 1 ] somar
	[ 2 ] multiplicar
	[ 3 ] maior
	[ 4 ] novos números
	[ 5 ] sair do programa
	''')
	opcao = int(input('>>>>>>>Escolha uma opção: '))
	if opcao == 1:
		somar = n1 + n2
		print(f'A soma de {n1} + {n2} é {somar}.')
	elif opcao == 2:
		multi = n1 * n2
		print(f'A multiplicação de  {n1} × {n2} é {multi}')
	elif opcao == 3:
		if n1 > n2:
			print(f'Entre {n1} e {n2} o maior é {n1}')
		elif n1 < n2:
			print(f'Entre {n1} e {n2} o maior é {n2}')
		else:
			print('Nenhum número é maior os dois são iguais.')
	elif opcao == 4:
		print('Digite os numeros novamente:')
		n1 = int(input('Primeiro valor: '))
		n2 = int(input('Segundo valor: '))
	else:
		if opcao != 5:
			print('Opção inválida!')
	print('==-'*10)
	sleep(1)
else:
	print('Finalizando...')

sleep(2)
print('Fim do programa volte sempre!')
