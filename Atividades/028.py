from random import randint

print('-_'*30)
guess = int(input('Estou pensando em um número de 1 à 5. Que número é esse?'))
print('_-'*30)

num = randint(1,5)

if guess >=6 or guess <1:
    print('X'*50)
    print('VOCÊ É BURRO? EU DISSE DE 1 À 5')
    print('X' * 50)
else:
    if guess == num:
        print('Você acertou! Parabéns!! Tome +10 créditos sociais')
    else:
        print(f'Errou feio, errou rude! Eu pensei em {num}. Perdeu -15 créditos sociais')
