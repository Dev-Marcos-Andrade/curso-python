'''num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print('O numero digitado foi: {}'.format(num))
print('Sua unidade é: {}'.format(num[3]))
print('Sua dezena é: {}'.format(num[2]))
print('Sua centena é: {}'.format(num[1]))
print('Seu milhar é: {}'.format(num[0]))'''

num = int(input('Informa um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Sua unidade é {}'.format(u))
print('Sua dezena é {}'.format(d))
print('Sua centena é {}'.format(c))
print('Seu milhar é {}'.format(m))
