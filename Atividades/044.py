
x = None
def cartao():
    global x
    global total
    print('{:-^40}'.format(' CARTÃO DE CRÉDITO '))
    x = int(input('MIN 2x / MAX 12x  >'))

    if x != None:
        if x == 2:
            total = valor  # / 2
        elif x > 2 and x < 13:
            total = (valor + (valor * 0.2))  # / x
        elif x == input(''):
            inicio()
        else:
            print('Método indisponível')
            cartao()

def inicio():
    global valor
    global forma
    global total
    valor = float(input('Valor R$'))
    print('{:*^40}'.format(' FORMA DE PAGAMENTO '))
    print(f'Qual será a forma de pagamento do produto custando R${valor:.2f}? ')

    forma = str(input('[1] - Dinheiro à vista / [2] - Cartão à vista / ENTER para cartão >')).lower().strip()

    if forma == '1':
        total = valor - (valor * 0.1)
    elif forma == '2':
        total = valor - (valor * 0.05)
    elif forma == '':
        cartao()
    else:
        inicio()
    resultado()




def resultado():
    print('{:-^40}'.format(' TOTAL '))
    print(f'O total a pagar é de R${total:.2f} ',end='')
    if x != None:
        print(f'em {x} vezes de R${total/x:.2f}.')


inicio()