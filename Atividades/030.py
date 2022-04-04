num = int(input('Digite um número: >'))

resto = num % 2

if resto > 0:
    print('{}ÍMPAR{}'.format('\033[30;41m','\033[m'))

else: print('{}PAR{}'.format('\033[97;42m','\033[m'))