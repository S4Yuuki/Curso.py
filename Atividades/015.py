day = int(input('Quantos dias o carra foi alugado? >'))
km = float(input('Quantos Km o carro andou? >'))

ppd = 60 * day
ppkm = 0.15 * km

print(f'O preço a ser pago pelo veículo é de R${ppd+ppkm:.2f}')