viagem =  int(input('Digite o km da viagem:'))
valor1 = 0.50
valor2 = 0.45
print('Você esta preste a fazer uma viagem de {}km'.format(viagem))
if viagem <= 200:
    print('O valor da sua viagem é de R${}'.format(viagem*valor1))
else:
    print('O valor da sua viagem é de R${}'.format(viagem*valor2))