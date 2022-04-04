valor = input('Digite qualquer coisa: ')

tipo = valor.__class__
espaco = valor.isspace()
num = valor.isnumeric()
alnum = valor.isalnum()
caps = valor.isupper()
low = valor.islower()
cap = valor.istitle()

print('Tipo {}\n' 
      'É vazio/espaço? {}\n'
      'É numérico? {}\n'
      'É alfanumérico? {}\n'
      'É maiúsculo? {}\n'
      'É minúsculo? {}\n'
      'É capitalizada? {}\n'
      .format(tipo,espaco,num,alnum,caps,low,cap))
