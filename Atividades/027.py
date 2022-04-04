name = str(input('Insira seu nome completo: >')).strip().title()

splited = name.split()
getMax = len(splited)

print(f'''
Nome completo: {name}
Primeiro nome: {splited[0]}
Último nome: {splited[-1]}
''')