frase = str(input('Digite uma frase qualquer: >')).strip()

print(f'''
A sua frase possui: {frase.lower().count('a')} letras 'A'
Ela aparece pela primeira vez na casa {frase.lower().find('a')} ({frase.lower().find('a')+1})
Ela aparece pela última vez na casa {frase.lower().rfind('a')} ({frase.lower().rfind('a')+1})
{len(frase)}
{frase[44:]}
''')
