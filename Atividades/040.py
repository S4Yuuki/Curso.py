n1 = float(input('Digite a primeira nota: >'))
n2 = float(input('Digite a segunda nota: >'))

media = (n1+n2)/2
cores = {'vermelhoNeg':'\033[1;31m',
         'verdeNeg':'\033[1;32m',
         'amareloNeg':'\033[1;33m',
         'limpo' : '\033[m'
         }

if media < 5:
    print('A sua média é de {}{:.1f}{}. Você está {}REPROVADO!{}'.format(
    cores['vermelhoNeg'],media,cores['limpo'],cores['vermelhoNeg'],cores['limpo']
    ))
elif media < 6.9:
    print('A sua média é de {}{:.1f}{}. Você está em {}RECUPERAÇÃO!{}'.format(
    cores['amareloNeg'],media,cores['limpo'],cores['amareloNeg'],cores['limpo']
    ))
else:
    print('A sua média é de {}{:.1f}{}. Você foi {}APROVADO!{}'.format(
    cores['verdeNeg'],media,cores['limpo'],cores['verdeNeg'],cores['limpo']
    ))