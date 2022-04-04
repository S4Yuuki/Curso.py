magro = 0
gordo = 0
for peso in range(5):
    p1 = float(input(f'Qual o peso {peso+1}? >'))

    if p1 < magro or magro == 0:
        magro = p1
    elif p1 > gordo:
        gordo = p1

print(f'O MENOR peso é {magro}, e o MAIOR peso é {gordo}')