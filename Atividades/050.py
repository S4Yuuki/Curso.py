s = 0
par = 0
for c in range (0,6):
    n = int(input('Digite um número: >'))
    if n % 2 ==0:
        s += n
        par +=1
print(f'A soma de {par} números pares foi {s}.')
