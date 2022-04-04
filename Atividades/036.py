import time

casa = float(input('Qual o valor da casa em questão? R$'))
sal = float(input('Qual o salário do comprador? R$'))
anos = int(input('Em quantos anos EXATOS você deseja pagar? >'))

trintaPCen = sal * 0.3

anoMes = anos * 12
mensalidade = casa / anoMes


cores = {'vermelho':'\033[31m',
         'limpo': '\033[m',
         'verde': '\033[32m'}

print('\033[97;40mCalculando...\033[m')
time.sleep(2)

if mensalidade > trintaPCen:
    print('{}Infelizmente{} o preço da parcela iria lhe causar prejuízo. \n'
          'Recomendamos aumentar o tempo das parcelas, ou procurar por outra opção.'.format(
        cores['vermelho'],cores['limpo']))

    print(cores['vermelho'])

else:
    print('{}Parabéns!{} O preço está em conta com o seu salário.\n'
          'Em instantes disponibilizaremos um link e enviaremos para o seu email.\n'
          'AGUARDE!'.format(cores['verde'],cores['limpo']))

    print(cores['verde'])

time.sleep(1)
print('-='*30)
time.sleep(1)
print(f'Valor à pagar R${mensalidade:.2f}/mês, durante {anos} anos.')
print(f'•O valor máximo com base no seu salário é de {trintaPCen:.2f}')
print(cores['limpo'])