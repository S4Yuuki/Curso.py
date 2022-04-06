from time import sleep
while True:
    num = int(input('Quer ver a tabuada de qual valor? >'))
    print('-'*20)
    if num < 0:
        break
    for tab in range (1,10+1):
        print(f'{num} x {tab} = {num*tab}')
    print('-' * 20)
    sleep(1)
print('Programa finalizado com sucesso!')