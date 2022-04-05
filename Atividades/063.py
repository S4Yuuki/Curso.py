fib = int(input('Quantas vezes deseja mostrar a sequência Fibonacci? >'))
print('.'*20)
v1 = 0
v2 = 1
qnt = 3
print(f'{v1} → {v2}', end='')

while qnt <= fib:
    v3 = v1 + v2
    print(f' → {v3}', end='')
    qnt += 1
    v1 = v2
    v2 = v3
