n = int(input('Digite um número >'))
forma = int(input('[1]=Binário, [2]=Octal, [3]=Hexadecimal >'))

if forma == 1:
    print(f'{n} convertido para binário == {bin(n)[2:]}')
elif forma ==2:
    print(f'{n} convertido para octal == {oct(n)[2:]}')
elif forma ==3:
    print(f'{n} convertido para hexadecimal == {hex(n)[2:]}')

else:
    print("BURRO. Não tem essa opção.")