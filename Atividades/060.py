from math import factorial
num = int(input('Qual o número à fatorear? >'))

res = 1
f = num

while f > 0:
    print(f'{f}', end='')
    print(' x ' if f > 1 else ' = ', end='')
    res *= f
    f -= 1

#res = factorial(num)
print(res)
