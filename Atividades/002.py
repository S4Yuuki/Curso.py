import time

nome = None

def bemVindo():
    global nome
    nome = input('Insira seu nome: ')

    confirm = input('Isso está correto? "{}"  S/N >'.format(nome)).lower()

    if confirm == 's':
        nome = nome
    else:
        bemVindo()

bemVindo()

time.sleep(1)
print('Bem vindo, ',nome)




