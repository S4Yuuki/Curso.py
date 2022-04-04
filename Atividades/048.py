s = 0
cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        s = s+c
        cont += 1
print(f'A soma de {cont} valores deu {s}')
