#!\Users\Zoloo\AppData\Local\Programs\Python\Python310\python.exe

with open('pessoas.csv') as arquivo:
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.close:
    print('Arquivo já foi fechado!')
