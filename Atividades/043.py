altura = float(input('Digite a sua altura em M >'))
peso = float(input('Digite o seu peso em Kg >'))

imc = peso / (altura**2)

if imc < 18.5:
    status = 'abaixo do peso'
elif imc <25:
    status = 'peso ideal'
elif imc < 30:
    status = 'sobrepeso'
elif imc < 40:
    status = 'obesidade'
else:
    status = 'obesidade MÓRBIDA'

print(f'Seu status é: {status}. '
      f'Com o IMC de: {imc:.1f}.')