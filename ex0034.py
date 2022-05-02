'''salario = float(input('Informe o valor do seu salário: '))
if salario > 1250:
    print('Você recebera um aumento no valor de R${:.2f} e seu salário total será de R${:.2f}'.format(salario*0.1, (salario*0.1)+salario))
else:
    print('Você receberá um aumento no valor de R${:.2f} e seu salário total será de R${:.2f}'.format(salario*0.15,(salario*0.15)+salario))'''

salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
