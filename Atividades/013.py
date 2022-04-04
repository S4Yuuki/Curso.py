sal = float(input('Qual o salário? R$'))
aumento = int(input('Qual a % do aumento? APENAS NÚMERO >'))

reajuste = sal+(sal *(aumento/100))

print(f'O salário novo será de R${reajuste:.2f}')