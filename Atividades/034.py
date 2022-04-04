sal = float(input('Qual o salário à ser aumentado? R$'))

if sal > 1250:
    print(f'Seu novo salário será de R${sal + (sal*0.1):.2f}')
else:
    print(F'Seu novo salário será de R${sal + (sal*0.15):.2f}')
