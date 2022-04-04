l1 = float(input('Insira o lado 1 do triângulo: >'))
l2 = float(input('Insira o lado 2 do triângulo: >'))
l3 = float(input('Insira o lado 3 do triângulo: >'))


print('<>'*20)
if l1 < l2+l3 and l2 < l1+l3 and l3 < l1+l2:
    print('É possível SIM, formar um triângulo')

    if l1 == l2 and l2 == l3 and l3 == l1:
        print('EQUILÁTERO')
    elif l1 == l2 and l1 != l3 or l2 == l3 and l2 != l1 or l3 == l1 and l3 != l2:
        print('ISÓSCELES')
    else:
        print('ESCALENO')


else:
    print('NÃO é possível formar um triângulo com base nessas medidas.')

