valor = float(input('Quantos R$ deseja converter? >'))

conversor = valor * 0.20
conversor2 = valor /5.01

print('\nCom R${:.2f}, você consegue adquirir US${:.2f}'.format(valor,conversor))
print('convertido com base na data de 03/2022')
print('\nCom R${:.2f}, você consegue adquirir US${:.2f}'.format(valor,conversor2))