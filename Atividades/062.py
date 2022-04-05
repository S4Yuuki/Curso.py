print('='*30)
print('{:^30}'.format('10 TERMOS DE PA'))
print('='*30)

qnt = 10
pt = int(input('Qual o primeiro termo? >'))
razao = int(input('Qual a razão? >'))
res = pt
print('.'*30)
while qnt != 0:
    print(res, end='')
    print(' → ', end='')
    res += razao
    qnt -= 1
    if qnt == 0:
        print('')
        qnt = int(input('Deseja continuar mais quantas vezes? [0] - NÃO >'))

