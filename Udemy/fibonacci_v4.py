# Usando listas no lugar variáveis.

def fibonacci(limete):
    resultado = [0, 1]
    while resultado[-1] < limete:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
