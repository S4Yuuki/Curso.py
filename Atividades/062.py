print('='*30)
print('{:^30}'.format('10 TERMOS DE PA'))
print('='*30)

qnt = 0
pt = int(input('Qual o primeiro termo? >'))
razao = int(input('Qual a razão? >'))
res = pt
print('.'*30)
while qnt != 10:
    print(res, end='')
    print(' → ', end='')
    res += razao
    qnt += 1
print('')
continuar = int(input(('Deseja continuar mais quantas vezes? [0] - NÃO >')))
while continuar != 0:
    print(res, end='')
    print(' → ', end='')
    continuar -= 1
    res +=razao