#!\Users\Zoloo\AppData\Local\Programs\Python\Python310\python.exe

arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))

arquivo.close()
