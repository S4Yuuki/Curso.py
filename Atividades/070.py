
nomeBarato = repetir = str(None)
total = qntCaro = valorBarato = 0

while True:
    print('-')
    nome = str(input('Nome do produto: >')).title().strip()
    preco = float(input('Preço: R$'))
    total += preco
    if preco >= 1000:
        qntCaro += 1
    if preco < valorBarato or valorBarato == 0:
        valorBarato = preco
        nomeBarato = nome
    while repetir not in 'SsNn':
        repetir = str(input('Quer continuar? [S/N] >')).lower().strip()[0]
    if repetir == 'n':
        break
    repetir = str(None)

print('{:=^40}'.format(' TOTAL '))
print(f'''TOTAL à pagar R${total:.2f}
{qntCaro} produto(s) acima de 1000,00 reais.
"{nomeBarato}" foi o produto mais barato da lista, custando R${valorBarato:.2f}
''')