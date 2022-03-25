dia = float(input('Digite aqui a quantidade de dias:'))
km = float(input('Digite aqui a quantidade de KM rodados:'))
d = dia * 60.00
k = km * 0.15
t = d + k
print('Você alugou o carro por {} dias e rodou {}KM. O valor a ser pago por dia alugado é: R${:.2f}, e por KM rodado é'
      'R${:.2f}. O total é: R${:.2f}.'.format(dia, km, d, k, t))