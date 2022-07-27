# Atribuindo Limite para a sequência.
def fibonacci(limete):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo},{ultimo}', end=',')
    while ultimo < limete:
        proximo = penultimo + ultimo
        print(f'{proximo}', end=',')
        penultimo = ultimo
        ultimo = proximo


if __name__ == '__main__':
    fibonacci(17000)
