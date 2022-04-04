from datetime import date
ano = int(input('Digite apenas o ANO de nascimento >'))
sexo = str(input('[M]=Masculino / [F]=Feminino >')).lower()

idade = date.today().year - ano
cores = {'vermelho':'\033[31m',
         'verde':'\033[32m',
         'limpo':'\033[m',
         'vermelhão':'\033[1;7;31;40m'}

if idade < 18:
    print('{}Você ainda não está apto para se alistar. Isso só é possível{}\n'
          '{}com 18 anos{}.'.format(
        cores['vermelho'],cores['limpo'],cores['vermelho'],cores['limpo']
    ))
    print(f'Tempo previsto: {18-idade} anos ({date.today().year+(18-idade)})')
elif idade == 18:
    print('{}Você está na idade de se alistar!{}\n'
          '{}Apresente-se à junta militar mais próxima de você em qualquer momento.{}'.format(
        cores['verde'], cores['limpo'],cores['verde'], cores['limpo']
    ))
else:
    print('{}Já passou da hora de se alistar. Uma pequena multa será aplicada{}\n'
          '{}devido ao prazo. Apresente-se à junta militar mais próxima IMEDIATAMENTE!{}'.format(
      cores['vermelhão'], cores['limpo'],cores['vermelhão'], cores['limpo']
    ))
    print(f'Tempo excedido: {idade-18} anos ({date.today().year-(idade-18)})')

if sexo == 'f':
    print('>>>O serviço de alistamento é obrigatório apenas para pessoas nascidas no sexo masculino')