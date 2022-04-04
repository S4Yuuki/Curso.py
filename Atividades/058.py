from random import randint
chance = 0
player = 0
pc = randint(1,10)

print('=-' * 20)
print('Estou pensando em um número de 1 à 10')
while player != pc:
    player = int(input('QUE NÚMERO É ESSE? >'))
    print('=-' * 20)
    if player < pc:
        print('ERRADO. Tente um valor mais alto.')
    elif player > pc:
        print('ERRADO. Tente um valor mais baixo.')
    chance += 1

print('')
#print('*'*20)
print(f'PARABÉNS! Você finalmente ganhou após {chance} tentativas! Haha')