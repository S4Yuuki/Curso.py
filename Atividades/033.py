n1 = int(input('Digite um número: >'))
n2 = int(input('Digite outro número: >'))
n3 = int(input('Digite mais um número: >'))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n2

medio = n1
if n2 > menor and n2 < maior:
    medio = n2
if n3 > menor and n3 < maior:
    medio = n3

print(f'O menor é {menor}')
print(f'O maior é {maior}')
print(f'O do meio é {medio}')

