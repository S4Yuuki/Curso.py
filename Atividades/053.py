p = str(input('Digite uma palavra ou frase: >')).strip().upper()
psplitada = p.split()
pjunto = ''.join(psplitada)

'''
resultado = str('')

for trasprafrente in range (len(pjunto)-1,0-1,-1):
    resultado += pjunto[trasprafrente]'''

resultado = pjunto[::-1]
print(pjunto,' / ', resultado)
if resultado == pjunto:
    print('A frase digitada é um palíndromo')
else:
    print('NÃO é um palíndromo')