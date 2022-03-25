salario = float(input('Coloque o valor do seu salário atualmente: R$'))
novo = salario + (salario * 15 / 100)
print('Seu salário atual é de R${:.2f}, com o aumento de 15% será de {:.2f}'.format(salario, novo))
