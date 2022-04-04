from datetime import date

ano = int(input('Insira a data de nascimento: >'))

idade = date.today().year - ano

if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 25:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'

cores = {
    'verde': '\033[32m',
    'limpo': '\033[m'
}
print('💦'*20)
print('Categoria {}{}{}'.format(
    cores['verde'], categoria, cores['limpo']
))
