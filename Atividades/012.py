valor = float(input('Qual o valor do produto? R$'))
prcnt = int(input('Quanto % de desconto? >'))

prcnt2 = float(prcnt) /100
desc = valor -(valor * prcnt2)


print(f'O produto com {prcnt}% OFF vai custar {desc:.2f}')