def imprimir(maxima, atual):
    if atual < maxima:
        print(atual)
        imprimir(maxima, atual + 1)


imprimir(20, 1)
