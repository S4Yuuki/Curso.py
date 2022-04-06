# [50] [20] [10] [1]
print('='*30)
print('{:^30}'.format('BANCO'))
print('='*30)

sacar = int(input('Qual o valor à ser sacado? >'))
cinq = vinte = dez = um = 0
total = 0

while True:
    if total + 50 <= sacar:
        total += 50
        cinq += 1
    elif total + 20 <= sacar:
        total += 20
        vinte += 1
    elif total + 10 <= sacar:
        total += 10
        dez += 1
    elif total + 1 <= sacar:
        total +=1
        um += 1

    if total >= sacar:
        break
print('-'*30)
print(f'TOTAL DE R$ {total},00')
print(f'''R$50,00 → ({cinq})
R$20,00 → ({vinte})
R$10,00 → ({dez})
R$ 1,00 → ({um})''')
print('-'*30)