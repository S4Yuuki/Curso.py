vi = float(input('Qual a distância em KM até o seu destino? >'))

'''if vi > 200:
    valor = vi * 0.45
else:
    valor = vi * 0.5'''

valor = vi*0.45 if vi >200 else vi*0.5 #condição simplificada

print(f'A sua viagem de {vi}Km vai custar R${valor:.2f}')
