name = str(input('Digite o nome da sua cidade: >')).strip()

splitado = name.split()

if 'santo' in splitado[0].lower():
    print('A sua cidade começa com Santo')

else: print('A sua cidade NÃO começa com Santo')
