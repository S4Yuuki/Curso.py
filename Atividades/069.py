over18 = men = wUnder20 = 0

while True:
    sexo = again = str(None)


    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)

    idade = int(input('Idade: >'))
    if idade >= 18:
        over18 += 1

    while sexo not in 'fFmM':
        sexo = str(input('Sexo: [M/F] >')).lower().strip()[0]
        if sexo == 'f' and idade < 20:
            wUnder20 += 1
        elif sexo == 'm':
            men += 1

    print('-'*30)
    while again not in 'SsNn':
        again = str(input('Quer continuar? [S/N] >')).lower().strip()[0]
    if again == 'n':
        break

print(f'''{over18} total de pessoas acima de 18 anos.
{men} pessoa(s) do sexo masculino cadastradas.
{wUnder20} pessoa(s) do sexo feminino abaixo de 20 anos.
''')
