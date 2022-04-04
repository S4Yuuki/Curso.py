fib = int(input('Quantas vezes deseja mostrar a sequência Fibonacci? >'))
valorAnt = 0
valorAgr = 0
while fib != 0:
    print(valorAgr, end='')
    print(' → ', end='')

    if valorAnt == 0:
        valorAgr = 1
    else:
        valorAgr = valorAnt + valorAgr

    valorAnt = valorAgr
    fib -= 1
