qnt = 0
maxIdade = 0
nomeMVelho = None
idadeMVelho = 0
qntMulheres = 0

for dados in range(4):
    nome = str(input(f'Qual o nome {dados+1}? > ')).strip()
    nomesplitado = nome.split()
    idade = int(input(f'Qual a sua idade, {nomesplitado[0]}? >'))
    sexo = str(input(f'Sexo? [M]asculino/[F]eminino >')).lower()
    qnt +=1
    maxIdade += idade
    if idade > idadeMVelho and sexo == 'm':
        idadeMVelho = idade
        nomeMVelho = nome
    if idade < 20 and sexo == 'f':
        qntMulheres += 1
    print('-'*20)

print(f'''A média de idade é {maxIdade/qnt:.1f}
O homem mais velho é o {nomeMVelho}, com {idadeMVelho} anos.
Existe(m) {qntMulheres} mulher(es) abaixo de 20 anos
''')
