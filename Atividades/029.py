km = int(input('Velocidade atual: '))

limite = int(80)
valorM = 7



if km >=0 and km < (limite-5):
    print(f'{km}Km/h')
    print('Você está dentro dos conformes. O máximo é 80Km/h')
    if km < (limite / 2):
        print('-'*20)
        print(f'Cuidado para não atrapalhar o trânsito. Vel. recomendada = {limite / 2}Km/h')

elif km <= limite and km >= (limite-5):
    print(f'{km}Km/h')
    print('CUIDADO! Você está quase acima do limite de 80Km/h')
else:
    multa = (km - limite) * valorM
    print(f'Você ultrapassou o limite. Uma multa de R${multa:.2f} será aplicada à você')