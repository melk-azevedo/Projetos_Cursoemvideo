#!\Users\Zoloo\AppData\Local\Programs\Python\Python310\python.exe

try:
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

finally:
    arquivo.close()

if arquivo.close:
    print('Arquivo já foi fechado!')
