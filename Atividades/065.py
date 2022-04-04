somaMedia = 0
qnt = 1
loop = True
maior = 0
menor = 0
while loop == True:
    print('/'*20)
    num = int(input(f'Insira o {qnt}º número: >'))
    conf = str(input('Deseja continuar? [Y/N] >')).lower()
    if conf == 'y':
        qnt += 1
    elif conf == 'n':
        loop = False
    else:
        print('Valor inválido...')

    if num < menor or menor == 0:
        menor = num
    if num > maior or maior == 0:
        maior = num
    somaMedia += num
print('='*20)
print(f'A média de todos os números foi {somaMedia / qnt:.1f}')
print(f'O MENOR número foi {menor} e o MAIOR foi {maior}')