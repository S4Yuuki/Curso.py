sexo = str(input('Digite o seu sexo [M/F] >')).lower().strip()

#while sexo != 'm' and sexo != 'f':
while sexo not in 'mf':
    sexo = str(input('Dados inválidos. [M] / [F] >')).lower().strip()

if sexo == 'm':
    gender = 'masculino'
elif sexo == 'f':
    gender = 'feminino'
print('=-'*20)
print(f'SUCESSO! Sexo cadastrado como {gender.upper()}')