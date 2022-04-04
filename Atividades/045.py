import time
from random import choice, randint

def jogo():
    global user
    user = int(input('[0]-Pedra, [1]-Papel, [2]-Tesoura >'))
    time.sleep(1)
    processo()

def processo():
    global user
    lista = ('PEDRA', 'PAPEL', 'TESOURA')
    pc = randint(0,2)

    print(' '*10)
    if user == 0 and pc == 1 or user == 1 and pc == 2 or user == 2 and pc == 0:
        derrota = True
    else:
        derrota = False

    if derrota == True:
        print('Você PERDEU!')
    elif pc == user or user == pc:
        print('EMPATAMOS!')
    else:
        print('Parabéns! Você ganhou!')


    print('- '*10)
    print(f'EU joguei [{lista[pc]}] e VOCÊ jogou [{lista[user]}]...')
    print('_'*40)
    time.sleep(2)
    jogo()

jogo()