from time import sleep
u = None
num = int(input('Digite um número: >'))
num2 = int(input('Agora digite outro: >'))

while u != 5:
    print('-'*20)
    u = int(input('''[1] - SOMAR
[2] - MULTIPLICAR
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR DO PROGRAMA    >'''))
    print('='*20)
    if u == 1:
        res = num+num2
        print(f'{num}+{num2}={res} ')
    elif u == 2:
        res = num * num2
        print(f'{num}x{num2}={res}')
    elif u == 3:
        if num > num2:
            res = num
        else: res = num2
        print(f'O maior número é {res}')
    elif u == 4:
        num = int(input('Digite um número: >'))
        num2 = int(input('Agora digite outro: >'))
    else:
        if u != 5:
            print('Opção inválida! Tente novamente.')
    sleep(1)

print('ENCERRADO')
