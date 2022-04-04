l1 = float(input('Insira o 1º lado do triângulo: >'))
l2 = float(input('Insira o 2º lado do triângulo: >'))
l3 = float(input('Insira o 3º lado do triângulo: >'))

if l1 < l2+l3 and l2 < l1 + l3 and l3 < l1+l2:
    print('É possível formar um triângulo')
else:
    print('NÃO é possível formar um triângulo')




