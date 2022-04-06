qnt = soma = 0
while True:
    num = int(input('Digite um valor ou [999] P/ PARAR: >'))
    if num == 999:
        break
    soma += num
    qnt += 1
print(f'Foram digitados {qnt} números e a soma total foi de {soma}')