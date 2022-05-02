vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    print('MUTADO! Você exedeu o limite permitido que é de 800km/h')
    multa = (vel-80) * 7
    print('Você deve pagar uma muta de R${}'.format(multa))
else:
    print('Parabens você esta no limite da via boa viajem')
