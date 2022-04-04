n = int(input('Digite um número: >'))

primo = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[39m', end='')
    else: print('\033[31m', end='')
    print(f'{c} ',end='')

    if n % 1 == 0 and n % c == 0:
        primo +=1

print('\033[m')
if primo == 2:
    print(f'\nO número {n} é um número PRIMO')
else:
    print(f'\nO número {n} NÃO é um número PRIMO')