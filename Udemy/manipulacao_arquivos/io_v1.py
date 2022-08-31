#!\Users\Zoloo\AppData\Local\Programs\Python\Python310\python.exe

arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
