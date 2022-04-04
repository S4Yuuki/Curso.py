n1 = float(input('Digite um número inteiro ou fracionado >'))
n2 = float(input('Digite OUTRO número >'))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
else:
    print('Ambos os números possuem o mesmo valor')