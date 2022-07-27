# Usando a função 'sum'.

def fibonacci(limete):
    resultado = [0, 1]
    while resultado[-1] < limete:
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10000):
        print(fib)
