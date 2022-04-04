from math import sin,cos,tan,radians

ang = float(input('Digite o ângulo >'))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print(f'O ângulo de {ang} \nPossui o cosseno de {coss:.2f} \nSeno de {seno:.2f} \nTangente de {tang:.2f}')