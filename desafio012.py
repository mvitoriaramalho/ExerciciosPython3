valor = float(input('Qual o valor do produto? R$'))
novo = valor - (valor * 5 / 100)
print('O preço do produto é R${:.2f}, e com o desconto de 5% será R${:.2f}'.format(valor, novo))
