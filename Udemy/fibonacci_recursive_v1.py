def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante colocar a condição  de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 15 primeiros números da sequência
    for fib in fibonacci(15):
        print(fib)
