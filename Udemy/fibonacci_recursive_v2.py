# Refatoração usando operador ternario

def fibonacci(quantidade, sequencia=(0, 1)):
    # Importante colocar a condição  de parada
    return sequencia if len(sequencia) == quantidade else \
        fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    # Listar os 15 primeiros números da sequência
    for fib in fibonacci(15):
        print(fib)
