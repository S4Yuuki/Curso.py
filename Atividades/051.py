print('='*25)
print('{:^25}'.format('10 TERMOS DE UMA P.A.'))
print('='*25)

pt = int(input('Qual o primeiro termo? >'))
r = int(input('Razão: >'))
print('.'*25)

for pa in range(pt, pt+10*r, r):
    print(f'{pa} → ', end='')
print('.')