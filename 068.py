import time
from random import randint
qnt = 0

print('=-'*20)
print('{:^40}'.format('JOGO DO PAR OU ÍMPAR'))

while True:
    print('=-' * 20)
    num = int(input('Digite um valor: >'))
    poi = ' '
    while poi not in 'pPiI':
        poi = str(input('PAR ou ÍMPAR? [P/I]>')).lower().strip()[0]
    pc = randint(0,10)
    print('-'*40)
    print(f'Eu joguei {pc} e você jogou {num}. TOTAL {num+pc}',end=' ')
    time.sleep(1.5)
    if (num+pc) % 2 == 0:
        print('DEU PAR')
        if poi == 'p':
            print('VOCÊ VENCEU!')
            qnt +=1
        else:
            print('VOCÊ PERDEU!')
            break
    else:
        print('DEU ÍMPAR')
        if poi == 'i':
            print('VOCÊ VENCEU!')
            qnt +=1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
    time.sleep(2)
print('=-'*20)
print(f'GAME OVER! Você venceu {qnt} vez(es)')


