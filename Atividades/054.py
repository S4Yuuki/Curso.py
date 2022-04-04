from datetime import date

maior = 0
menor = 0
data = date.today().year
for pessoas in range(7):
    p = int(input(f'Em que ano nasceu a pessoa {pessoas+1}? >'))

    if data - p >= 21:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas são de MAIOR idade.')
print(f'{menor} pessoas são de MENOR idade.')
