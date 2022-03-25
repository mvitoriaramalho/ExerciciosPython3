l = float(input('Digite aqui a altura em metros:'))
b = float(input('Dgite aqui a largura em metros:'))
a = b * l
print('Sua parede tem a dimensão de {}x{} e área é de {}m².'.format(l, b, a))
t = a / 2
print('Para pintar sua parede, você precisará de {}l de tinta.'.format(t))