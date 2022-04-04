name = str(input('Digite aqui o seu nome completo >')).strip()

dividedName = name.split()
tirarEspaco = name.count(' ')

print(f'''
{name.upper()}
{name.lower()}

Letras sem espaço:
{len(name) - tirarEspaco}

Letras primeiro nome:
{len(dividedName[0])}  ''')