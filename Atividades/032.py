from datetime import date

ano = int(input('Qual ano deseja analisar? 0 para ano atual >'))

if ano == 0:
    ano = date.today().year
if ano % 4==0 and ano % 100 != 0 or ano % 400==0:
    print(f'O ano de {ano} é um ano bissexto')
else:
    print(f'Este ano {ano} NÃO é bissexto')

