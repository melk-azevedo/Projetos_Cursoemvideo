# Simplificando as variáveis.

def fibonacci(limete):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limete:
        penultimo, ultimo = ultimo, penultimo + ultimo
        print(f'{ultimo}', end=',')


if __name__ == '__main__':
    fibonacci(17000)
