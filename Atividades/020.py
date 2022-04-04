from random import shuffle
n1 = input('Digite o nome da 1ª pessoa: >')
n2 = input('Digite o nome da 2ª pessoa: >')
n3 = input('Digite o nome da 3ª pessoa: >')
n4 = input('Digite o nome da 4ª pessoa: >')

embaralhar = [n1, n2, n3, n4]
shuffle(embaralhar)
print(f'A ordem será {embaralhar}')