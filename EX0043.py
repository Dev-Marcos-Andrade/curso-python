peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso!!')
elif 18.5 <= imc < 25:
    print(' Você esta no peso ideal!!')
elif 25 <= imc < 30:
    print('Você esta com sobrepeso!!')
elif 30 <= imc < 40:
    print('Você esta com obesidade!!')
else:
    print('Você esta com obesidade mórbida!!')
