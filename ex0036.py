casa = float(input('Valor da casa: R$ '))
salário = float(input('Quanto você recebe: R$ '))
anos = int(input('Em quantos anos quer pagar: '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!!!')
else:
    print('Empréstimo NEGADO!!!')
    