nnn = 0
soma = 0
while nnn != 999:
    nnn = int(input('Para parar, digite [999] >'))
    if nnn != 999:
        soma += nnn
print(f'A somatória final de todos os números inseridos foi {soma}.')