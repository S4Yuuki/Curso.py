largura = float(input('Qual a LARGURA em m da parede? >'))
altura = float(input('Qual a ALTURA em m da parede? >'))

m2 = largura*altura
litro = m2/2

print('Sua parede tem a dimensão de {}x{}. E a área de {}m², você iria precisar de {:.1f}L de tinta'.format(largura,altura,m2,litro))