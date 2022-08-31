#!\Users\Zoloo\AppData\Local\Programs\Python\Python310\python.exe

with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)

if arquivo.close:
    print('Arquivo já foi fechado!')

if saida.close:
    print('Arquivo de saída já foi fechado!')
