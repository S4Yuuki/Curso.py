valor = float(input('Insira a medida em metros: '))

print('{:.0f}cm\n'
      '{:.0f}mm\n'
      '{}km'.format(valor*100,valor*1000,valor/1000))